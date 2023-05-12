import json
import math
import numpy as np

###############
# Configurables
###############

# Misc
verbosity = 2

# LHC parameters
bunches = 2450    # This is configurable (to reflect LHC operations)
full_orbit = 2450 # This is "fixed"

# CMS trigger params and funcs
l1_max_rate = 110.
l1_menu_rate = 93.
l1_used = lambda pu : l1_menu_rate * (pu/60.) * (bunches/full_orbit) # Used L1 rate
l1_free = lambda pu : max(2., l1_max_rate - l1_used(pu))             # Free L1 rate

enable_prescale = True

############################
# TSG prescale column schema
############################

# index 0      = emergency
# indices 1-4  = 2p4E34 --> 2p1E34
# index 5      = 2p0E34
# index 6      = 2p0E34+ZeroBias+HLTPhysics
# indices 7-20 = 1p9-E34 --> 0p6E34
column_indices = [5] + list(range(7,21)) 
length         = len(column_indices)
column_labels  = [(20-x)/10 for x in range(0,length)]
pu_values      = [60-x*3 for x in range(0,length)]

if verbosity>1:
    print("length:        ",length)
    print("column_indices:",column_indices)
    print("column_labels: ",column_labels)
    print("pu_values:     ",pu_values)

##################
# Di-electron menu
##################

l1_pts  = [11.0, 10.5, 9.0, 8.5, 8.0, 7.5, 7.0, 7.0, 6.5, 6.0, 6.0, 5.5, 5.5, 5.0, 4.5]
hlt_pts = [ 6.5,  6.5, 6.0, 5.5, 5.0, 5.0, 5.0, 5.0, 4.5, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
effs    = [0.03, 0.04, 0.09, 0.12, 0.15, 0.22, 0.24, 0.24, 0.30, 0.39, 0.39, 0.46, 0.46, 0.52, 0.55] # x1E34

if verbosity>1:
    print("l1_pts: ",l1_pts)
    print("hlt_pts:",hlt_pts)
    print("effs:   ",effs)

# Parameterisation of L1 rate / bx curves from 2023 data
ratebx_funcs = [
    lambda pu :   289752 + (0.000306 -   289752)/(1 + (pu/282807)**1.509), # 11.0
    lambda pu :   523954 + (0.001036 -   523954)/(1 + (pu/206369)**1.583), # 10.5
    lambda pu :  1309084 + (0.010722 -  1309084)/(1 + (pu/115797)**1.669), #  9.0
    lambda pu :  2202995 + (0.003296 -  2202995)/(1 + (pu/124520)**1.680), #  8.5    
    lambda pu :  3506648 + (0.095218 -  3506648)/(1 + (pu/103156)**1.747), #  8.0
    lambda pu :  1781997 + (0.000684 -  1781997)/(1 + (pu/ 65271)**1.696), #  7.5
    lambda pu :  7912245 + (0.009392 -  7912245)/(1 + (pu/ 78876)**1.801), #  7.0
    lambda pu :  7912245 + (0.009392 -  7912245)/(1 + (pu/ 78876)**1.801), #  7.0
    lambda pu : 13023000 + (0.127634 - 13023000)/(1 + (pu/ 73575)**1.824), #  6.5 
    lambda pu : 21829290 + (0.035174 - 21829290)/(1 + (pu/ 61131)**1.869), #  6.0
    lambda pu : 21829290 + (0.035174 - 21829290)/(1 + (pu/ 61131)**1.869), #  6.0
    lambda pu : 20608440 + (0.302950 - 20608440)/(1 + (pu/ 47833)**1.877), #  5.5
    lambda pu : 20608440 + (0.302950 - 20608440)/(1 + (pu/ 47833)**1.877), #  5.5
    lambda pu : 48971960 + (0.604148 - 48971960)/(1 + (pu/ 39269)**1.966), #  5.0
    lambda pu : 80150340 + (0.140223 - 80150340)/(1 + (pu/ 28891)**2.085), #  4.5
    ]

def pu_enable(ratebx,prescale=1.0):
    pu_vector   = np.arange(pu_values[0], pu_values[-1], -0.1)
    free_vector = [ l1_free(pu) for pu in pu_vector ]
    rate_vector = [ ratebx(pu)*bunches/1000./prescale for pu in pu_vector ]
    diff_vector = [ abs(rate-free) for free,rate in zip(free_vector,rate_vector) ]
    idx = np.argmin(diff_vector)
    pu = pu_vector[idx]
    if verbosity>2:
        print("pu_vector",pu_vector[:10])
        print("free_vector",free_vector[:10])
        print("rate_vector",rate_vector[:10]) 
        print("diff_vector",diff_vector[:10]) 
        print("argmin",idx)
        print("min diff",diff_vector[idx])
        print("pu",pu)
    return pu

###############
# Print summary
###############

def print_info(): 
    print("# of columns: ",length)
    print("Bunches:      ",bunches)
    print("Max L1 rate:  ",l1_max_rate)
    print("L1 menu rate: ",l1_menu_rate)

def print_header():
    print("   ".join(["Index",
                      " Label",
                      "  PU",
                      "L1 pT",
                      "HLT pT",
                      " Used",
                      " Free",
                      "Rate/BX",
                      "Rate",
                      "  PU",
                      "Rate/BX",
                      "  PS",
                      "Rate",
                      "  Eff",
                      "Eff/PS",
                      "Gain",
                          ]))

def print_row(idx,
              index,
              label,
              pu,
              l1_pt,
              hlt_pt,
              ratebx,
              eff):

    pu_this     = pu_enable(ratebx)
    ratebx_this = ratebx(pu_this)
    rate_this   = ratebx(pu_this)*bunches/1000.
    
    #enable_prescale=False
    if enable_prescale and idx>0:
        idx_last    = idx-1
        eff_last   = effs[idx_last]
        eff_new     = eff_last + (eff - eff_last)/2.
        prescale    = eff / eff_new
        pu_last     = pu_enable(ratebx_funcs[idx_last])
        pu_diff     = pu_last - pu_this
        pu_new      = pu_enable(ratebx,prescale)# pu_this + pu_diff/2.
        ratebx_last = ratebx_funcs[idx_last](pu_last)
        rate_last   = ratebx_funcs[idx_last](pu_last)*bunches/1000.
        rate_new    = ratebx(pu_new)*bunches/1000.
        #print("eff",eff)
        #print("eff_last",eff_last)
        #print("eff_mid",eff_last + (eff - eff_last)/2.)
        #print("pu_last",pu_last)
        #print("pu_this",pu_this)
        #print("pu_diff",pu_diff)
        #print("pu_new",pu_new)
        #print("ratebx_last",ratebx_last)
        #print("rate_last",rate_last)
        #print("rate_new",rate_new)
        #print("prescale",prescale)
        if pu_diff>0.:
            print(f'     ',end='')
            print(f'         ',end='')
            print(f'       ',end='')
            print(f' | {l1_pt:5.1f}',end='')
            print(f'   {hlt_pt:6.1f}',end='')
            print(f' | {l1_used(pu_new):5.1f}',end='')
            print(f'   {l1_free(pu_new):5.1f}',end='')
            print(f' | {ratebx(pu_new):7.1f}',end='')
            print(f'   {ratebx(pu_new)*bunches/1000.:4.1f}',end='')
            print(f' | {pu_new:4.1f}',end='')
            print(f'   {ratebx(pu_new):7.1f}',end='')
            print(f'   {prescale:4.2f}',end='')
            print(f'   {ratebx(pu_new)*bunches/1000./prescale:4.1f}',end='')
            print(f' | {eff:5.3f}',end='')
            print(f'   {eff_new:6.3f}',end='')
            print(f'   {eff_new/eff_last:4.2f}',end='')
            print()

    print(f'{index:5.0f}',end='')
    print(f'   {label:6s}',end='')
    print(f'   {pu:4.1f}',end='')
    print(f' | {l1_pt:5.1f}',end='')
    print(f'   {hlt_pt:6.1f}',end='')
    print(f' | {l1_used(pu):5.1f}',end='')
    print(f'   {l1_free(pu):5.1f}',end='')
    print(f' | {ratebx(pu):7.1f}',end='')
    print(f'   {ratebx(pu)*bunches/1000.:4.1f}',end='')
    print(f' | {pu_this:4.1f}',end='')
    print(f'   {ratebx_this:7.1f}',end='')
    print(f'   1.00',end='')
    print(f'   {rate_this:4.1f}',end='')
    print(f' | {eff:5.3f}',end='')
    print(f'   {eff:6.3f}',end='')
    print()

    return pu_this

def label(linst):
    return str(f"{linst:.1f}").replace(".","p")+"E34"
    
def print_table():
    print("#"*80)
    print_info()
    print()
    print_header()
    for idx in range(length):
        print_row(idx,
                  column_indices[idx],
                  label(column_labels[idx]),
                  pu_values[idx],
                  l1_pts[idx],
                  hlt_pts[idx],
                  ratebx_funcs[idx],
                  effs[idx])
    print("#"*80)
    print()

###########
# Execution
###########

if __name__ == "__main__":
    print("Running menu.py...")
    print_table()
