# %%
import sys
sys.path.append("/afs/cern.ch/work/l/lekerner/code/l1teg-ML/models/EB_TkEleID/xgb_2class/v1/")
sys.path.append("/afs/cern.ch/work/l/lekerner/code/l1teg-ML/utils/BitHub")
from utils.data import (
    generate_paths,
    load_df,
    normalize_weight,
)

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.colors import LogNorm
import numpy as np
import mplhep as hep
from utils.plot.features import profile, plot_input_features
from params_pu200 import features, auxiliary, samples, tag, P0

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


plt.hist(sig_train[sig_train['TkEle_CryClu_pt']<100]['TkEle_CryClu_pt'], bins=50, alpha=0.5, label='Signal (pre-training)')
plt.hist(bkg_train[bkg_train['TkEle_CryClu_pt']<100]['TkEle_CryClu_pt'], bins=50, alpha=0.5, label='Background (pre-training)')
plt.xlabel('TkEle_CryClu_pt')
plt.ylabel('Entries')
plt.legend()
plt.title('Pre-training Distribution of TkEle_CryClu_pt')
plt.yscale('log')
plt.show()
# %%
