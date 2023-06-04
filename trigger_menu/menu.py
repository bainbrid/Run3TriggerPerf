import json
import math
import numpy as np

################################################################################
# Configuration
################################################################################

# Misc
verbosity = 2

# Build the menu
optimised_menu       = 1
intermediate_columns = 0

# LHC parameters
bunches        = 1800  # This is configurable (to reflect LHC operations)
full_orbit     = 2450  # This is "fixed"
fill_duration  =   12. # hrs
levelling_time =    0. # hrs
peak_pu        =   60.

# CMS trigger params and funcs
l1_max_rate  = 110.
l1_menu_rate = 93.
allocation   = 2.9 # Di-ele allocation of L1 rate @ 2E34
l1_used = lambda pu : l1_menu_rate * (pu/peak_pu) * (bunches/full_orbit) # Used L1 rate
l1_free = lambda pu : max(allocation, l1_max_rate - l1_used(pu))         # Free L1 rate
hlt_max_rate  = 300.

# delta used by pu_best search (and corresponding delta L1 rate)
delta_pu = 0.01
delta_l1 = l1_used(delta_pu)

# TSG prescale column schema
# index 0      = emergency
# indices 1-4  = 2p4E34 --> 2p1E34
# index 5      = 2p0E34
# index 6      = 2p0E34+ZeroBias+HLTPhysics
# indices 7-20 = 1p9-E34 --> 0p6E34
column_indices = [5] + list(range(7,19))#21)) 
length         = len(column_indices)
column_labels  = [(20-x)/10 for x in range(0,length)]
pu_values      = [peak_pu-x*3 for x in range(0,length)]

# Di-electron trigger menu
l1_pts  = [11.0, 10.5, 9.0, 8.5, 8.0, 7.5, 7.0, 7.0, 6.5, 6.0, 6.0, 5.5, 5.5]#, 5.0, 4.5]
hlt_pts = [ 6.5,  6.5, 6.0, 5.5, 5.0, 5.0, 5.0, 5.0, 4.5, 4.0, 4.0, 4.0, 4.0]#, 4.0, 4.0]
effs    = [0.03, 0.04, 0.09, 0.12, 0.15, 0.22, 0.24, 0.24, 0.30, 0.39, 0.39, 0.46, 0.46]#, 0.52, 0.55] # x1E34

if verbosity>1:
    print("l1_pts: ",l1_pts)
    print("hlt_pts:",hlt_pts)
    print("effs:   ",effs)

################################################################################
# Useful functions
################################################################################

# Parameterisation of L1 rate / bx curves from 2023 data
l1_ratebx_funcs = [
    lambda pu :   289752 + (0.000306 -   289752)/(1 + (pu/282807)**1.509), # 11.0,6.5
    lambda pu :   523954 + (0.001036 -   523954)/(1 + (pu/206369)**1.583), # 10.5,6.5
    lambda pu :  1309084 + (0.010722 -  1309084)/(1 + (pu/115797)**1.669), #  9.0,6.0
    lambda pu :  2202995 + (0.003296 -  2202995)/(1 + (pu/124520)**1.680), #  8.5,5.5   
    lambda pu :  3506648 + (0.095218 -  3506648)/(1 + (pu/103156)**1.747), #  8.0,5.0
    lambda pu :  1781997 + (0.000684 -  1781997)/(1 + (pu/ 65271)**1.696), #  7.5,5.0
    lambda pu :  7912245 + (0.009392 -  7912245)/(1 + (pu/ 78876)**1.801), #  7.0,5.0
    lambda pu :  7912245 + (0.009392 -  7912245)/(1 + (pu/ 78876)**1.801), #  7.0,5.0
    lambda pu : 13023000 + (0.127634 - 13023000)/(1 + (pu/ 73575)**1.824), #  6.5,4.5
    lambda pu : 21829290 + (0.035174 - 21829290)/(1 + (pu/ 61131)**1.869), #  6.0,4.0
    lambda pu : 21829290 + (0.035174 - 21829290)/(1 + (pu/ 61131)**1.869), #  6.0,4.0
    lambda pu : 20608440 + (0.302950 - 20608440)/(1 + (pu/ 47833)**1.877), #  5.5,4.0
    lambda pu : 20608440 + (0.302950 - 20608440)/(1 + (pu/ 47833)**1.877), #  5.5,4.0
    lambda pu : 48971960 + (0.604148 - 48971960)/(1 + (pu/ 39269)**1.966), #  5.0,4.0
    lambda pu : 80150340 + (0.140223 - 80150340)/(1 + (pu/ 28891)**2.085), #  4.5,4.0
    ]

hlt_ratebx_funcs = [
    lambda pu :0.,                                                                    # 11.0,6.5
    lambda pu :0.,                                                                    # 10.5,6.5
    lambda pu :0.,                                                                    #  9.0,6.0
    lambda pu : 1856.952 + (0.000001427441 - 1856.952)/(1 + (pu/537.7534)**4.737433), #  8.5,5.5
    lambda pu : 6695.862 + (0.000004460516 - 6695.862)/(1 + (pu/861.0147)**4.236512), #  8.0,5.0
    lambda pu : 8753.011 + (0.000009374157 - 8753.011)/(1 + (pu/1341.164)**3.589976), #  7.5,5.0
    lambda pu : 0.820315 + (-5.022876e-8 - 0.820315)/(1 + (pu/86.44273)**3.770649),   #  7.0,5.0
    lambda pu : 0.820315 + (-5.022876e-8 - 0.820315)/(1 + (pu/86.44273)**3.770649),   #  7.0,5.0
    lambda pu : 11523.24 + (0.000008690305 - 11523.24)/(1 + (pu/2712.352)**2.832322), #  6.5,4.5
    lambda pu : 0.3552093 + (-1.379113e-7 - 0.3552093)/(1 + (pu/39.09098)**3.525065), #  6.0,4.0
    lambda pu : 0.3552093 + (-1.379113e-7 - 0.3552093)/(1 + (pu/39.09098)**3.525065), #  6.0,4.0
    lambda pu : 8446.93 + (0.000003146499 - 8446.93)/(1 + (pu/2033.536)**2.767513),   #  5.5,4.0
    lambda pu : 8446.93 + (0.000003146499 - 8446.93)/(1 + (pu/2033.536)**2.767513),   #  5.5,4.0
    lambda pu :0.,                                                                    #  5.0,4.0
    lambda pu :0.,                                                                    #  4.5,4.0
    ]

# Solve simultaneous equations
# 1) Free rate as a function of PU
# 2) L1 di-ele rate (possibly prescaled) as a function of PU
# 3) Solve for free rate == L1 di-ele rate, return PU value
def pu_best(l1_ratebx,l1_prescale=1.0,hlt_ratebx=None):
    delta_pu = 0.01
    pu_vector   = np.arange(pu_values[0], pu_values[-1], -1.*delta_pu)
    l1_free_vector = [ l1_free(pu) for pu in pu_vector ]
    l1_rate_vector = [ l1_ratebx(pu)*bunches/1000./l1_prescale for pu in pu_vector ]
    l1_diff_vector = [ abs(l1_free-l1_rate) for l1_free,l1_rate in zip(l1_free_vector,l1_rate_vector) ]
    l1_idx = np.argmin(l1_diff_vector)
    l1_pu = pu_vector[l1_idx]
    
    hlt_rate_vector = [ hlt_ratebx(pu)*bunches for pu in pu_vector ]
    hlt_diff_vector = [ max(hlt_max_rate-hlt_rate,0.) for hlt_rate in hlt_rate_vector ]
    hlt_idx = len(hlt_diff_vector) - np.argmin(hlt_diff_vector[::-1]) # find last occurance of min value (zero), not the first ...
    #print(pu_vector,hlt_rate_vector,hlt_diff_vector,hlt_idx,len(hlt_diff_vector))
    hlt_pu = pu_vector[hlt_idx] if hlt_idx < len(pu_vector) else pu_values[0]

    if verbosity>2:
        print("pu_vector",pu_vector[:10])
        print("l1_free_vector",l1_free_vector[:10])
        print("l1_rate_vector",l1_rate_vector[:10]) 
        print("l1_diff_vector",l1_diff_vector[:10]) 
        print("l1_argmin",l1_idx)
        print("l1_min_diff",l1_diff_vector[l1_idx])
        print("l1_pu",l1_pu)
        print("hlt_argmin",hlt_idx)
        print("hlt_pu",hlt_pu)

    if hlt_pu<l1_pu: 
        print("l1_argmin",l1_idx,"l1_pu",l1_pu,"hlt_argmin",hlt_idx,"hlt_pu",hlt_pu)
    #return max(l1_pu,hlt_pu)
    return min(l1_pu,hlt_pu)
    #return l1_pu

# Elapsed time to reach PU value assuming the given luminosity profile
# 1) Lumi-levelling for "levelling_time" [hours]
# 2) Burn off accordibng to parameterisation
# 3) Max "fill_duration" [hours]
def elapsed(pu):
    burn_off = -6.579879 + (17.99803 - -6.579879)/(1 + (pu/41.10469)**2.664125)
    if pu > 59.9 : return 0.
    else: return min(fill_duration,levelling_time + burn_off)

# Returns instantaneous luminosity as a function of PU (and # bunches)
def Linst(pu):
    return 2.e-5 * (pu/peak_pu) * (bunches/full_orbit) # Hz/fb

# Returns prescale column "label" (e.g. 2p0E34)
def label(linst):
    return str(f"{linst:.1f}").replace(".","p")+"E34"

################################################################################
# Build prescale table
################################################################################

# Determine parameter values for a given prescale column
# Return as a dict to add to the "prescale table"
def prescale_column(idx,
                    index,
                    label,
                    pu,
                    l1_pt,
                    hlt_pt,
                    l1_ratebx,
                    hlt_ratebx,
                    eff,
                    intermediate=False):

    if intermediate==False: # Default prescale columns
        l1_prescale = 1.
        if optimised_menu: pu = pu_best(l1_ratebx,l1_prescale,hlt_ratebx)
        return {
            "intermediate":intermediate,
            "index":index,
            "label":label,
            "pu":pu,
            "l1_pt":l1_pt,
            "hlt_pt":hlt_pt,
            "l1_used":l1_used(pu),
            "l1_free":l1_free(pu),
            "l1_ratebx":l1_ratebx(pu),
            "l1_prescale":l1_prescale, # unit prescale for nominal triggers
            "hlt_ratebx":hlt_ratebx(pu),
            "eff":eff,
            "eff_ps":eff/l1_prescale,
            "elapsed":min(fill_duration,elapsed(pu)),
        }
    else: # Intermediate prescale columns
        idx_prev = idx-1 if idx>0 else 0
        idx_next = idx+1 if idx<length-1 else length-1
        eff_prev = effs[idx_prev]                      # previous eff (lower)
        eff_this = eff                                 # this eff (higher)
        eff_next = effs[idx_next]                      # next eff (even higher)
        eff_mid  = eff_prev + (eff_this - eff_prev)/2. # determine mid-point eff between "prev" and "this"
        l1_prescale = eff_this/eff_mid                 # determine rate prescale to give mid-point efficiency
        pu_prev = pu_values[idx_prev]
        pu = pu_best(l1_ratebx,l1_prescale) # always done (not just for optimised menu)
        return {
            "intermediate":intermediate,
            "index":index,
            "label":label,
            "pu":pu,
            "l1_pt":l1_pt,
            "hlt_pt":hlt_pt,
            "l1_used":l1_used(pu),
            "l1_free":l1_free(pu),
            "l1_ratebx":l1_ratebx(pu),
            "l1_prescale":l1_prescale,
            "hlt_ratebx":hlt_ratebx(pu),
            "eff":eff_this,
            "eff_ps":eff_this/l1_prescale,
            "elapsed":min(fill_duration,elapsed(pu)),
        }

# Build prescale table
# 1) Populate prescale table with nominal columns
# 2) If required, populate prescale table with intermediate columns
def build_prescale_table():
    vdict = []
    for idx in range(length):
        if intermediate_columns and idx>0: # Insert intermediate columns
            dct = prescale_column(
                idx,
                column_indices[idx],
                label(column_labels[idx]),
                pu_values[idx],
                l1_pts[idx],
                hlt_pts[idx],
                l1_ratebx_funcs[idx],
                hlt_ratebx_funcs[idx],
                effs[idx],
                intermediate=True,
            )
            vdict.append(dct)
        # Add nominal columns
        dct = prescale_column(
            idx,
            column_indices[idx],
            label(column_labels[idx]),
            pu_values[idx],
            l1_pts[idx],
            hlt_pts[idx],
            l1_ratebx_funcs[idx],
            hlt_ratebx_funcs[idx],
            effs[idx],
            intermediate=False,
        )
        vdict.append(dct)
    return vdict

################################################################################
# Print summary
################################################################################

def print_info(ncol): 
    print("Optimised menu?   ","Yes" if optimised_menu==True else "No")
    print("Mid-steps?        ","Yes" if intermediate_columns==True else "No")
    print("# of columns:     ",ncol)
    print("Bunches:          ",bunches)
    print("L1 menu rate:     ",l1_menu_rate)
    print("Max L1 rate [kHz]:",l1_max_rate)
    print("Max HLT rate [Hz]:",hlt_max_rate)
    print("Fill [hrs]:       ",fill_duration)
    print("Levelling [hrs]:  ",levelling_time)

def print_header():
    print("".join([""+"Index",
                   " "+" Label",
                   " "+"  PU",
                   " | "+"L1 pT",
                   " "+"HLT pT",
                   " | "+" Menu",
                   " "+" Free",
                   " | "+"  L1/BX",
                   " "+"Rate",
                   #" "+"  PU",
                   #" "+"Rate/BX",
                   " "+"   PS" if intermediate_columns == True else "",
                   " "+"Rate/PS" if intermediate_columns == True else "",
                   " "+"Unused",
                   " | "+" HLT/BX",
                   " "+"  Rate",
                   " "+"Unused",
                   " | "+"  Eff",
                   " "+"Eff/PS"  if intermediate_columns == True else "",
                   " "+"Gain",
                   " | "+" Time",
                   " "+"dTime",
                   " "+"dLumi",
                   #" "+" Time",
                   " "+"Cands",
                   " "+"Enabled?",
     ]))

def print_row(idx,vdict):

    # Extract variables
    dct = vdict[idx]
    intermediate = dct.get("intermediate",None)
    index = dct.get("index",None)
    label = dct.get("label",None)
    pu = dct.get("pu",None)
    l1_pt = dct.get("l1_pt",None)
    hlt_pt = dct.get("hlt_pt",None)
    l1_used = dct.get("l1_used",None)
    l1_free = dct.get("l1_free",None)
    l1_ratebx = dct.get("l1_ratebx",None)
    l1_rate = l1_ratebx*bunches/1000. if l1_ratebx is not None and l1_ratebx > 0. else None
    l1_prescale = dct.get("l1_prescale",None)
    hlt_ratebx = dct.get("hlt_ratebx",None)
    hlt_rate = hlt_ratebx*bunches if hlt_ratebx is not None and hlt_ratebx > 0. else 0.
    hlt_unused = max(hlt_max_rate - hlt_rate, 0.)
    eff = dct.get("eff",None)
    eff_ps = dct.get("eff_ps",None)
    elapsed = dct.get("elapsed",None)
    
    # Previous and next indices
    idx_prev = idx-1 if idx>0 else 0
    idx_next = idx+1 if idx<len(vdict)-1 else len(vdict)-1

    # Previous and next dict entries
    dct_prev = vdict[idx_prev] if idx_prev != idx else {}
    dct_next = vdict[idx_next] if idx_next != idx else {}

    # Efficiency gain
    eff_prev = dct_prev.get("eff_ps",None)
    eff_gain = eff_ps/eff_prev if eff_prev is not None else 1.
    #eff_ps   = eff/l1_prescale
    
    # Time elapsed and delta
    elapsed_prev = dct_prev.get("elapsed",None)
    elapsed_next = dct_next.get("elapsed",None)
    delta_time   = elapsed_next - elapsed if elapsed_next is not None else fill_duration - elapsed
    enabled      = "YES" if delta_time > 0. else ""

    # Check if next delta_time is nonzero
    #idx_nnext = idx+2 if idx<len(vdict)-2 else None
    #dct_nnext = vdict[idx_nnext] if idx_nnext is not None and idx_nnext != idx else {}
    #elapsed_nnext = dct_nnext.get("elapsed",None)
    #delta_nnext = elapsed_nnext - elapsed_next if elapsed_nnext is not None else None
    #if delta_time > 0. and delta_nnext is not None and delta_nnext == 0. : delta_time = fill_duration - elapsed
    #print(elapsed_prev,elapsed,elapsed_next,elapsed_nnext,delta_time,delta_nnext)
    #print(elapsed_prev,elapsed,elapsed_next,delta_time)

    # Integrated luminosity
    lumi = Linst(pu) * delta_time * 3600. # /fb
    cands = lumi * 4.694e11 * 0.4 * 4.5e-7 * 2 * eff_ps * 1.e-4
    #print(lumi,eff_ps,cands)

    # Unused L1 rate (ensure +ve given delta_pu precision)
    l1_unused = l1_free - l1_rate/l1_prescale
    if abs(l1_unused) < delta_l1 : l1_unused = 0.
    
    if intermediate==False:
        print(f'{index:5.0f}',end='')
        print(f' {label:6s}',end='')
    else:
        print(" "*5,end='')
        print(" "*7,end='')
    print(f' {pu:4.1f}',end='')
    print(f' | {l1_pt:5.1f}',end='')
    print(f' {hlt_pt:6.1f}',end='')
    print(f' | {l1_used:5.1f}',end='')
    print(f' {l1_free:5.1f}',end='')
    print(f' | {l1_ratebx:7.1f}',end='')
    print(f' {l1_rate:4.1f}',end='')
    print(f' {l1_prescale:5.2f}' if intermediate_columns == True else '',end='')
    print(f' {l1_rate/l1_prescale:7.1f}' if intermediate_columns == True else '',end='')
    print(f' {l1_unused:6.2f}',end='')
    print(f' | {hlt_ratebx:7.3f}',end='')
    print(f' {hlt_rate:6.1f}',end='')
    print(f' {hlt_unused:6.1f}',end='')
    print(f' | {eff:5.3f}',end='')
    print(f' {eff_ps:6.3f}' if intermediate_columns == True else '',end='')
    print(f' {eff_gain:4.2f}',end='')
    print(f' | {elapsed:5.2f}',end='')
    print(f' {delta_time:5.2f}',end='')
    print(f' {lumi:5.2f}',end='')
    print(f' {cands:5.2f}',end='')
    print(f' {enabled:8s}',end='')
    print()

    dct["eff_gain"] = eff_gain
    dct["dtime"] = delta_time
    dct["lumi"] = lumi
    dct["cands"] = cands
    return dct

def print_table():
    total_elapsed = 0.
    total_lumi = 0.
    total_cands = 0.
    vdict = build_prescale_table()
    print("#"*80)
    print_info(len(vdict))
    print()
    print_header()
    for idx in range(len(vdict)):
        dct = print_row(idx,vdict)
        total_elapsed += dct.get("dtime",None)
        total_lumi += dct.get("lumi",None)
        total_cands += dct.get("cands",None)
    print(" "*111 if intermediate_columns == True else " "*114,end='')
    print(f"{total_elapsed:5.2f}",f"{total_lumi:5.2f}",f"{total_cands:5.2f}")
    print("#"*80)
    print()

################################################################################
# Execution
################################################################################

if __name__ == "__main__":
    print("Running menu.py...")
    print_table()
