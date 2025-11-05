tag = "140Xv0C1"
path = f"/eos/user/l/lekerner/www/l1teg/Endcap/1"
P0 = f"{path}/zsnap/era{tag}/reweight_1_full"

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
    "CryClu_sigmarr",
    "CryClu_zbarycenter",
    "CryClu_hoe",
    "Tk_chi2RPhi",
    "Tk_chi2Bend",
    "Tk_chi2RZ",
    "Tk_pt",
    "PtRatio",
    "nTkMatch",
    "absdeta",
    "absdphi",
]

auxiliary = [   "GenEle_pt", 
                "GenEle_idx", 
                "label", 
                "weight",
                "sumTkPt", 
                "CryClu_idx"
            ]

samples = [
    "DoubleElectron_PU200_train",
    "DoubleElectron_PU200_test",
    "MinBias_train",
    "MinBias_test",
]

saturate = {
    "CryClu_pt": (0, 100),
    "CryClu_sigmarr": (0, 0.01),
    "CryClu_zbarycenter": (0, 512),
    "CryClu_hoe": (0, 64),
    "Tk_chi2RPhi": (0, 16),
    "Tk_chi2Bend": (0, 16),
    "Tk_chi2RZ": (0, 16),
    "Tk_pt": (0, 128),
    "PtRatio": (0, 32),
    "nTkMatch": (0, 16),
    "absdeta": (0, 8),
    "absdphi": (0, 64),
}

features = [f"TkEle_{f}" for f in features]
auxiliary = [f"TkEle_{f}" for f in auxiliary]
saturate = {f"TkEle_{key}": saturate[key] for key in saturate}