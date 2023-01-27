# MC production

## MC production for L1 and HLT studies

```
cmsrel CMSSW_12_4_10
cd CMSSW_12_4_10/src
cmsenv
git cms-init
git cms-addpkg Configuration/Generator # required for step0
git clone git@github.com:DiElectronX/GENfragments.git Configuration/GENfragments # required for step0
git cms-merge-topic bainbrid:EGHLTCustomisation_1230pre6 # required for step3
scram b -j8
voms-proxy-init --voms cms -valid 192:00
```

### step0: “GENSIM”

Performs GEN,SIM steps. (5000 toys will give 100 events based on GEN filter eff of 2%.)

```
cmsDriver.py Configuration/GENfragments/python/BuToKee_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec --python_filename step0_cfg.py -n 5000
cmsRun step0_cfg.py >& step0.log &
```

### step1: “PREMIXRAW”

Performs DIGI,DATAMIX,L1,DIGI2RAW,HLT steps.

```
cmsDriver.py step1 --mc --eventcontent PREMIXRAW --pileup_input dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX --datatier GEN-SIM-RAW --conditions 124X_mcRun3_2022_realistic_v12 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2022v12 --procModifiers premix_stage2 --nThreads 4 --geometry DB:Extended --datamix PreMix --era Run3 --filein file:step0.root --fileout file:step1.root --pileup_input dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX --customise Configuration/DataProcessing/Utils.addMonitoring --no_exec --python_filename step1_cfg.py -n -1
cmsRun step1_cfg.py >& step1.log &
```

### step2: "Extended MINIAOD”

Performs RAW2DIGI,L1Reco,RECO,RECOSIM,PAT steps.

```
cmsDriver.py step2 --mc --eventcontent MINIAODSIM --datatier MINIAODSIM --conditions 124X_mcRun3_2022_realistic_v12 --step RAW2DIGI,L1Reco,RECO,RECOSIM,PAT --nThreads 4 --geometry DB:Extended --era Run3 --filein file:step1.root --fileout file:step2.root --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuBParkStep2,Configuration/DataProcessing/Utils.addMonitoring --no_exec --python_filename step2_cfg.py -n -1
cmsRun step2_cfg.py >& step2.log &
```

### step3: "Extended MINIAOD + reHLT (open mode)"

```
hltGetConfiguration /users/sharper/2022/egamma/EgOpen1240FrozenV1p2 --globaltag 124X_mcRun3_2022_realistic_v12 --mc --unprescale --output minimal --max-events -1 --eras Run3 --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuBParkStep3,Configuration/DataProcessing/Utils.addMonitoring --input file:step2.root > step3_cfg.py
cmsRun step3_cfg.py >& step3.log &
```
