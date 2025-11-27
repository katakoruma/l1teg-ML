import numpy as np
import os, shutil

tag = "140Xv0C1"
path = f"/eos/user/l/lekerner/www/l1teg/Endcap/1"
P0 = f"{path}/zsnap/era{tag}/reweight_1_full"

dir = 'model_hoe'

destination_dir = f"{path}/results/{dir}"
os.makedirs(destination_dir, exist_ok=True)
shutil.copy(__file__, os.path.join(destination_dir, "params_pu200.py"))

features = [
#    "CryClu_pt",
#    "CryClu_eta",
    # "CryClu_phi",
    "CryClu_EmIdProb",
    # "CryClu_PuIdProb",
    "CryClu_piIdProb",
    "CryClu_sigmarr",
    "CryClu_zbarycenter",
   # "CryClu_relIso",
#    "CryClu_caloIso",
#    "CryClu_standaloneWP",
#    "CryClu_looseL1TkMatchWP",
    "Tk_chi2RPhi",
    "Tk_chi2Bend",
    "Tk_chi2RZ",
#    "Tk_ptFrac",
    # "Tk_eta",
    # "Tk_phi",
    # "Tk_pt",
   # "Tk_caloPhi",
#    "Tk_caloEta",
   # "GenEle_calophi",
   # "GenEle_caloeta",
   # "GenEle_pt",
    "PtRatio",
    "nTkMatch",
    "absdeta",
    # "absdphi",
    # "CryClu_showerlength",
    # "CryClu_coreshowerlength",
 #   "CryClu_firstlayer",
 #   "CryClu_first1layers",
 #   "CryClu_first3layers",
    "CryClu_first5layers",
    # "CryClu_firstHcal1layers",
    # "CryClu_firstHcal3layers",
    # "CryClu_firstHcal5layers",
 #   "CryClu_last1layers",
 #   "CryClu_last3layers",
 #   "CryClu_last5layers",
 #     "CryClu_emf",
     "CryClu_hoe",
]

auxiliary = [   "GenEle_pt", 
                "GenEle_idx", 
                "label", 
                "weight",
                "sumTkPt", 
                "CryClu_idx",
                "CryClu_pt"
            ]

samples = [
    "DoubleElectron_PU200_train",
    "DoubleElectron_PU200_test",
    "MinBias_train",
    "MinBias_test",
]

saturate = {
#    "CryClu_pt": (0, 128),
    "CryClu_EmIdProb": (0, 2),
#    "CryClu_PuIdProb": (0, 2),
    "CryClu_piIdProb": (0, 2),
    "Tk_chi2RPhi": (0, 16),
    "Tk_chi2Bend": (0, 16),
    "Tk_chi2RZ": (0, 16),
    "CryClu_sigmarr": (0, 0.01),
    "CryClu_zbarycenter": (0, 512),
  #  "Tk_ptFrac": (0, 64),
#    "Tk_pt": (0, 128),
#    "CryClu_relIso": (0, 1),
#    "CryClu_caloIso": (0, 1),
#    "Tk_caloPhi": (0, 64),  # Default range added
#    "Tk_caloEta": (0, 64),  # Default range added
#    "GenEle_calophi": (0, 64),  # Default range added
#    "GenEle_caloeta": (0, 64),  # Default range added
#    "GenEle_pt": (0, 64),  # Default range added
    "PtRatio": (0, 32),
    "nTkMatch": (0, 16),
    "absdeta": (0, 8),
#    "absdphi": (0, 64),
#    "CryClu_showerlength": (0, 64),
#    "CryClu_coreshowerlength": (0, 64),
#    "CryClu_firstlayer": (0, 64),  # Default range added
#    "CryClu_first1layers": (0, 64),  # Default range added
#    "CryClu_first3layers": (0, 64),  # Default range added
    "CryClu_first5layers": (0, 1),  # Default range added
#    "CryClu_firstHcal1layers": (0, 64),  # Default range added
#    "CryClu_firstHcal3layers": (0, 64),  # Default range added
#    "CryClu_firstHcal5layers": (0, 64),  # Default range added
#    "CryClu_last1layers": (0, 64),  # Default range added
#    "CryClu_last3layers": (0, 64),  # Default range added
#    "CryClu_last5layers": (0, 64),  # Default range added
#     "CryClu_emf": (-1, 2),
    "CryClu_hoe": (-1, 3),  # Default range added
}

features = [f"TkEle_{f}" for f in features]
auxiliary = [f"TkEle_{f}" for f in auxiliary]
saturate = {f"TkEle_{key}": saturate[key] for key in saturate}



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
    "TkEle_CryClu_hoe": (r"Cluster H/E", np.linspace(-5,20,30)),
    "TkEle_CryClu_showerlength": (r"Cluster showerlength", np.linspace(0,30,30)),
    "TkEle_CryClu_coreshowerlength": (r"Cluster coreshowerlength", np.linspace(0,30,30)),
    "TkEle_CryClu_first5layers": (r"Cluster first5layers", np.linspace(0,1,30)),
    "TkEle_CryClu_firstHcal1layers": (r"Cluster firstHcal1layers", np.linspace(0,1,30)),
    "TkEle_CryClu_firstHcal3layers": (r"Cluster firstHcal3layers", np.linspace(0,1,30)),
    "TkEle_CryClu_firstHcal5layers": (r"Cluster firstHcal5layers", np.linspace(0,1,30)),
}


feat_info_normalized = {}
for key in feat_info:
    label, bins = feat_info[key]
    min_bin = bins[0]
    max_bin = bins[-1]
    feat_info_normalized[key] = (label, np.linspace(-1,1, len(bins)))