# %%
import sys
sys.path.append("/afs/cern.ch/work/l/lekerner/code/l1teg-ML/models/EB_TkEleID/xgb_2class/v1/utils")
sys.path.append("/afs/cern.ch/work/l/lekerner/code/l1teg-ML/models/EB_TkEleID/xgb_2class/v1/")
sys.path.append("/afs/cern.ch/work/l/lekerner/code/l1teg-ML/utils/BitHub")

from data import (
    generate_paths,
    load_df,
    normalize_weight,
)

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.colors import LogNorm
import numpy as np
import mplhep as hep
from plot.features import profile, plot_input_features
from params_pu0 import features, auxiliary, samples, tag, P0

# %%å

#!------------------------------------- Load Dataframe -------------------------------------!#
paths = generate_paths(P0, tag, samples)
data = load_df(
    *paths, branches=features + auxiliary
)

# data = normalize_weight(
#     data, key="TkEle_weight", kind="entries"
# )

# %%
#!------------------------------------ Plot Pre-training -----------------------------------!#

delta_eta = data[0]['TkEle_Tk_eta'] - data[0]['TkEle_CryClu_eta']
delta_phi = data[0]['TkEle_Tk_phi'] - data[0]['TkEle_CryClu_phi']

delta_phi[delta_phi > np.pi] = 2 * np.pi - delta_phi[delta_phi > np.pi]



def plot_histogram(data, variable, bins, xlabel, label, linestyle='-', alpha=1, normalize=False):
    hep.set_style("CMS")
    
    for name, dataset in data.items():
        values = variable(dataset)
        weights = None
        if normalize:
            weights = np.ones_like(values) / len(values)
        
        plt.hist(
            values, bins=bins, alpha=alpha, 
            label=f'{label} ({name})', histtype='step', linestyle=linestyle, weights=weights, linewidth=2
        )
    
    plt.xlabel(xlabel)
    plt.ylabel('Events' if not normalize else 'Normalized Events')
    hep.cms.text("Preliminary", fontsize=18)
    hep.cms.lumitext("", fontsize=18)
    plt.legend()
    plt.show()

# Define lambda functions for delta_eta and delta_phi
delta_eta_func = lambda d: (d['TkEle_GenEle_caloeta'] - d['TkEle_Tk_caloEta'])
delta_phi_func = lambda d: (d['TkEle_GenEle_calophi'] - d['TkEle_Tk_caloPhi'])

# Adjust delta_phi for periodicity
for name, d in zip(['Double_Ele', 'MinBias'], data):
    delta_phi = delta_phi_func(d)
    delta_phi[delta_phi > np.pi] = 2 * np.pi - delta_phi[delta_phi > np.pi]
    d['delta_phi_adjusted'] = delta_phi

# Create a dictionary for named datasets
named_data = {'DoubleEle': data[0]}

# Plot histograms
normalize = False  # Set this to True for normalized plots, False otherwise
#plot_histogram(data[1], delta_eta_func, bins=20, xlabel='Delta Eta', label='Delta Eta', linestyle='-', normalize=normalize)
#plot_histogram(data[1], lambda d: d['delta_phi_adjusted'], bins=20, xlabel='Delta Phi', label='Delta Phi', linestyle='-', normalize=normalize)

#%%

def plot_2d_histogram(data, x_func, y_func, bins, xlabel, ylabel, normalize=False):
    hep.set_style("CMS")
    
    x_values = x_func(data)
    y_values = y_func(data)
    weights = None
    if normalize:
        weights = np.ones_like(x_values) / len(x_values)
    
    plt.hist2d(
        x_values, y_values, bins=bins, weights=weights, cmap='viridis', range=[[-0.4, 0.4], [-0.4, 0.4]], norm=LogNorm()
    )


    #Ellipse((0, 0), 0.4, 0.4, edgecolor='red', facecolor='none', linestyle='--')
    plt.gca().add_patch(Ellipse((0, 0), 0.3, 0.03, edgecolor='red', facecolor='none', linestyle='--'))
    plt.text(-0.2, 0.1, 'Delta Eta = 0.3, Delta Phi = 0.03', color='red', fontsize=15)

    plt.colorbar(label='Events' if not normalize else 'Normalized Events')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(-0.4, 0.4)
    plt.ylim(-0.4, 0.4)
    hep.cms.text("Preliminary", fontsize=18)
    hep.cms.lumitext("", fontsize=18)
    plt.title(f'{name}')
    plt.show()

# Plot 2D histogram for Delta Eta vs Delta Phi
plot_2d_histogram(
    data[0][:1000],
    delta_phi_func,
    delta_eta_func,
    bins=(120, 120),
    xlabel='Delta Phi',
    ylabel='Delta Eta',
    normalize=normalize
)
# %%
