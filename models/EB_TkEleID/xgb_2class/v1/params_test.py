tag = "140Xv0C1"
P0 = f"/eos/user/l/lekerner/www/l1teg/Endcap/3/zsnap/era140Xv0C1/reweight_1_full"

features = [
    "TkEleL2_pt",
    "TkEleL2_phi",
    "TkEleL2_eta",
    "DecEmCaloHGCal_pt",
    "DecEmCaloHGCal_phi",
    "DecEmCaloHGCal_eta"
    
]

features = [
    "CryClu_pt",
    "CryClu_eta",
    "CryClu_phi",
    "CryClu_showerShape",
    "CryClu_relIso",
    "CryClu_standaloneWP",
    "CryClu_looseL1TkMatchWP",
    "Tk_chi2RPhi",
    "Tk_ptFrac",
    "Tk_eta",
    "Tk_phi",
    "Tk_caloPhi",
    "Tk_caloEta",
    "GenEle_calophi",
    "GenEle_caloeta",
    "GenEle_pt",
    "PtRatio",
    "nTkMatch",
    "absdeta",
    "absdphi",
    "absdphi"
]

auxiliary = ["GenEle_pt", "GenEle_idx", "label", "weight", "sumTkPt", "CryClu_idx"]

samples = [
    "DoubleElectron_PU200",
    "MinBias",
]


features = [f"TkEle_{f}" for f in features]
auxiliary = [f"TkEle_{f}" for f in auxiliary]