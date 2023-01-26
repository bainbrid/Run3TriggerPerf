import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as plt
lumipertrigger = {
        "L1_11p0_HLT_6p5": 1.577,
        "L1_10p5_HLT_6p5": 1.136,
        "L1_10p5_HLT_5p0": 0.103,
        "L1_9p0_HLT_6p0": 8.844,
        "L1_8p5_HLT_5p5": 3.339,
        "L1_8p5_HLT_5p0": 0.675,
        "L1_8p0_HLT_5p0": 6.890,
        "L1_7p5_HLT_5p0": 1.635,
        "L1_7p0_HLT_5p0": 2.662,
        "L1_6p5_HLT_4p5": 3.611,
        "L1_6p0_HLT_4p0": 2.511,
        "L1_5p5_HLT_6p0": 0.150,
        "L1_5p5_HLT_4p0": 0.650,
        "L1_5p0_HLT_4p0": 0.041,
        "L1_4p5_HLT_4p0": 0.030
}
def expectation(val,lumi,err=None,region="Jpsi"):
    bf = {
        "Jpsi":0.001*0.06,
        "Psi2S":6.2e-4*7.9e-3,
        "LowQ2":4.5e-7,
    }.get(region)
    eff     = val/50000000
    #eff_err = err/50000000
    exp = lumi * 4.7e11 * 0.4 * bf * eff
    #exp_err = exp * (eff_err/eff)
    return exp

print(lumipertrigger["L1_11p0_HLT_6p5"])
df = pd.DataFrame(lumipertrigger, index=['w'])
df=df.drop("w")
print(df)
#rangeofnums = [11,10,"9p5",9,8,7,6,5,4]
rangeofnums = ["9p5withtrigeff"]
siglist=[]
bkglist=[]
for i in rangeofnums:
    sigbkg=[0,0]
    print(i)
    l=[]
    base = "/vols/cms/jo3717/slimming/Run3TriggerPerf/commissioning/output/2022Test/scans/scan"+str(i)+".json"
    with open(base) as f:
        data = json.load(f)
        for trig in [*lumipertrigger]:
            normSig = expectation(data['2sig']['LowQ2'][trig]["sig_num_2_sig"],lumipertrigger[trig], region="LowQ2")
            bkg = data['2sig']['LowQ2'][trig]["bkg_num_2_sig"]
            sigbkg[0] = sigbkg[0] + normSig
            sigbkg[1] = sigbkg[1] + bkg 
            soversplusb = normSig/np.sqrt(normSig+bkg)
            l.append(soversplusb)
        
    df.loc[len(df)]=l
    siglist.append(sigbkg[0])
    bkglist.append(sigbkg[1])
print(bkglist)
#print(siglist)
df['addedxclusivetrig'] = df.sum(axis=1)
df['bdtval'] = [9.5]
print(df)

for trig in [*lumipertrigger]:
    df.plot.line(x='bdtval',y=trig, style='o')
    plt.title(trig + "    Integrated lumi = " + str(lumipertrigger[trig]) + "/FB")
    plt.ylabel(r'$\dfrac{S}{\sqrt{S \plus B}}$')
    plt.savefig("bdtscanplots/BDTSCAN_withtrigeff_"+trig+".png")
    plt.clf()



siglistnew =[17.0,32.6,40,47,58.5,65.5,69.5,71.9,73.7]
soverbor=[]
for i in range(len(siglist)):
    soverborelement = siglist[i]/np.sqrt(siglist[i]+bkglist[i])
    soverbor.append(soverborelement)


plt.scatter(df['bdtval'].to_list(),soverbor)
plt.title("BDT scan with predicted Signal counts    Integrated lumi  " + str(sum(lumipertrigger.values()))+"/FB")
plt.ylabel(r'$\dfrac{S}{\sqrt{S \plus B}}$')
plt.xlabel("bdtval")
plt.savefig("bdtscanplots/BDTSCAN_addedxclusivetrig.png")
plt.clf()



print(sigbkg)
print(siglist)
print(bkglist)
print(soverbor)
