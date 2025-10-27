#Save only the cluster pt histogram
DIR="/eos/user/l/lekerner/www/l1teg/Endcap/1"
ERA="140Xv0C1"

if [[ "$*" != *"--no_baseline"* ]]; then
    echo "Running baseline"
#    run_analysis.py --cfg cfg/l1teg_cfg_endcap.py --mc data/samples.py   --flow flows/Endcap/Baseline/FlowBaseline.py   --plots plots/Endcap/Baseline/PlotEffRate.py  -o $DIR --eras $ERA --noStack
fi
run_analysis.py --cfg cfg/l1teg_cfg_endcap.py --mc data/TrainTest_samples.py  --flow flows/Endcap/TkEle/FlowBDT_test.py:bdt_path=\"/eos/user/l/lekerner/www/l1teg/Endcap/PU200_train/results/\"  --plots plots/Endcap/TkEle/PlotTkEleFeatures.py:score_only=True -o $DIR --eras $ERA --noStack --snapshot --columnSel "TkEle_score,TkEle_(GenEle|CryClu)_pt,TkEle_GenEle_eta,TkEle_(Tk|GenEle)_idx,weight"