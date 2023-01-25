from DataFormats.FWLite import Events, Handle
from common.deltar             import deltaR, bestMatch, bestMatchAtVtx
from ROOT import TFile, TTree, TLorentzVector
from array import array
import math, copy
from os import listdir
from os.path import isfile, join
from TreeProducerGen import *
import argparse
import json
import itertools

from optparse import OptionParser, OptionValueError
usage = "usage: python runTauDisplay_BsTauTau.py"
parser = OptionParser(usage)


parser = argparse.ArgumentParser(description='example e/gamma HLT analyser')
parser.add_argument('in_filenames',nargs="+",help='input filename')
parser.add_argument('--out','-o',default="purityCheck.root",help='output filename')
parser.add_argument('--type','-t',default="data",help='type')
args = parser.parse_args()

print('filename=', args.in_filenames)

events = Events(args.in_filenames)

#import pdb; pdb.set_trace()
print('nevents = ', events.size())
Nevt = int(events.size())


me = 0.000511
mpi = 0.139571
mk = 0.493677
mB = 5.27963

drdict = {
    3.0:1.0,
    3.5:1.0,
    4.0:1.0,
    4.5:0.9,
    5.0:0.9,
    5.5:0.8,
    6.0:0.8,
    6.5:0.8,
    7.0:0.8,
    7.5:0.7,
    8.0:0.7,
    8.5:0.7,
    9.0:0.7,
    9.5:0.6,
    10.0:0.6,
    10.5:0.6,
    11.0:0.6,
    11.5:0.5,
    12.0:0.5,
    12.5:0.5,
    13.0:0.5,
    13.5:0.4,
    14.0:0.4,
}   


def hlt_criteria(hlt_eg):
    
    flag = False
    
#    if chain.eg_pms2[idx] < 10000 \
#       and chain.eg_invEInvP[idx] < 0.2 \
#       and chain.eg_trkDEtaSeed[idx] < 0.01 \
#       and chain.eg_trkDPhi[idx] < 0.2 \
#       and chain.eg_trkChi2[idx] < 40 \
#       and chain.eg_trkValidHits[idx] >= 5 \
#       and chain.eg_trkNrLayerIT[idx] >= 2:

#        flag = True


    if hlt_eg.var('hltEgammaPixelMatchVars_s2') < 10000 \
       and hlt_eg.var('hltEgammaGsfTrackVars_OneOESuperMinusOneOP') < 0.2 \
       and hlt_eg.var('hltEgammaGsfTrackVars_DetaSeed') < 0.01 \
       and hlt_eg.var('hltEgammaGsfTrackVars_Dphi') < 0.2 \
       and hlt_eg.var('hltEgammaGsfTrackVars_Chi2') < 40 \
       and hlt_eg.var('hltEgammaGsfTrackVars_ValidHits') >= 5 \
       and hlt_eg.var('hltEgammaGsfTrackVars_NLayerIT') >= 2:

        flag = True

    return flag


def createRunDict(file2read):

    rundict = {}

    run_save = None
    
    llist = {}

    for line in open(file2read):

        if line.find('STABLE BEAMS')==-1: continue

        line = line.rstrip().split(',')
    
        run = line[0].split(':')[0]
        ls = line[1].split(':')[0]
        ls_end = line[1].split(':')[1]
        _instL = float(line[5])*0.0001
        _npu = float(line[7])


        
        if run_save!=None and run != run_save:
            rundict[run_save] = llist
            llist = {}

        if ls==ls_end: 
            llist[ls] = {'instL':_instL, 'npu':_npu}
            run_save = line[0].split(':')[0]
            

    return rundict





##################################################

l1_ptthreshold = 4
hlt_ptthreshold = 4
offline_ptthreshold = 4

handle_e  = Handle ('vector<pat::Electron>')
label_e = ("slimmedElectrons",  "", "RECO")

handle_hlt =  Handle ('std::vector<trigger::EgammaObject>')
label_hlt = ("hltEgammaHLTExtra",  "", "MYHLT")

handle_l1 = Handle ('BXVector<l1t::EGamma>')
label_l1 = ("hltGtStage2Digis",  "EGamma",  "MYHLT")
                 
handle_pf = Handle ('vector<pat::PackedCandidate>')
label_pf = ("packedPFCandidates",  "",  "RECO")


rundict = createRunDict('./LumiData_2018_20200401.csv')

gjson = None

with open("/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt") as f:
    gjson = json.load(f)


##################################################

nevents = 0
nevents_interesting = 0

out = TreeProducerGen(args.out, args.type)


for ev in events:

    nevents += 1
    
    if nevents%10000==0: print('{0:.2f}'.format(float(nevents)/float(Nevt)*100.), '% processed')
        
    out.hist.Fill(0)

    _runnum = str(ev.object().eventAuxiliary().run())
    _ls = str(ev.object().eventAuxiliary().luminosityBlock())
        
    flag_gjson = False

    if _runnum in gjson:
            
        for lrange in gjson[_runnum]:

            if int(_ls) > min(lrange) and int(_ls) < max(lrange):
                flag_gjson = True
                break


    out.isgjson[0] = flag_gjson
    

    if not flag_gjson: continue

    out.evt[0] = ev.object().eventAuxiliary().event()
    out.lumi[0] = ev.object().eventAuxiliary().luminosityBlock()
    out.run[0] = ev.object().eventAuxiliary().run()
    
    if _runnum in rundict and _ls in rundict[_runnum]:
        out.instL[0] = rundict[_runnum][_ls]['instL']
        out.npu[0] = rundict[_runnum][_ls]['npu']
    else:
        out.instL[0] = -1
        out.npu[0] = -1



    ####################################
    ### Level-1 
    ####################################

    out.hist.Fill(1)


    ev.getByLabel(label_l1, handle_l1)
    l1_egs = handle_l1.product()
    l1_egs = [l1_egs.at(0,egnr) for egnr in range(0,l1_egs.size(0))]
    l1_egs = sorted(l1_egs, key = lambda e : e.et(), reverse = True )
#    print('# of Level-1 objects=', len(l1_egs))

    l1_electrons = []

    for l1idx, l1_eg in enumerate(l1_egs):

        if abs(l1_eg.eta()) > 1.218: continue
        if l1_eg.et() < 5.: continue

        l1_electrons.append(l1idx)
    

    if len(l1_electrons) < 2: continue
    out.hist.Fill(2)


    flag_l1 = False
    for ele1,ele2 in itertools.combinations(l1_electrons,2):

        if l1_egs[ele1].et() < l1_ptthreshold: continue
        if l1_egs[ele2].et() < l1_ptthreshold: continue
        
        if deltaR(l1_egs[ele1].eta(), l1_egs[ele1].phi(), l1_egs[ele2].eta(), l1_egs[ele2].phi()) > float(drdict[l1_ptthreshold]): continue
        
        flag_l1 = True
        break


    if not flag_l1: continue
    out.hist.Fill(3)


    ev.getByLabel(label_hlt, handle_hlt) 
    hlt_egs = handle_hlt.product()
    
    hlt_egs = sorted(hlt_egs, key = lambda e : e.et(), reverse = True )


    hlt_electrons = []
    for idx, hlt_eg in enumerate(hlt_egs):

        if abs(hlt_eg.eta()) > 1.218: continue
        if hlt_eg.et() < 4: continue
        if not hlt_criteria(hlt_eg): continue

        hlt_electrons.append(idx)

#    print('# of hlt electrons=', len(hlt_electrons))

    if len(hlt_electrons) < 2: continue
    out.hist.Fill(4)


    flag_hlt = False

    hltidx2match = []
    
    for ele1,ele2 in itertools.combinations(hlt_electrons,2):
            
        if hlt_egs[ele1].et() < hlt_ptthreshold: continue
        if hlt_egs[ele2].et() < hlt_ptthreshold: continue

        tlv1 = TLorentzVector()
        tlv1.SetPtEtaPhiM(hlt_egs[ele1].et(), 
                          hlt_egs[ele1].eta(), 
                          hlt_egs[ele1].phi(),
                          me)

        tlv2 = TLorentzVector()
        tlv2.SetPtEtaPhiM(hlt_egs[ele2].et(), 
                          hlt_egs[ele2].eta(), 
                          hlt_egs[ele2].phi(),
                          me)
        
        mass = (tlv1 + tlv2).M()

        if mass > 6.: continue

        flag_hlt = True

        if ele1 not in hltidx2match: hltidx2match.append(ele1)
        if ele2 not in hltidx2match: hltidx2match.append(ele2)


    if not flag_hlt: continue

    out.hist.Fill(5)

#    print('indices=', hltidx2match)

    nevents_interesting += 1

    ev.getByLabel(label_e, handle_e) 
    electrons = handle_e.product()

#    print('# of electrons =', len(electrons))

    offline_electrons = []
    for ie, electron in enumerate(electrons):

#        print(ie, electron.pt())

        if electron.pt() < offline_ptthreshold: continue

        # mimic HLT matching here
        flag_match = False

        for hltidx in hltidx2match:
            
            if deltaR(electron.eta(), electron.phi(), hlt_egs[hltidx].eta(), hlt_egs[hltidx].phi()) < 0.2:
                flag_match = True

#        if not flag_match: 
#            print ('This even did not match ...')
#            continue

        offline_electrons.append(ie)
        

    if len(offline_electrons) < 2: continue
    out.hist.Fill(6)

    highest_jpsi_pt = -1
    highest_jpsi = TLorentzVector()
    highest_e1 = TLorentzVector()
    highest_e2 = TLorentzVector()

    for ele1,ele2 in itertools.combinations(offline_electrons,2):

        tlv1 = TLorentzVector()
        tlv1.SetPtEtaPhiM(electrons[ele1].et(), 
                          electrons[ele1].eta(), 
                          electrons[ele1].phi(),
                          me)

        tlv2 = TLorentzVector()
        tlv2.SetPtEtaPhiM(electrons[ele2].et(), 
                          electrons[ele2].eta(), 
                          electrons[ele2].phi(),
                          me)


        jpsi = tlv1 + tlv2

        jpsi_mass = jpsi.M()

#        print('jpsi_mass =', jpsi_mass)


        out.hist_mee_wide.Fill(jpsi_mass)

        if jpsi_mass < 2.95: continue
        if jpsi_mass > 3.25: continue

#        if jpsi_mass < 2.65: continue
#        if jpsi_mass > 3.55: continue


        jpsi_pt = jpsi.Pt()

        if jpsi_pt > highest_jpsi_pt:
            highest_jpsi_pt = jpsi_pt 
            highest_jpsi = jpsi
            highest_e1 = tlv1
            highest_e2 = tlv2

#    out.hist_mee.Fill(highest_jpsi_mass)

    if highest_jpsi_pt==-1: continue
    out.hist.Fill(7)

    out.jpsi_mass[0] = highest_jpsi.M()
    out.jpsi_pt[0] = highest_jpsi.Pt()
    out.jpsi_e1_pt[0] = highest_e1.Pt()
    out.jpsi_e1_eta[0] = highest_e1.Eta()
    out.jpsi_e1_phi[0] = highest_e1.Phi()
    out.jpsi_e2_pt[0] = highest_e2.Pt()
    out.jpsi_e2_eta[0] = highest_e2.Eta()
    out.jpsi_e2_phi[0] = highest_e2.Phi()

#    chosen_b_pt = -1
    diff_mB = 100
    chosen_b = TLorentzVector()

    # now read PF candidates
    ev.getByLabel(label_pf, handle_pf)
    pfs = handle_pf.product()

    for ipf, pf in enumerate(pfs):
        if pf.pt() < 0.5: continue
        if not pf.hasTrackDetails(): continue
        
        if deltaR(pf.eta(), pf.phi(), highest_jpsi.Eta(), highest_jpsi.Phi()) < 0.2: continue

        if not pf.trackHighPurity(): continue
        if pf.pseudoTrack().hitPattern().numberOfValidPixelHits() < 0: continue
        if pf.pseudoTrack().hitPattern().numberOfValidHits() < 3: continue
        if pf.pseudoTrack().normalizedChi2() > 100: continue

        if abs(pf.pdgId())!=211 : continue
        if abs(pf.eta()) > 2.5: continue

        
        tlv_pi = TLorentzVector()
        tlv_pi.SetPtEtaPhiM(pf.et(), 
                            pf.eta(), 
                            pf.phi(),
                            mk)

        bcand = highest_jpsi + tlv_pi

        out.hist_bmass.Fill(bcand.M())

        if abs(bcand.M() - mB) < diff_mB:
            diff_mB = abs(bcand.M() - mB)
#            chosen_b_pt = bcand.Pt()
            chosen_b = bcand

            
#        print(ipf, bcand.M())


    out.b_mass[0] = chosen_b.M()
    out.b_pt[0] = chosen_b.Pt()

    out.tree.Fill()



print(nevents, 'has been analyzed (', nevents_interesting, ' interesting events)')

out.endJob()
