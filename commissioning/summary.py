import json
import math
import numpy as np

################################################################################
# Methods ...

#for value in ['signal_num','cb_mean','cb_sigma','cb_alphaL','cb_alphaR','cb_nL','cb_nR',]:

def val_err(dct,string):
    return (
        dct[string][0], # central value
        dct[string][0]-dct[string][1] # central value - low value = error
        )

def print_signal_header():
    print(
        "Trigger"+
        "                    Counts"+
        "            Mass"+
        "           Width"+
        "     cb_alphaL"+
        "            cb_nL"+
        "     cb_alphaR"+
        "            cb_nR"
        )

def print_signal_row(dct,trigger,lumi,isMC='mc',region='Jpsi'):
    sub_dct = dct[isMC][region][trigger]
    print(f'{trigger:16s}, ',end='')
    val,err = val_err(sub_dct,"signal_num")
    count = (val,err)
    #if isMC=='mc': count = expectation(val,lumi,err,region)
    print(f'{val:7.1f}+/-{err:5.1f} , ',end='')
    val,err = val_err(sub_dct,"cb_mean")
    print(f'{val:5.3f}+/-{err:5.3f} , ',end='')
    val,err = val_err(sub_dct,"cb_sigma")
    print(f'{val:5.3f}+/-{err:5.3f} , ',end='')
    val,err = val_err(sub_dct,"cb_alphaL")
    print(f'{val:4.2f}+/-{err:4.2f} , ',end='')
    val,err = val_err(sub_dct,"cb_nL")
    print(f'{val:6.2f}+/-{err:5.2f} , ',end='')
    val,err = val_err(sub_dct,"cb_alphaR")
    print(f'{val:4.2f}+/-{err:4.2f} , ',end='')
    val,err = val_err(sub_dct,"cb_nR")
    print(f'{val:6.2f}+/-{err:5.2f} , ',end='')
    print()
    return count

def print_signal_table(dct,triggers,isMC="mc",region="Jpsi"):
    print("Table of signal parameter values for","isMC=",isMC,"region=",region)
    print_signal_header()
    counts = []
    for trigger,lumi in triggers:
        count,err = print_signal_row(dct,trigger,lumi,isMC=isMC,region=region)
        counts.append((count,err))
    print()
    return counts

def print_bkgd_header():
    print(
        "Trigger"+
        "                  comb_num"+
        "      exp_slope"
        "           part_num"+
        "     expo_slope"+
        #"    expo_offset"+
        "      erfc_mean"+
        "      erfc_sigma"
        )

def print_bkgd_row(dct,trigger,isMC='data',region='Jpsi',partial=True):
    sub_dct = dct[isMC][region][trigger]
    print(f'{trigger:16s}, ',end='')
    val,err = val_err(sub_dct,"comb_num")
    print(f'{val:7.1f}+/-{err:5.1f} , ',end='')
    val,err = val_err(sub_dct,"exp_slope")
    print(f'{val:5.2f}+/-{err:4.2f} , ',end='')
    if partial==True:
        val,err = val_err(sub_dct,"part_num")
        print(f'{val:7.1f}+/-{err:6.1f} , ',end='')
        val,err = val_err(sub_dct,"expo_slope")
        #print(f'{val:6.1f}+/-{err:5.1f} , ',end='')
        #val,err = val_err(sub_dct,"expo_offset")
        print(f'{val:5.2f}+/-{err:4.2f} , ',end='')
        val,err = val_err(sub_dct,"erfc_mean")
        print(f'{val:5.2f}+/-{err:4.2f} , ',end='')
        val,err = val_err(sub_dct,"erfc_sigma")
        print(f'{val:5.3f}+/-{err:4.3f} , ',end='')
    print()
                
def print_bkgd_table(dct,triggers,region="Jpsi",partial=True):
    isMC='data'
    print("Table of background parameter values for","isMC=",isMC,"region=",region)
    print_bkgd_header()
    for trigger,lumi in triggers:
        print_bkgd_row(dct,trigger,isMC=isMC,region=region,partial=partial)
    print()

def print_comparison_header():
    print(
        "Trigger"+
        "      Lint [fb]"+
        "   AxE [1e-4]"
        "      Exp. counts"+
        "      Obs. counts"+
        "         Ratio"
        )

def ntoys(): return 50.e6

def expectation(val,lumi,err=None,region="Jpsi"):
    bf = {
        "Jpsi":0.001*0.06,
        "Psi2S":6.2e-4*7.9e-3,
        "LowQ2":4.5e-7,
    }.get(region)
    eff     = val / ntoys()
    eff_err = err / ntoys()
    exp = lumi * 4.7e11 * 0.4 * bf * eff
    exp_err = exp * (eff_err/eff)
    return (exp,exp_err)

def print_comparison_table(dct,triggers,region="Jpsi"):
    print("Comparison for observed (data) and expected (MC) in region",region)
    print_comparison_header()
    ratios = []
    for trigger,lumi in triggers:
        data = dct["data"][region][trigger]
        mc   = dct["mc"][region][trigger]
        print(f"{trigger:16s}, ",end="")
        print(f"{lumi:4.2f}, ",end="")
        val,err = val_err(mc,"signal_num")
        eff     = val / ntoys()
        eff_err = err / ntoys()
        print(f"{eff/1.e-4:4.2f}+/-{eff_err/1.e-4:4.2f}, " , end="")
        exp,exp_err = expectation(val,lumi,err,region)
        print(f"{exp:7.1f}+/-{exp_err:5.1f}, ",end="")
        obs,obs_err = val_err(data,"signal_num")
        print(f'{obs:7.1f}+/-{obs_err:5.1f} ',end='')
        ratio = obs/exp if exp > 0. else 0.
        ratio_err = math.sqrt(exp)/exp * ratio if exp > 0. else 0.
        print(f'{ratio:5.2f}+/-{ratio_err:5.2f} ',end='')
        print()
        ratios.append((ratio,ratio_err))
    return ratios

def summary(filename,triggers=None) :

    print("Parsing json file ...")

    # Open file and parse json
    dct = {}
    try:
      with open(filename,'r') as f:
        try:
          dct = json.load(f)
        except json.decoder.JSONDecodeError:
          print("Problem parsing json contained in file:",filename)
    except FileNotFoundError:
      print("Problem opening file:",filename)

    # Check if MC content is there
    if "mc" not in dct:
        print("Incorrect json format...")
        return

    # Tables ...
    _partial=True
    mc_jpsi = print_signal_table(dct,triggers,isMC="mc",region="Jpsi")
    data_jpsi = print_signal_table(dct,triggers,isMC="data",region="Jpsi")
    print_bkgd_table(dct,triggers,region="Jpsi",partial=_partial)
    mc_psi2s = print_signal_table(dct,triggers,isMC="mc",region="Psi2S")
    data_psi2s = print_signal_table(dct,triggers,isMC="data",region="Psi2S")
    print_bkgd_table(dct,triggers,region="Psi2S",partial=_partial)
    mc_lowq2 = print_signal_table(dct,triggers,isMC="mc",region="LowQ2")
    data_lowq2 = print_signal_table(dct,triggers,isMC="data",region="LowQ2")
    print_bkgd_table(dct,triggers,region="LowQ2",partial=_partial)

    # Comparison
    ratios_jpsi = print_comparison_table(dct,triggers,region="Jpsi")
    ratios_psi2s = print_comparison_table(dct,triggers,region="Psi2S")
    ratios_lowq2 = print_comparison_table(dct,triggers,region="LowQ2")

    # Compare 
    print()
    print("Obs and exp: Jpsi and Psi2S")
    for (trg,lumi),d_jpsi,m_jpsi,d_psi2s,m_psi2s in zip(triggers,data_jpsi,mc_jpsi,data_psi2s,mc_psi2s):
        m_jpsi = expectation(m_jpsi[0],lumi,m_jpsi[1],"Jpsi")
        m_psi2s = expectation(m_psi2s[0],lumi,m_psi2s[1],"Psi2S")
        print(
            f'Trigger: {trg:16s}',
            f'  (J/psi) Exp: {m_jpsi[0]:7.1f}, Obs: {d_jpsi[0]:7.1f}',
            f'  (Psi2S) Exp: {m_psi2s[0]:6.1f}, Obs: {d_psi2s[0]:6.1f}',
            )

    # Double ratio
    print()
    print("Double ratio: [obs/exp]_Psi2S / [obs/exp]_Jpsi")
    for trg,jpsi,psi2s in zip(triggers,ratios_jpsi,ratios_psi2s):
        ratio = psi2s[0]/jpsi[0] if jpsi[0]>0. else 0.
        ratio_err  = ( jpsi[1]/ jpsi[0])**2. if  jpsi[0]>0. else 0.
        ratio_err += (psi2s[1]/psi2s[0])**2. if psi2s[0]>0. else 0.
        ratio_err = ratio * np.sqrt(ratio_err)
        #print(trg,ratio,ratio_err)
        print(f'Trigger: {trg[0]:16s}, Lumi: {trg[1]:4.2f}, Ratio: {ratio:4.2f} +/- {ratio_err:4.2f}')

    # Ratio of AxE
    print()
    print("AxE [x1E-4]")
    for trg,m_jpsi,m_psi2s,m_lowq2 in zip(triggers,mc_jpsi,mc_psi2s,mc_lowq2):
        print(
            f'Trigger: {trg[0]:16s}',
            f'  (AxE) J/psi: {m_jpsi[0]*1.e4/ntoys():4.2f}',
            f'Psi2S: {m_psi2s[0]*1.e4/ntoys():4.2f}',
            f'LowQ2: {m_lowq2[0]*1.e4/ntoys():5.3f}',
            f'  (Ratios) LowQ2/Jpsi: {m_lowq2[0]/m_jpsi[0] if m_jpsi[0]>0. else 0.:5.3f}',
            f'Psi2S/Jpsi: {m_psi2s[0]/m_jpsi[0] if m_jpsi[0]>0. else 0.:5.3f}',
            )

    # Predict Psi2S
    print()
    print("Predict @ Psi(2S)")
    for (trg,lumi),r_jpsi,m_psi2s,d_psi2s in zip(triggers,ratios_jpsi,mc_psi2s,data_psi2s):
        m_psi2s = expectation(m_psi2s[0],lumi,m_psi2s[1],"Psi2S")
        print(
            f'Trigger: {trg:16s}',
            f'  Obs/Exp @ Jpsi: {r_jpsi[0]:4.2f}',
            f'  Exp @ LowQ2: {m_psi2s[0]:5.1f}',
            f'  Pred @ LowQ2: {m_psi2s[0]*r_jpsi[0]:5.1f}',
            f'  Obs @ LowQ2: {d_psi2s[0]:5.1f}',
            )

    # Predict LowQ2 (blinded)
    print()
    print("Predict @ low q2")
    for (trg,lumi),r_jpsi,m_lowq2,_ in zip(triggers,ratios_jpsi,mc_lowq2,data_lowq2):
        m_lowq2 = expectation(m_lowq2[0],lumi,m_lowq2[1],"LowQ2")
        print(
            f'Trigger: {trg:16s}',
            f'  Obs/Exp @ Jpsi: {r_jpsi[0]:4.2f}',
            f'  Exp @ LowQ2: {m_lowq2[0]:5.1f}',
            f'  Pred @ LowQ2: {m_lowq2[0]*r_jpsi[0]:5.1f}',
            #f'  Obs @ LowQ2: {d_lowq2[0]:5.1f}', #@@
            )
    
################################################################################
# Main ...

if __name__ == "__main__":

    # Production tag
    tag = ["2022Sep05","2022Oct12","2022Nov14","2022Test"][-1]
    
    filename = 'output/'+tag+'/params/parameters.json'
    triggers = [
#        ("trigger_none",7.36),
#        ("trigger_OR",7.10),
        ("L1_11p0_HLT_6p5",7.09),
        ("L1_10p5_HLT_6p5",7.04),
        ("L1_10p5_HLT_5p0",6.28),
        ("L1_8p5_HLT_5p0",6.18),
        ("L1_8p0_HLT_5p0",5.60),
        ("L1_7p0_HLT_5p0",2.00),
        ("L1_6p5_HLT_4p5",1.78),
        ("L1_6p0_HLT_4p0",0.65),
        ("L1_5p5_HLT_6p0",0.15),
        ("L1_5p5_HLT_4p0",0.00),
    ]
    summary(filename,triggers=triggers)
