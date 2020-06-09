#!/bin/bash

echo "!!!! WARNING: Submitting for MC!!!"
python submit_allHLT.py \
  runHLTBTagAnalyzer_cfg.py \
  -f CRAB/tosubmit_MC.txt \
  -s T3_US_FNALLPC \
  -p groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar" runOnData=False globalTag="110X_mcRun3_2021_realistic_v6" trackPtSeed=2.0 \
  -o /store/user/johnda/BTagNTuples/Run3/ \
  -v crab_projects_run3_trackPt2p0
