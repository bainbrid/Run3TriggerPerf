import awkward as ak
import numpy as np
import time
import uproot as uproot

import numpy as np
np.seterr(divide='ignore', invalid='ignore')

# Environment: conda activate py37

# Time it
starttime = time.time()

dct = {
    "2022Sep05":{
        # Separate eras
        "2022Sep05_Run2022C_Jpsi":["2022Sep05_Run2022C"],
        "2022Sep09_Run2022Dv1_Jpsi":["2022Sep09_Run2022Dv1"],
        "2022Sep05_Run2022Dv2_Jpsi":["2022Sep05_Run2022Dv2"],
        # Total (B+C+D)
        "2022Sep05_Run2022_LowQ2":["2022Sep05_Run2022C","2022Sep09_Run2022Dv1","2022Sep05_Run2022Dv2"],
        "2022Sep05_Run2022_Jpsi":["2022Sep05_Run2022C","2022Sep09_Run2022Dv1","2022Sep05_Run2022Dv2"],
        "2022Sep05_Run2022_Psi2S":["2022Sep05_Run2022C","2022Sep09_Run2022Dv1","2022Sep05_Run2022Dv2"],
        # MC
        "2022Sep05_BuToKJpsi_Toee":["2022Sep05_BuToKJpsi_Toee"],
        "2022Sep05_BuToKPsi2S_Toee":["2022Sep05_BuToKPsi2S_Toee"],
        "2022Sep05_BuToKee":["2022Sep05_BuToKee"],
    },
    "2022Oct12":{
        "2022Oct12_BuToKJpsi_Toee":["2022Oct12_BuToKJpsi_Toee"],
        "2022Oct12_BuToKPsi2S_Toee":["2022Oct12_BuToKPsi2S_Toee"],
        "2022Oct12_BuToKee":["2022Oct12_BuToKee"],
        "2022Oct12_Run2022_Jpsi":["2022Oct12_Run2022C","2022Oct12_Run2022Dv1","2022Oct12_Run2022Dv2"],
        "2022Oct12_Run2022_Psi2S":["2022Oct12_Run2022C","2022Oct12_Run2022Dv1","2022Oct12_Run2022Dv2"],
        "2022Oct12_Run2022_LowQ2":["2022Oct12_Run2022C","2022Oct12_Run2022Dv1","2022Oct12_Run2022Dv2"],
    }
}

tag=["2022Sep05","2022Oct12"][1]
entries=50000
bmass_values=[]
bmass_nvalues=0
initial=0

# Interesting variables
branches_used = ['theRun','theEvent', # 'theLumi'
                 'isBToKEE','inAcc','isMatched',
                 'e1_gen_pt','e2_gen_pt','e1_gen_eta','e2_gen_eta','e12_gen_dr',
                 'e1_reco_pt','e2_reco_pt','e1_reco_eta','e2_reco_eta','e12_reco_dr',
                 'e1_reco_loose','e2_reco_loose','e1_reco_medium','e2_reco_medium','e1_reco_tight','e2_reco_tight',
                 'ip3d','cos2d','bdt','mll','b_mass','b_mass_err',
                 'b_pt','b_l1_pt','b_l2_pt','b_k_pt','b_cos2D','b_lxy','b_lxyerr','b_svprob'
                 ]
# JSON files
branches_used.extend([
    'JSON_TOTAL',
    'JSON_L1_11p0_HLT_6p5_final','JSON_L1_10p5_HLT_6p5_final','JSON_L1_10p5_HLT_5p0_final',
    'JSON_L1_8p5_HLT_5p0_final','JSON_L1_8p0_HLT_5p0_final','JSON_L1_7p0_HLT_5p0_final',
    'JSON_L1_6p5_HLT_4p5_final','JSON_L1_6p0_HLT_4p0_final','JSON_L1_5p5_HLT_6p0_final',
    'JSON_L1_5p5_HLT_4p0_final',
    ])

# HLT paths
branches_used.extend([
    'HLT_DoubleEle10p0','HLT_DoubleEle9p5','HLT_DoubleEle9p0','HLT_DoubleEle8p5','HLT_DoubleEle8p0',
    'HLT_DoubleEle7p5','HLT_DoubleEle7p0','HLT_DoubleEle6p5','HLT_DoubleEle6p0','HLT_DoubleEle5p5',
    'HLT_DoubleEle5p0','HLT_DoubleEle4p5','HLT_DoubleEle4p0',
    ])

# L1 seeds
branches_used.extend([
    'L1_DoubleEG11p0','L1_DoubleEG10p5','L1_DoubleEG10p0','L1_DoubleEG9p5','L1_DoubleEG9p0',
    'L1_DoubleEG8p5','L1_DoubleEG8p0','L1_DoubleEG7p5','L1_DoubleEG7p0','L1_DoubleEG6p5',
    'L1_DoubleEG6p0','L1_DoubleEG5p5','L1_DoubleEG5p0','L1_DoubleEG4p5','L1_DoubleEG4p0',
    ])
print("branches_used:",branches_used)

for dataset,samples in dct[tag].items() :

    isData = "Run2022" in dataset
    region = "LowQ2" if ( (    "BuToKee" in dataset ) or ( "LowQ2" in dataset ) ) \
      else    "Jpsi" if ( (  "BuToKJpsi" in dataset ) or (  "Jpsi" in dataset ) ) \
      else   "Psi2S" if ( ( "BuToKPsi2S" in dataset ) or ( "Psi2S" in dataset ) ) \
      else "Unknown" # error
    print("Region:",region)
    if region=="Unknown": print("Exitting..."); exit()

    name_output = "./slimmed/"+tag+"/slimmed_"+dataset+".root"
    file_output = uproot.recreate(name_output)
    file_output.mktree("tree",{
        "b_mass": ("float",(1,)),
        "b_mass_reduced": ("float",(1,)),
        "mll": ("float",(1,)),
        "trigger_OR": ("int",(1,)),
        "L1_11p0_HLT_6p5": ("int",(1,)),
        "L1_10p5_HLT_6p5": ("int",(1,)),
        "L1_10p5_HLT_5p0": ("int",(1,)),
        "L1_8p5_HLT_5p0": ("int",(1,)),
        "L1_8p0_HLT_5p0": ("int",(1,)),
        "L1_7p0_HLT_5p0": ("int",(1,)),
        "L1_6p5_HLT_4p5": ("int",(1,)),
        "L1_6p0_HLT_4p0": ("int",(1,)),
        "L1_5p5_HLT_6p0": ("int",(1,)),
        "L1_5p5_HLT_4p0": ("int",(1,)),
        })

    print("Dataset:",dataset)
    print("Output:",name_output)
    
    for sample in samples :

        name_input = "./ntuples/"+tag+"/ntuple_"+sample+".root:tree"
        with uproot.open(name_input,
                         file_handler=uproot.MultithreadedFileSource,
                         num_workers=100) as file_input:
        
            print(" Input:",name_input)
            # print(" Available branches",file_input.keys())
            # print(" Branches used",branches_used)
            ibatch=0

            for batch in file_input.iterate(step_size="10 mb",
                                            library="ak",
                                            filter_name=branches_used):

                ##########
                # INIT
                ##########

                #if ibatch >= 1 : continue
                print("  ibatch:",ibatch)
                ibatch+=1

                # Calc Lxy significance
                batch['b_lxysig'] = batch['b_lxy']/batch['b_lxyerr']

                # Reduced B mass
                batch['b_mass_reduced'] = batch['b_mass'] - batch['mll'] + 3.0969

                mll_cut = (batch['mll']>1.05) & (batch['mll']<2.45) if region == "LowQ2" \
                  else (batch['mll']>2.9) & (batch['mll']<3.2) if region == "Jpsi" \
                  else (batch['mll']>3.55) & (batch['mll']<3.8) if region == "Psi2S" \
                  else None

                ##########
                # CUT SETS
                ##########

                cuts_riccardo = (
                    (batch['inAcc']==1) & (batch['isMatched']==1) # GEN
                    #& (batch['HLT_DoubleEle6p5']==1) # Trigger
                    & (batch['e1_reco_loose']==1) & (batch['e2_reco_loose']==1) # ele ID
                    & (batch['e1_reco_pt']<100.) & (batch['e2_reco_pt']<100.) # ele "ID"
                    & (np.abs(batch['e1_reco_eta'])<1.4) & (np.abs(batch['e2_reco_eta'])<1.4) # ele eta
                    & (batch['e1_reco_pt']>4.) & (batch['e2_reco_pt']>4.) # ele pT
                    & mll_cut # mll region
                    & (batch['b_k_pt']>0.5) # kaon pT
                    & (batch['b_cos2D']>0.999) # cut-based
                    & (batch['b_svprob']>0.1) # cut-based
                    #& (batch['b_pt']>15.) # cut-based
                    & (batch['b_lxysig']>10.) # cut-based
                    #& (batch['bdt']>8.) # BDT-based
                    & (batch['b_mass']>4.7) & (batch['b_mass']<5.7) # B mass window
                    )

                cuts_riccardo_lowq2 = (
                    (batch['inAcc']==1) & (batch['isMatched']==1) # GEN
                    & (batch['HLT_DoubleEle6p5']==1) # Trigger
                    & (batch['e1_reco_loose']==1) & (batch['e2_reco_loose']==1) # ele ID
                    & (batch['e1_reco_pt']<100.) & (batch['e2_reco_pt']<100.) # ele "ID"
                    & (np.abs(batch['e1_reco_eta'])<1.2) & (np.abs(batch['e2_reco_eta'])<1.2) # ele eta
                    & (batch['e1_reco_pt']>5.) & (batch['e2_reco_pt']>5.) # ele pT
                    & mll_cut # mll region
                    & (batch['b_k_pt']>5.) # kaon pT
                    & (batch['b_cos2D']>0.99) # cut-based
                    & (batch['b_svprob']>0.01) # cut-based
                    & (batch['b_pt']>15.) # cut-based
                    & (batch['b_lxysig']>10.) # cut-based
                    #& (batch['bdt']>8.) # BDT-based
                    & (batch['b_mass']>4.7) & (batch['b_mass']<5.7) # B mass window
                    )

                # USED FOR PJSI IN PRESENTATION TO BPH
                cuts_rob = (
                    (batch['inAcc']==1) & (batch['isMatched']==1) # GEN
                    & (batch['HLT_DoubleEle6p5']==1) # Trigger
                    & (batch['e1_reco_loose']==1) & (batch['e2_reco_loose']==1) # ele ID
                    & (batch['e1_reco_pt']<100.) & (batch['e2_reco_pt']<100.) # ele "ID"
                    & (np.abs(batch['e1_reco_eta'])<1.2) & (np.abs(batch['e2_reco_eta'])<1.2) # ele eta
                    & (batch['e1_reco_pt']>5.) & (batch['e2_reco_pt']>5.) # ele pT
                    & mll_cut # mll region
                    & (batch['b_k_pt']>1.0) # kaon pT ???
                    & (batch['b_cos2D']>0.8) # cut-based ???
                    & (batch['b_svprob']>0.01) # cut-based
                    & (batch['b_pt']>15.) # cut-based
                    #& (batch['b_lxysig']>0.5) # cut-based ???
                    & (batch['bdt']>8.) # BDT-based
                    & (batch['b_mass']>4.7) & (batch['b_mass']<5.7) # B mass window
                    )

                # USED FOR LOWQ2 IN PRESENTATION TO BPH
                # USED FOR PSI2S (W/OUT BDT!) IN PRESENTATION TO BPH
                cuts_tight = (
                    (batch['inAcc']==1) & (batch['isMatched']==1) # GEN
                    & (batch['HLT_DoubleEle6p5']==1) # Trigger
                    & (batch['e1_reco_loose']==1) & (batch['e2_reco_loose']==1) # ele ID
                    & (batch['e1_reco_pt']<100.) & (batch['e2_reco_pt']<100.) # ele "ID"
                    & (np.abs(batch['e1_reco_eta'])<1.2) & (np.abs(batch['e2_reco_eta'])<1.2) # ele eta
                    & (batch['e1_reco_pt']>5.) & (batch['e2_reco_pt']>5.) # ele pT
                    & mll_cut # mll region
                    & (batch['b_k_pt']>0.5) # kaon pT ???
                    & (batch['b_cos2D']>0.99) # cut-based ???
                    & (batch['b_svprob']>0.01) # cut-based
                    & (batch['b_pt']>15.) # cut-based
                    & (batch['b_lxysig']>1.) # cut-based ???
                    & (batch['bdt']>8.) # BDT-based (was removed for Psi2S...!!!)
                    & (batch['b_mass']>4.7) & (batch['b_mass']<5.7) # B mass window
                    )

                ##########
                # CHOOSE CUTS
                ##########
                
                cuts = cuts_tight

                ##########
                # TRIGGERS
                ##########
                
                cuts_L1_11p0_HLT_6p5 = (batch['L1_DoubleEG11p0',cuts]==1) & (batch['HLT_DoubleEle6p5',cuts]==1)
                cuts_L1_10p5_HLT_6p5 = (batch['L1_DoubleEG10p5',cuts]==1) & (batch['HLT_DoubleEle6p5',cuts]==1)
                cuts_L1_10p5_HLT_5p0 = (batch['L1_DoubleEG10p5',cuts]==1) & (batch['HLT_DoubleEle5p0',cuts]==1)
                cuts_L1_8p5_HLT_5p0  = (batch['L1_DoubleEG8p5',cuts]==1)  & (batch['HLT_DoubleEle5p0',cuts]==1)
                cuts_L1_8p0_HLT_5p0  = (batch['L1_DoubleEG8p0',cuts]==1)  & (batch['HLT_DoubleEle5p0',cuts]==1)
                cuts_L1_7p0_HLT_5p0  = (batch['L1_DoubleEG7p0',cuts]==1)  & (batch['HLT_DoubleEle5p0',cuts]==1)
                cuts_L1_6p5_HLT_4p5  = (batch['L1_DoubleEG6p5',cuts]==1)  & (batch['HLT_DoubleEle4p5',cuts]==1)
                cuts_L1_6p0_HLT_4p0  = (batch['L1_DoubleEG6p0',cuts]==1)  & (batch['HLT_DoubleEle4p0',cuts]==1)
                cuts_L1_5p5_HLT_6p0  = (batch['L1_DoubleEG5p5',cuts]==1)  & (batch['HLT_DoubleEle6p0',cuts]==1)
                cuts_L1_5p5_HLT_4p0  = (batch['L1_DoubleEG5p5',cuts]==1)  & (batch['HLT_DoubleEle4p0',cuts]==1)

                if isData:
                    cuts_L1_11p0_HLT_6p5 = cuts_L1_11p0_HLT_6p5 & (batch['JSON_L1_11p0_HLT_6p5_final',cuts]==1)
                    cuts_L1_10p5_HLT_6p5 = cuts_L1_10p5_HLT_6p5 & (batch['JSON_L1_10p5_HLT_6p5_final',cuts]==1)
                    cuts_L1_10p5_HLT_5p0 = cuts_L1_10p5_HLT_5p0 & (batch['JSON_L1_10p5_HLT_5p0_final',cuts]==1)
                    cuts_L1_8p5_HLT_5p0  = cuts_L1_8p5_HLT_5p0  & (batch['JSON_L1_8p5_HLT_5p0_final',cuts]==1)
                    cuts_L1_8p0_HLT_5p0  = cuts_L1_8p0_HLT_5p0  & (batch['JSON_L1_8p0_HLT_5p0_final',cuts]==1)
                    cuts_L1_7p0_HLT_5p0  = cuts_L1_7p0_HLT_5p0  & (batch['JSON_L1_7p0_HLT_5p0_final',cuts]==1)
                    cuts_L1_6p5_HLT_4p5  = cuts_L1_6p5_HLT_4p5  & (batch['JSON_L1_6p5_HLT_4p5_final',cuts]==1)
                    cuts_L1_6p0_HLT_4p0  = cuts_L1_6p0_HLT_4p0  & (batch['JSON_L1_6p0_HLT_4p0_final',cuts]==1)
                    cuts_L1_5p5_HLT_6p0  = cuts_L1_5p5_HLT_6p0  & (batch['JSON_L1_5p5_HLT_6p0_final',cuts]==1)
                    cuts_L1_5p5_HLT_4p0  = cuts_L1_5p5_HLT_4p0  & (batch['JSON_L1_5p5_HLT_4p0_final',cuts]==1)

                cuts_trigger_OR = (
                    cuts_L1_11p0_HLT_6p5 | cuts_L1_10p5_HLT_6p5 | cuts_L1_10p5_HLT_5p0 | cuts_L1_8p5_HLT_5p0 |
                    cuts_L1_8p0_HLT_5p0 | cuts_L1_7p0_HLT_5p0 | cuts_L1_6p5_HLT_4p5 | cuts_L1_6p0_HLT_4p0 |
                    cuts_L1_5p5_HLT_6p0 | cuts_L1_5p5_HLT_4p0
                )
                    
                ##########
                # FOLD CUTS AND TRIGGER OR
                ##########

                #cuts = cuts & cuts_trigger_OR

                ##########
                # OUTPUT
                ##########

                values1 = [[i] for i in batch["b_mass",cuts].tolist()]
                values2 = [[i] for i in batch["b_mass_reduced",cuts].tolist()]
                values3 = [[i] for i in batch["mll",cuts].tolist()]

                if False:
                    length=10
                    for br in branches_used: print(br,batch[br][:length])
                    print(cuts[:length])
                    print(values1[:length])
                    print(values2[:length])
                    print(values3[:length])
                
                for start in range(0, len(values1),entries):
                    file_output["tree"].extend({
                        "b_mass": values1[start: start + entries],
                        "b_mass_reduced": values2[start: start + entries],
                        "mll": values3[start: start + entries],
                        "trigger_OR": [[i] for i in cuts_trigger_OR.tolist()][start: start + entries],
                        "L1_11p0_HLT_6p5": [[i] for i in cuts_L1_11p0_HLT_6p5.tolist()][start: start + entries],
                        "L1_10p5_HLT_6p5": [[i] for i in cuts_L1_11p0_HLT_6p5.tolist()][start: start + entries],
                        "L1_10p5_HLT_5p0": [[i] for i in cuts_L1_10p5_HLT_6p5.tolist()][start: start + entries],
                        "L1_8p5_HLT_5p0":  [[i] for i in cuts_L1_10p5_HLT_5p0.tolist()][start: start + entries],
                        "L1_8p0_HLT_5p0":  [[i] for i in cuts_L1_8p5_HLT_5p0 .tolist()][start: start + entries],
                        "L1_7p0_HLT_5p0":  [[i] for i in cuts_L1_8p0_HLT_5p0 .tolist()][start: start + entries],
                        "L1_6p5_HLT_4p5":  [[i] for i in cuts_L1_7p0_HLT_5p0 .tolist()][start: start + entries],
                        "L1_6p0_HLT_4p0":  [[i] for i in cuts_L1_6p5_HLT_4p5 .tolist()][start: start + entries],
                        "L1_5p5_HLT_6p0":  [[i] for i in cuts_L1_6p0_HLT_4p0 .tolist()][start: start + entries],
                        "L1_5p5_HLT_4p0":  [[i] for i in cuts_L1_5p5_HLT_6p0 .tolist()][start: start + entries],
                    })

                ##########
                # COUNTERS
                ##########
                
                initial += len(batch['b_mass'])
                bmass_nvalues += len(values1)

    print(f"Initial number of entries on input 'b_mass' branch: {initial}")
    print(f"entries per basket {entries}, time {time.time() - starttime}")
    print(f"Number of entries on skimmed branches: {bmass_nvalues}")