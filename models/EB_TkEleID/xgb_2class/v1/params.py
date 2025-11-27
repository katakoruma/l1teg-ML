import numpy as np
import os, shutil

tag = "140Xv0C1"
path = f"/eos/user/l/lekerner/www/l1teg/Barrel/3"
P0 = f"{path}/zsnap/era{tag}/reweight_1_full"

dir = 'thesis'

destination_dir = f"{path}/results/{dir}"
os.makedirs(destination_dir, exist_ok=True)
shutil.copy(__file__, os.path.join(destination_dir, "params.py"))

features = [
    "CryClu_pt",
    "CryClu_showerShape",
    "CryClu_relIso",
    "CryClu_standaloneWP",
    "CryClu_looseL1TkMatchWP",
    "Tk_chi2RPhi",
    "Tk_ptFrac",
    "PtRatio",
    "nTkMatch",
    "absdeta",
    "absdphi",
]

auxiliary = ["GenEle_pt", "GenEle_idx", "label", "weight", "sumTkPt", "CryClu_idx", "CryClu_eta"]

samples = [
    "DoubleElectron_PU200_train",
    "DoubleElectron_PU200_test",
    "MinBias_train",
    "MinBias_test",
]

saturate = {"TkEle_PtRatio": (0, 32),
                  "TkEle_Tk_chi2RPhi": (0, 16),
                  "TkEle_Tk_ptFrac": (0, 64),
                  "TkEle_CryClu_relIso": (0, 1),
                  "TkEle_CryClu_pt": (0, 64),
                  "TkEle_CryClu_showerShape": (0, 1),
                  "TkEle_absdphi": (0, 64),
                  "TkEle_absdeta": (0, 8),
                  "TkEle_nTkMatch": (0, 16),
                  }

features = [f"TkEle_{f}" for f in features]
auxiliary = [f"TkEle_{f}" for f in auxiliary]


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
    "TkEle_CryClu_emf": (r"Cluster emf", np.linspace(-1,2,30)),
    "TkEle_CryClu_showerlength": (r"Cluster showerlength", np.linspace(0,30,30)),
    "TkEle_CryClu_coreshowerlength": (r"Cluster coreshowerlength", np.linspace(0,30,30)),
}


feat_info_normalized = {}
for key in feat_info:
    label, bins = feat_info[key]
    min_bin = bins[0]
    max_bin = bins[-1]
    feat_info_normalized[key] = (label, np.linspace(-1,1, len(bins)))