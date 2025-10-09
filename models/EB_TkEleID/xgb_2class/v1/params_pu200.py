tag = "140Xv0C1"
P0 = f"/eos/user/l/lekerner/www/l1teg/Endcap/PU200_train/zsnap/era{tag}/reweight_1_full"

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
    # "CryClu_phi",
#    "CryClu_showerShape",
#    "CryClu_relIso",
#    "CryClu_standaloneWP",
#    "CryClu_looseL1TkMatchWP",
    "Tk_chi2RPhi",
    "Tk_ptFrac",
    # "Tk_eta",
    # "Tk_phi",
   # "Tk_caloPhi",
    "Tk_caloEta",
   # "GenEle_calophi",
   # "GenEle_caloeta",
   # "GenEle_pt",
    "PtRatio",
    "nTkMatch",
    "absdeta",
    "absdphi",
    "CryClu_firstlayer",
    "CryClu_first1layers",
    "CryClu_first3layers",
    "CryClu_first5layers",
    "CryClu_emf",
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
    "CryClu_pt": (0, 64),
    "Tk_chi2RPhi": (0, 16),
    "Tk_ptFrac": (0, 64),
    "Tk_caloPhi": (0, 64),  # Default range added
    "Tk_caloEta": (0, 64),  # Default range added
    "GenEle_calophi": (0, 64),  # Default range added
    "GenEle_caloeta": (0, 64),  # Default range added
    "GenEle_pt": (0, 64),  # Default range added
    "PtRatio": (0, 32),
    "nTkMatch": (0, 16),
    "absdeta": (0, 8),
    "absdphi": (0, 64),
    "CryClu_firstlayer": (0, 64),  # Default range added
    "CryClu_first1layers": (0, 64),  # Default range added
    "CryClu_first3layers": (0, 64),  # Default range added
    "CryClu_first5layers": (0, 64),  # Default range added
    "CryClu_hoe": (0, 64),  # Default range added
}

features = [f"TkEle_{f}" for f in features]
auxiliary = [f"TkEle_{f}" for f in auxiliary]
saturate = {f"TkEle_{key}": saturate[key] for key in saturate}