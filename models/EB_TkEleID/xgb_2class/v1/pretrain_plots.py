# %%
from utils.data import (
    generate_paths,
    load_df,
    normalize_weight,
)
from utils.plot.features import profile, plot_input_features
from params_pu200 import features, auxiliary, samples, tag, P0, path, dir
import pandas as pd
import numpy as np


feat_info = {
    "TkEle_CryClu_pt": (r"$p_T^{\text{Cluster}}$ [GeV]", np.linspace(0,100,20)),
    "TkEle_CryClu_showerShape": (r"$E^{\text{Cluster}}_{2\times5}/E^{\text{Cluster}}_{5\times5}$", np.linspace(0,0.1,30)),
    "TkEle_CryClu_relIso": (r"Cluster Iso./$p^{\text{Cluster}}_T$", np.linspace(0,1.5,20)),
    "TkEle_CryClu_standaloneWP": (r"Cluster StandaloneWP", np.linspace(0,2,3)),
    "TkEle_CryClu_looseL1TkMatchWP": (r"Cluster LooseL1TkMatchWP", np.linspace(0,2,3)),
    "TkEle_CryClu_sigmarr": (r"Cluster $\sigma_{rr}$", np.linspace(0,0.05,30)),
    "TkEle_Tk_chi2RPhi": (r"Tk $\chi^2_{\text{R-}\phi}$", np.linspace(0,16,17)),
    "TkEle_Tk_ptFrac": (r"$p_T^{\text{Tk}}/\sum p_T^{\text{Matched Tk}}$", np.linspace(0,64,30)),
    "TkEle_Tk_pt": (r"$p_T^{\text{Tk}}$ [GeV]", np.linspace(0,128,20)),
    "TkEle_Tk_chi2RZ": (r"Tk $\chi^2_{\text{R-Z}}$", np.linspace(0,16,17)),
    "TkEle_Tk_chi2Bend": (r"Tk $\chi^2_{\text{Bend}}$", np.linspace(0,16,17)),
    "TkEle_Tk_chi2RPhi": (r"Tk $\chi^2_{\text{R-}\phi}$", np.linspace(0,16,17)),
    "TkEle_CryClu_zbarycenter": (r"Cluster z barycenter", np.linspace(0,512,512)),
    "TkEle_absdeta": (r"$|\Delta \eta|$ (Tk-Cluster)", np.linspace(0,8,9)),
    "TkEle_absdphi": (r"$|\Delta \phi|$ (Tk-Cluster)", np.linspace(0,65,25)),
    "TkEle_nTkMatch": (r"$N_{\text{Matched Tracks}}$", np.linspace(0,16,17)),
    "TkEle_PtRatio": (r"$p_T^{\text{Tk}}/p_T^{\text{Cluster}}$", np.linspace(0,32,20)),
    "TkEle_CryClu_EmIdProb": (r"Cluster EmIdProb", np.linspace(0,1,30)),
    "TkEle_CryClu_PuIdProb": (r"Cluster PuIdProb", np.linspace(0,1,30)),
    "TkEle_CryClu_piIdProb": (r"Cluster piIdProb", np.linspace(0,1,30)),
    "TkEle_Tk_chi2Bend": (r"Tk $\chi^2_{\text{Bend}}$", np.linspace(0,16,17)),
    "TkEle_Tk_chi2RZ": (r"Tk $\chi^2_{\text{R-Z}}$", np.linspace(0,16,17)),
    "TkEle_CryClu_caloIso": (r"Cluster CaloIso", np.linspace(0,1,30)),
    "TkEle_CryClu_emf": (r"Cluster emf", np.linspace(0,1,30)),
    "TkEle_CryClu_hoe": (r"Cluster H/E", np.linspace(0,3,30)),
    "TkEle_CryClu_showerlength": (r"Cluster showerlength", np.linspace(0,30,30)),
    "TkEle_CryClu_coreshowerlength": (r"Cluster coreshowerlength", np.linspace(0,30,30)),
    "TkEle_CryClu_first5layers": (r"Cluster first5layers", np.linspace(0,1,30)),
    "TkEle_CryClu_firstHcal1layers": (r"Cluster firstHcal1layers", np.linspace(0,1,30)),
    "TkEle_CryClu_firstHcal3layers": (r"Cluster firstHcal3layers", np.linspace(0,1,30)),
    "TkEle_CryClu_firstHcal5layers": (r"Cluster firstHcal5layers", np.linspace(0,1,30)),
}

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
#!------------------------------------ Plot Pre-training -----------------------------------!#

#profile(sig_train, bkg_train, features=features, save="results/profile_{name}")
plot_input_features(
    sig_train,
    bkg_train,
    feat_info=feat_info,
    weight="TkEle_weight",
    features=features,
    save=f"{path}/results/{dir}/input_features_reweight",
)
plot_input_features(
    sig_test,
    bkg_test,
    feat_info=feat_info,
    weight="TkEle_weight",
    features=features,
    save=f"{path}/results/{dir}/input_features",
)

# %%
