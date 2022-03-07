import ROOT
import math 
import numpy as np
from TreeProducerCommon import *

ptrange = np.arange(3, 14, 1).tolist() 

class TreeProducerGen(TreeProducerCommon):
    """Class to create a custom output file & tree; as well as create and contain branches."""

    def __init__(self, name,  dataType, **kwargs):
        print('TreeProducerGen is called for', name)
        super(TreeProducerGen, self).__init__(name,dataType, **kwargs)


#        for pt in ptrange:
#            self.addBranch('singleMu' + str(pt) + '_eta1p5',                  '?')
#            self.addBranch('singleMu' + str(pt) + '_eta2p4',                  '?')
            

        self.hist       = ROOT.TH1F('hist', 'hist', 10, 0, 10)
#        self.hist_mee       = ROOT.TH1F('mee', 'mee', 50, 2.65, 3.55)
        self.hist_mee_wide       = ROOT.TH1F('mee_wide', 'mee_wide', 50, 0, 15)

        self.hist_bmass       = ROOT.TH1F('b_mass', 'b_mass', 60, 4.5, 6)

        self.addBranch('instL',                  'f')
        self.addBranch('npu',                  'i')
        self.addBranch('isgjson',                  '?')
        self.addBranch('evt',                  'i')
        self.addBranch('run',                  'i')
        self.addBranch('lumi',                  'i')
        self.addBranch('jpsi_mass',                  'f')
        self.addBranch('jpsi_pt',                  'f')
        self.addBranch('jpsi_e1_pt',                  'f')
        self.addBranch('jpsi_e1_eta',                  'f')
        self.addBranch('jpsi_e1_phi',                  'f')
        self.addBranch('jpsi_e2_pt',                  'f')
        self.addBranch('jpsi_e2_eta',                  'f')
        self.addBranch('jpsi_e2_phi',                  'f')
        self.addBranch('b_mass',                  'f')
        self.addBranch('b_pt',                  'f')

