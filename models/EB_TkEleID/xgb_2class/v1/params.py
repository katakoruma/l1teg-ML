tag = "140Xv0C1"
P0 = f"/eos/user/l/lekerner/www/l1teg/Barrel/2/zsnap/era{tag}/reweight_1_full"
P0 = f"/eos/user/l/lekerner/www/l1teg/Endcap/PU200_train/zsnap/era{tag}/reweight_1_full"

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