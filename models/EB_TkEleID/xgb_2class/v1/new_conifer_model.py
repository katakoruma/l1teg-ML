#%%
# %load_ext autoreload
# %autoreload 2

import sys
sys.path.append("/afs/cern.ch/work/l/lekerner/code/l1teg-ML/models/EB_TkEleID/xgb_2class/v1/")
sys.path.append("/afs/cern.ch/work/l/lekerner/code/l1teg-ML/utils/BitHub")
import os
import conifer

import numpy as np
import xgboost as xgb
import shutil

from custom.data import (
    generate_paths,
    load_df,
    concatenate,
    df_to_DMatrix
)

from custom.plot.post_train import (
    plot_loss,
    plot_importance,
    plot_scores,
    plot_roc,
    plot_roc_bins,
    plot_quant_aucs,
)

from params_pu200 import path, features, auxiliary, tag, P0, dir
precision = 64

# path = '/eos/user/l/lekerner/www/l1teg/Barrel/2'
# dir = "q_8"

os.environ["PATH"] = "/home/Xilinx/Vivado/2023.1/bin:/home/Xilinx/Vitis_HLS/2023.1/bin:" + os.environ["PATH"]
os.environ["XILINX_AP_INCLUDE"] = "/afs/cern.ch/work/l/lekerner/code/l1teg-ML/tasks/EB_TkEle/v0/cpp/conifer/Vitis_HLS/simulation_headers/include"
os.environ["JSON_ROOT"] = "/afs/cern.ch/work/p/pviscone/conifer"


from bithub.scalers import BitScaler


import matplotlib.pyplot as plt
import mplhep as hep
hep.set_style("CMS")


destination_dir = f"{path}/results/{dir}"
os.makedirs(destination_dir, exist_ok=True)
shutil.copy(__file__, os.path.join(destination_dir, "new_conifer_model.py"))


#%%
#!----------------------Load Data----------------------!#
def get_dmatrix(precision = None, q_scaler="float"):
    paths = generate_paths(P0, tag, [
        "DoubleElectron_PU200_test",
        "MinBias_test",
    ])
    sig_test, bkg_test = load_df(
        *paths, branches=features + auxiliary
    )
    bkg_test=bkg_test[:len(sig_test)]
    df_test = concatenate(
        {"test": [sig_test, bkg_test]}
    )

    scaler = BitScaler()
    scaler.load(f"{path}/results/{dir}/scaler.json")


    dmatrix = df_to_DMatrix(
        df_test,
        features=features,
        y="TkEle_label",
        bitscaler=scaler,
        ap_fixed=(precision,32,"AP_RND_CONV", "AP_SAT") if precision else None
    )
    return df_test, dmatrix



#%%
def convert(backend, precision, build=False, predict=False):
    df_test, dmatrix = get_dmatrix(q_scaler=precision)

    model = f"{path}/results/{dir}/model.json"
    #!----------------------VIVADO ENVS----------------------!#
    os.environ["PATH"] = "/data2/Xilinx/Vivado/2024.2/bin:/data2/Xilinx/Vitis_HLS/2024.2/bin:" + os.environ["PATH"]

    #!----------------------CFG----------------------!#
    if backend == "vivado":
        cfg = conifer.backends.xilinxhls.auto_config(granularity="full")
        cfg["XilinxPart"] = "xcvu13p-flga2577-2-e"
        cfg['InputPrecision'] = f"ap_fixed<{precision},32,AP_RND_CONV,AP_SAT>"
        cfg['ThresholdPrecision'] = f"ap_fixed<{precision},32,AP_RND_CONV,AP_SAT>"
        cfg['ScorePrecision'] =  f"ap_fixed<{precision},32,AP_RND_CONV,AP_SAT>"
        cfg['ClockPeriod'] = 4.16666666


    elif backend == "py":
        cfg = {"backend": "py", "output_dir": "dummy", "project_name": "dummy", "Precision": "float"}

    elif backend == "cpp":
        cfg = conifer.backends.cpp.auto_config()
        cfg["Precision"] = f"ap_fixed<{precision},32,AP_RND_CONV,AP_SAT>"
        cfg["score_precision"] = "ap_fixed<64,32,AP_RND_CONV,AP_SAT>"

    cfg["OutputDir"] = f"{path}/results/{dir}/conifer_model_{backend}"


    #!----------------------Load Model----------------------!#
    xgb_model = xgb.Booster()
    xgb_model.load_model(model)

    #!----------------------Convert Model----------------------!#
    hls_model = conifer.converters.convert_from_xgboost(xgb_model, cfg)
    print(f"Model Converted to {backend}")
    hls_model.compile()
    print("Model compiled")
    if build:
        hls_model.build()
        print("Model built")

    #!----------------------Predict----------------------!#
    if predict:
        raw_func = lambda x: np.log(x / (1 - x)) / 8
        xgb_preds = xgb_model.predict(dmatrix)
        xgb_preds = raw_func(xgb_preds)

        hls_preds = hls_model.decision_function(dmatrix.get_data().toarray())
        hls_preds = hls_preds / 8

        df_test["TkEle_xgb_score"] = xgb_preds
        df_test["TkEle_hls_score"] = hls_preds

        return df_test, cfg, xgb_model, xgb_preds, hls_model, hls_preds, dmatrix
    else:
        return df_test, cfg, xgb_model, hls_model, dmatrix




def save(cfg, hls_model, precision):
    import json
    hls_model.save(f"{path}/results/{dir}/{precision}/conifer_model.json")
    with open(f"{path}/results/{dir}/{precision}/conifer_conf.json", "w") as f:
        f.write(json.dumps(cfg, indent=4))


# %%

convert("cpp", 64, predict=False, build=False)
df_test, cfg, xgb_model, xgb_preds, hls_model, hls_preds, dmatrix = convert("cpp", 64, predict=True)
save(cfg, hls_model, dir)
bins = np.linspace(-1, 1, 100)

# %%

fig,ax=plt.subplots()
ax.hist(xgb_preds[df_test["TkEle_label"]==1], bins=bins, histtype="step", label="XGBoost-sig", density=True, linewidth=2)
ax.hist(xgb_preds[df_test["TkEle_label"]==0], bins=bins, histtype="step", label="XGBoost-bkg", density=True, linewidth=2)
ax.hist(hls_preds[df_test["TkEle_label"]==1], bins=bins, histtype="step", label="HLS-sig", density=True, linestyle="--", linewidth=2)
ax.hist(hls_preds[df_test["TkEle_label"]==0], bins=bins, histtype="step", label="HLS-bkg", density=True, linestyle="--", linewidth=2)
ax.set_xlabel("Score")
ax.set_ylabel("Density")
plt.yscale("log")
plt.legend()
hep.cms.text("Phase-2 Simulation Preliminary", fontsize=18, ax = ax)
hep.cms.lumitext("PU 200 (14 TeV)", fontsize=18, ax = ax)
fig.savefig(f"{path}/results/{dir}/plots/hls_vs_xgb.png")
fig.savefig(f"{path}/results/{dir}/plots/hls_vs_xgb.pdf")


# %%

# #!------------------------------------ Evaluate -----------------------------------!#
raw_func = lambda x: np.log(x / (1 - x)) / 8
df_train["score"] = raw_func(xgb_model.predict(dtrain))
df_test["score"] = raw_func(xgb_model.predict(dtest))

sig_test["score"] = df_test["score"][df_test["TkEle_label"] == 1]
sig_train["score"] = df_train["score"][df_train["TkEle_label"] == 1]
bkg_test["score"] = df_test["score"][df_test["TkEle_label"] == 0]
bkg_train["score"] = df_train["score"][df_train["TkEle_label"] == 0]


sig_train_best, sig_test_best = take_max_score(
    ["TkEle_ev_idx", "TkEle_GenEle_idx"], sig_train, sig_test
)
bkg_train_best, bkg_test_best = take_max_score(
    ["TkEle_ev_idx", "TkEle_CryClu_idx"], bkg_train, bkg_test
)

df_test_best = pd.concat([sig_test_best, bkg_test_best])
df_train_best = pd.concat([sig_train_best, bkg_train_best])


# %%

#!------------------------------------ Plot ROCs (only test) ----------------------------------!#
plot_roc(
    df_test,  # Use the DataFrame instead of dmatrix
    score="TkEle_hls_score",
    y="TkEle_label",
    save=f"{path}/results/{dir}/plots/roc_conifer",
)

#!------------------------------------ ROC per pt ----------------------------------!#

pt_bins = (0, 10, 20, 30, 50, 100)
thresholds = [0.0, 0.1, 0.2, 0.3, 0.4]

pt_bins = [0, 5, 10, 30, 40, 100]
thresholds = [0.15, 0.15, 0.32, 0.32, 0.1]

_, aucs = plot_roc_bins(
    df_test,
    score="TkEle_hls_score",
    label="$p_T$",
    units="GeV",
    y="TkEle_label",
    var_name="TkEle_CryClu_pt",
    xlim=(-0.025, 0.5),
    var_bins=pt_bins,
    thresholds=thresholds,
    save=f"{path}/results/{dir}/plots/roc_pt_bestTkEle_test_conifer",
)

plot_roc_bins(
    df_train,
    score="TkEle_xgb_score",
    label="$p_T$",
    units="GeV",
    y="TkEle_label",
    var_name="TkEle_CryClu_pt",
    xlim=(-0.025, 0.5),
    var_bins=pt_bins,
    thresholds=thresholds,
    save=f"{path}/results/{dir}/plots/roc_pt_bestTkEle_train_conifer",
)
# quant_aucs[f"{quant}"] = aucs
# quant_models[quant] = model
# quant_params[quant] = params
# scaler_quant[quant] = scaler


# with open(f"{path}/results/{dir}/parameters.json", "w") as f:
#     f.write(json.dumps(params, indent=4))

# with open(f"{path}/results/{dir}/report.txt", "w") as f:
#     f.write("--- Scaler ---\n")
#     f.write("\n inf + (x - min) >> bit_shift\n\n")
#     f.write(str(scaler))
#     f.write("\n\n--- Parameters ---\n")
#     f.write(str(params))


# %%