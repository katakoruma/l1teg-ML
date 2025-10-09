# TO run only on samples that will be used for training (140Xv0B9)

DIR="/eos/user/l/lekerner/www/l1teg/Endcap/PU200_train"
#DIR="/eos/user/l/lekerner/l1teg/Endcap/PU200"
ERA="140Xv0C1"

#Save only the cluster pt histogram
if [[ "$*" != *"--no_pt_hist"* ]]; then
    echo "Saving cluster pt histogram"
#    run_analysis.py --cfg cfg/l1teg_cfg_endcap.py --mc data/samples_pu0.py  --flow flows/Endcap/TkEle/FlowBase.py  --plots plots/Endcap/TkEle/PlotTkEleFeatures.py:pt_only=True  -o $DIR --eras $ERA --noYields --noStack
#    run_analysis.py --cfg cfg/l1teg_cfg_endcap.py --mc data/samples.py  --flow flows/Endcap/TkEle/FlowBase.py  --plots plots/Endcap/TkEle/PlotTkEleFeatures.py:pt_only=True  -o $DIR --eras $ERA --noYields --noStack
#    run_analysis.py --cfg cfg/l1teg_cfg_endcap.py --mc data/TrainTest_samples.py  --flow flows/Endcap/TkEle/FlowBase.py  --plots plots/Endcap/TkEle/PlotTkEleFeatures.py:pt_only=True  -o $DIR --eras $ERA --noYields --noStack
fi

#Read the cluster pt histogram to reweight the TkEle features and save a snapshot
#run_analysis.py --cfg cfg/l1teg_cfg_endcap.py --mc data/samples_pu0.py  --flow flows/Endcap/TkEle/FlowPtReweight.py:pt_hist=\"$DIR/era$ERA/matching_1_full/TkEle_CryClu_pt.root,DoubleElectron_PU0,MinBias\"  --plots plots/Endcap/TkEle/PlotTkEleFeatures.py  -o $DIR --eras $ERA --snapshot --columnSel "TkEle_.*" --noStack
#run_analysis.py --cfg cfg/l1teg_cfg_endcap.py --mc data/samples.py  --flow flows/Endcap/TkEle/FlowPtReweight.py:pt_hist=\"$DIR/era$ERA/matching_1_full/TkEle_CryClu_pt.root,DoubleElectron_PU200,MinBias\"  --plots plots/Endcap/TkEle/PlotTkEleFeatures.py  -o $DIR --eras $ERA --snapshot --columnSel "TkEle_.*" --noStack
run_analysis.py --cfg cfg/l1teg_cfg_endcap.py --mc data/TrainTest_samples.py --flow flows/Endcap/TkEle/FlowPtReweight.py:pt_hist=\"$DIR/era$ERA/matching_1_full/TkEle_CryClu_pt.root,DoubleElectron_PU200_train,MinBias_train\"  --plots plots/Endcap/TkEle/PlotTkEleFeatures.py  -o $DIR --eras $ERA --snapshot --columnSel "TkEle_.*" --noStack