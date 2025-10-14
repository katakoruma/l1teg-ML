# %%
from utils.data import (
    generate_paths,
    load_df,
    normalize_weight,
    concatenate,
    df_to_DMatrix,
    take_max_score
)

from utils.plot.post_train import (
    plot_loss,
    plot_importance,
    plot_scores,
    plot_roc,
    plot_roc_bins,
    plot_quant_aucs,
)

from bithub.scalers import BitScaler

from bayes_opt import BayesianOptimization
import numpy as np
import xgboost as xgb

from params_pu200 import features, auxiliary, samples, tag, P0, saturate
import pandas as pd

# %%
#!------------------------------------- Load Dataframe -------------------------------------!#
paths = generate_paths(P0, tag, samples)
sig_train, sig_test, bkg_train, bkg_test = load_df(
    *paths, branches=features + auxiliary
)
sig_train, bkg_train = normalize_weight(
    sig_train, bkg_train, key="TkEle_weight", kind="entries"
)
# %%
#!------------------------------------  scaling -----------------------------------!#

df_train, df_test = concatenate(
    {"train": [sig_train, bkg_train], "test": [sig_test, bkg_test]}
)

# scaler = None

dtrain, dtest, dtest_cut = df_to_DMatrix(
    df_train,
    df_test,
    df_test[df_test["TkEle_CryClu_pt"] < df_train["TkEle_CryClu_pt"].max()],
    features=features,
    y="TkEle_label",
   #  bitscaler=scaler,
   # ap_fixed=q if q != "float" else None,
    weight="TkEle_weight",
    class_weights="balanced",
)

#%%

def train(
        dtrain,
        dtest,
        dtest_cut,
        max_depth=12,
        learning_rate=0.45,
        subsample=0.8,
        colsample_bytree=1.0,
        alpha=1500,
        lambd=1500,
        min_split_loss=5,
        min_child_weight=80,
        num_round=15,
    ):
    
    #global model, eval_result, dtrain, dtest_cut, params, _num_round
    params = {
        "tree_method": "hist",
        "max_depth": int(max_depth),
        "learning_rate": learning_rate,
        "lambda": lambd,
        "alpha": alpha,
        "colsample_bytree": colsample_bytree,
        "subsample": subsample,
        # "gamma":5,
        "min_split_loss": min_split_loss,
        "min_child_weight": min_child_weight,
        "objective": "binary:logistic",
        "eval_metric": "logloss",
    }

    global model, eval_result, _num_round

    num_round = 14
    _num_round = num_round
    evallist = [(dtrain, "train"), (dtest_cut, "eval")]
    eval_result = {}


    model = xgb.train(
        params,
        dtrain,
        num_round,
        evallist,
        evals_result=eval_result,
        early_stopping_rounds=2,
    )
    print(params)
    return -eval_result["eval"][params["eval_metric"]][-1]
# %%

fixed_params = {
    #"alpha": 115.86842537080673,
    "colsample_bytree": 1.,
    "lambd": 0.,
    "learning_rate": 0.55,
    "max_depth": 20,
    "min_child_weight": 600,
    "min_split_loss": 100.,
    "subsample": 1.,
}
train(dtrain=dtrain, dtest=dtest, dtest_cut=dtest_cut, **fixed_params)

# %%

#!------------------------------------ Evaluate -----------------------------------!#
raw_func = lambda x: np.log(x / (1 - x)) / 8
df_train["score"] = raw_func(model.predict(dtrain))
df_test["score"] = raw_func(model.predict(dtest))

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

plot_loss(eval_result, save=f"results/float/plots/loss")

plot_importance(model, save=f"results/float/plots/importance")
plot_scores(
    df_train,
    df_test[df_test["TkEle_CryClu_pt"] < df_train["TkEle_CryClu_pt"].max()],
    score="score",
    y="TkEle_label",
    save=f"results/float/plots/scores",
    bins=np.linspace(-1, 1, 30),
    log=True,
)

#!------------------------------------ Plot ROCs (only test) ----------------------------------!#
plot_roc(
    df_train,
    df_test[df_test["TkEle_CryClu_pt"] < df_train["TkEle_CryClu_pt"].max()],
    score="score",
    y="TkEle_label",
    save=f"results/float/plots/roc",
)

#!------------------------------------ ROC per pt ----------------------------------!#

pt_bins = (0, 5, 10, 20, 30, 50, 100)

_, aucs = plot_roc_bins(
    df_test_best,
    score="score",
    label="$p_T$",
    units="GeV",
    y="TkEle_label",
    var_name="TkEle_CryClu_pt",
    xlim=(-0.025, 0.5),
    var_bins=pt_bins,
    save=f"results/float/plots/roc_pt_bestTkEle_test",
)

plot_roc_bins(
    df_train_best,
    score="score",
    label="$p_T$",
    units="GeV",
    y="TkEle_label",
    var_name="TkEle_CryClu_pt",
    xlim=(-0.025, 0.5),
    var_bins=pt_bins,
    save=f"results/float/plots/roc_pt_bestTkEle_train",
)
# quant_aucs[f"{quant}"] = aucs
# quant_models[quant] = model
# quant_params[quant] = params
# scaler_quant[quant] = scaler