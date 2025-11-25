from collections import OrderedDict
import cmgrdf_cli.defaults

# Priority: global_defaults < histo1d_defaults < branch_defaults < user defined
cmgrdf_cli.defaults.global_defaults = OrderedDict(density=False)

cmgrdf_cli.defaults.histo1d_defaults = OrderedDict(
    includeOverflows=False,
    includeUnderflows=False,
)

cmgrdf_cli.defaults.histo2d_defaults = OrderedDict()

cmgrdf_cli.defaults.histo3d_defaults = OrderedDict()

# The first matched pattern will be used
cmgrdf_cli.defaults.name_defaults = OrderedDict({
    "(.*)_EmIdProb(.*)": dict(
        bins=(2, 0, 2),
        label="EmIdProb",
        log="counts",
    ),
    "(.*)_PuIdProb(.*)": dict(
        bins=(2, 0, 2),
        label="PuIdProb$",
        log="counts",
    ),
    "(.*)_ptFrac(.*)": dict(
        bins=(64, 0, 64),
        label="($1) $p_{T}/\sum p_{T}$",
        log="counts",
    ),
    "(.*)_sumTkPt(.*)": dict(
        bins=(40, 0, 120),
        label="($1) ($2) $p_{T}$ [GeV]",
        log="counts",
    ),
    "(.*)_pt(.*)": dict(
        bins=(120, 0, 120),
        label="($1) ($2) $p_{T}$ [GeV]",
        log="counts",
    ),
    "(.*)_PtRatio(.*)": dict(
        bins=(64, 0, 32),
        label="($1) $p_{T}^{\\text{Clu}}/p_{T}^{\\text{Tk}}$ [GeV]",
        log="counts",
    ),
    "(.*)_idScore(.*)": dict(
        bins=(100, -1, 1),
        label="($1) ($2) Score",
        log="counts",
    ),
    "(.*)_score(.*)": dict(
        bins=(50, -1, 1),
        label="($1) ($2) Score",
        log="counts",
    ),
    "(.*)_(|calo)(:?eta|Eta)(:?.*)": dict(
        bins=(25, -3, 3),
        label="($1) ($2) $\eta$",
    ),
    "(.*)_(|calo)(:?phi|Phi)(:?.*)": dict(
        bins=(25, -3.14, 3.14),
        label="($1) ($2) $\phi$",
    ),
    "(.*)_deta(.*)": dict(
        bins=(25, -0.4, 0.4),
        label="($1) ($2) $\Delta \eta$",
    ),
    "(.*)_absdeta(.*)": dict(
        bins=(25, 0, 0.04*720/3.14),
        label="($1) ($2) $|\Delta \eta|$",
    ),
    "(.*)_dphi(.*)": dict(
        bins=(25, -0.4, 0.4),
        label="($1) ($2) $\Delta \phi$",
    ),
    "(.*)_absdphi(.*)": dict(
        bins=(25, 0, 0.4*720/3.14),
        label="($1) ($2) $|\Delta \phi|$",
    ),
    "(.*)_dR(.*)": dict(
        bins=(25, 0, 1),
        label="($1) ($2) $\Delta$R",
    ),
    "(.*)_caloIso(.*)": dict(
        bins=(25, 0, 40),
        label="($1) ($2) isolation",
        log="counts",
    ),
    "(.*)_idx(.*)": dict(
        bins=(101, -1, 100),
        label="($1) index",
        log="counts",
    ),
    "(.*)_chi2RPhi(.*)": dict(
        bins=(16, 0, 16),
        label="($1) $\chi^2_{\\text{RPhi}}$",
        log="counts",
    ),
    "(.*)_chi2(.*)": dict(
        bins=(30, 0, 30),
        label="($1) $\chi^2_{\\text{($2)}}$",
        log="counts",
    ),
    "(.*)_showerShape(.*)": dict(
        bins=(20, 0, 1.2),
        label="($1) $E_{2 \\times 5} / E_{5 \\times 5}$",
        log="counts",
    ),
    "(.*)_relIso(.*)": dict(
        bins=(32, 0, 16),
        label="($1) iso./$p_{T}$",
        log="counts",
    ),
    "(.*)_(standaloneWP|looseL1TkMatchWP|label)(.*)": dict(
        bins=(2, 0, 2),
        label="($1) ($2)",
    ),
    "(?:^n|.*_n)(.*)": dict(
        bins=(15, 0, 15),
        label="# ($1)",
        log="counts",
    ),
    "(.*)_weight(.*)": dict(
        bins=(100, 0, 2),
        label="($1) ($2) weight",
        log="counts",
    ),
    "(.*)_firstlayer(.*)": dict(
        bins=(20, 0, 100),
        label="($1) ($2) First Layer",
        log="counts",
    ),
    "(.*)_first1layers(.*)": dict(
        bins=(30, 0, 1),
        label="($1) ($2) First 1 Layers",
        log="counts",
    ),
    "(.*)_first3layers(.*)": dict(
        bins=(30, 0, 1),
        label="($1) ($2) First 3 Layers",
        log="counts",
    ),
    "(.*)_first5layers(.*)": dict(
        bins=(30, 0, 1),
        label="($1) ($2) First 5 Layers",
        log="counts",
    ),
    "(.*)_firstHcal1layers(.*)": dict(
        bins=(30, 0, 1),
        label="($1) ($2) First 1 Layers",
        log="counts",
    ),
    "(.*)_firstHcal3layers(.*)": dict(
        bins=(30, 0, 1),
        label="($1) ($2) First 3 Layers",
        log="counts",
    ),
    "(.*)_firstHcal5layers(.*)": dict(
        bins=(30, 0, 1),
        label="($1) ($2) First 5 Layers",
        log="counts",
    ),
    "(.*)_last1layers(.*)": dict(
        bins=(30, 0, 1),
        label="($1) ($2) Last 1 Layers",
        log="counts",
    ),
    "(.*)_last3layers(.*)": dict(
        bins=(30, 0, 1),
        label="($1) ($2) Last 3 Layers",
        log="counts",
    ),
    "(.*)_last5layers(.*)": dict(
        bins=(30, 0, 1),
        label="($1) ($2) Last 5 Layers",
        log="counts",
    ),
    "(.*)_hbm(.*)": dict(
        bins=(50, 0, 1),
        label="($1) ($2) HBM",
        log="counts",
    ),
    "(.*)_hoe(.*)": dict(
        bins=(50, 0, 3),
        label="($1) ($2) H/E",
        log="counts",
    ),
    "(.*)_emf(.*)": dict(
        bins=(50, 0, 1),
        label="($1) ($2) EMF",
        log="counts",
    ),
})
