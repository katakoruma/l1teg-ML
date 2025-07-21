tag = "140Xv0B9"
P0 = f"/eos/home-l/lekerner/ngt/data/l1teg/zsnap/era{tag}/reweight_1_full"

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


features = [f"TkEle_{f}" for f in features]
auxiliary = [f"TkEle_{f}" for f in auxiliary]