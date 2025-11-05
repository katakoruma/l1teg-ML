tag = "140Xv0C1"
path = f"/eos/user/l/lekerner/www/l1teg/Endcap/1"
P0 = f"{path}/zsnap/era{tag}/reweight_1_full"

dir = 'model_6'

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
    "Tk_pt",
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
     "CryClu_hwEmf",
    #"CryClu_hoe",
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
    "CryClu_hwEmf": (0, 1),
#    "CryClu_hoe": (0, 64),  # Default range added
}

features = [f"TkEle_{f}" for f in features]
auxiliary = [f"TkEle_{f}" for f in auxiliary]
saturate = {f"TkEle_{key}": saturate[key] for key in saturate}