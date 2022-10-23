import json

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

def print_signal_row(dct,trigger,isMC='mc',region='Jpsi'):
    sub_dct = dct[isMC][region][trigger]
    print(f'{trigger:16s}, ',end='')
    val,err = val_err(sub_dct,"signal_num")
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

def print_signal_table(dct,triggers,isMC="mc",region="Jpsi"):
    print("Table of signal parameter values for","isMC=",isMC,"region=",region)
    print_signal_header()
    for trigger,lumi in triggers:
        print_signal_row(dct,trigger,isMC=isMC,region=region)
    print()

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

def print_comparison_table(dct,triggers,region="Jpsi"):
    print("Comparison for observed (data) and expected (MC) in region",region)
    bf = {
        "Jpsi":0.001*0.06,
        "Psi2S":6.2e-4*7.9e-3,
        "LowQ2":4.5e-7,
    }.get(region)
    for trigger,lumi in triggers:
        data = dct["data"][region][trigger]
        mc   = dct["mc"][region][trigger]
        print(f"{trigger:16s}, ",end="")
        print(f"{lumi:4.2f}, ",end="")
        val,err = val_err(mc,"signal_num")
        eff     = val / 50.e6
        eff_err = err / 50.e6
        print(f"{eff/1.e-4:4.2f}+/-{eff_err/1.e-4:4.2f}, " , end="")
        exp = lumi * 4.7e11 * 0.4 * bf * eff
        exp_err = exp * (eff_err/eff)
        print(f"{exp:7.1f}+/-{exp_err:5.1f}, ",end="")
        obs,obs_err = val_err(data,"signal_num")
        print(f'{obs:7.1f}+/-{obs_err:5.1f}, ',end='')
        print()

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
    #print_signal_table(dct,triggers,isMC="mc",region="Jpsi")
    #print_signal_table(dct,triggers,isMC="data",region="Jpsi")
    #print_bkgd_table(dct,triggers,region="Jpsi",partial=_partial)
    #print_signal_table(dct,triggers,isMC="mc",region="Psi2S")
    #print_signal_table(dct,triggers,isMC="data",region="Psi2S")
    #print_bkgd_table(dct,triggers,region="Psi2S",partial=_partial)
    #print_signal_table(dct,triggers,isMC="mc",region="LowQ2")
    #print_signal_table(dct,triggers,isMC="data",region="LowQ2")
    #print_bkgd_table(dct,triggers,region="LowQ2",partial=_partial)

    # Comparison
    print_comparison_table(dct,triggers,region="Jpsi")
    print_comparison_table(dct,triggers,region="Psi2S")
    print_comparison_table(dct,triggers,region="LowQ2")

################################################################################
# Main ...

if __name__ == "__main__":

    filename = 'parameters.json'
    triggers = [
        ("trigger_none",7.36),
#        ("trigger_OR",7.10),
#        ("L1_11p0_HLT_6p5",7.09),
#        ("L1_10p5_HLT_6p5",7.04),
#        ("L1_10p5_HLT_5p0",6.28),
#        ("L1_8p5_HLT_5p0",6.18),
#        ("L1_8p0_HLT_5p0",5.60),
#        ("L1_7p0_HLT_5p0",2.00),
#        ("L1_6p5_HLT_4p5",1.78),
#        ("L1_6p0_HLT_4p0",0.65),
#        ("L1_5p5_HLT_6p0",0.15),
#        ("L1_5p5_HLT_4p0",0.00),
    ]
    summary(filename,triggers=triggers)
