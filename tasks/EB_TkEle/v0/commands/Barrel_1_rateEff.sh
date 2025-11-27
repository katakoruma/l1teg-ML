#Save only the cluster pt histogram
DIR="/eos/user/l/lekerner/www/l1teg/Barrel/3"
ERA="140Xv0B9"

if [[ "$*" != *"--no_baseline"* ]]; then
    echo "Running baseline"
    run_analysis.py --cfg cfg/l1teg_cfg.py --mc data/TrainTest_samples.py --flow flows/Barrel/Baseline/FlowBaseline.py   --plots plots/Barrel/Baseline/PlotEffRate.py  -o $DIR --eras $ERA --noStack  # --snapshot --columnSel "(TkEleLoose|TkEleTight)_genIdx"
fi

#run_analysis.py --cfg cfg/l1teg_cfg.py --mc data/TrainTest_samples.py  --flow flows/Barrel/TkEle/FlowBDT_test.py:bdt_path=\"/eos/user/l/lekerner/www/l1teg/Barrel/3/results/\"  --plots plots/Barrel/TkEle/PlotTkEleFeatures.py:score_only=True -o $DIR --eras $ERA --noStack --snapshot --columnSel "TkEle_score,TkEle_(GenEle|CryClu)_pt,TkEle_GenEle_eta,TkEle_(Tk|GenEle)_idx,weight"