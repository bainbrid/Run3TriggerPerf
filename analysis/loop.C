// .L loop.C++
// run("../ntuples/data.root", "../ntuples/mc_nonprompt_2017.root", "../ntuples/mc_prompt_2017_low_stats.root")

#include <vector>
#include <iostream>
#include <string>
using namespace std;
#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
#include "TF1.h"
#include <TStyle.h>
#include "TROOT.h"
#include <map>
#include "TCanvas.h"
#include "TLegend.h"
#include "TColor.h"
#include "TFile.h"
#include "TMath.h"
#include "TGraphErrors.h"
#include "TLorentzVector.h"
#include "TGraphAsymmErrors.h"
#include "TLatex.h"
#include "TBranch.h"
#include "TTree.h"
#include "TChain.h"
#include "TMinuit.h"
#include "TROOT.h"
#include "TProfile.h"
//#include "/Applications/root/macros/AtlasStyle.C"

//#define Data
//#define trigger

TFile *root_file;
#include "tree.C"
tree *TREE;

//void run(string file){
void loop(){
  //  SetAtlasStyle();

  //  root_file = new TFile(file.c_str(),"READ");
  root_file = new TFile("/pnfs/psi.ch/cms/trivcat/store/user/ytakahas/JpsiK_20211214/flatTuple.root", "READ");
  TREE = new tree((TTree*)root_file->Get("tree"));

  int entries = (TREE->fChain)->GetEntries();

  std::cout << entries << "entries detected ..." << std::endl;

  TFile *ntuple = new TFile("ntupleOutput.root", "RECREATE");
  double mass;
  TTree *aux;
  aux = new TTree("tree", "tree");
  aux->Branch("mass", &mass);

  // start the truth/match plotting here
  for(int iEntry=0; iEntry<entries; iEntry++) { // loop in reco
    (TREE->fChain)->GetEntry(iEntry);
    if(iEntry%2000==0)
      cout << "\r" << (double)iEntry/(double)entries*100 << "\% processed" << flush;

    mass = 0;
    double pt_comp = 0;
    for (size_t i=0; i<TREE->JpsiKE_B_mass->size(); i++) {
      if (TREE->JpsiKE_B_pt->at(i)>pt_comp) {
	mass = TREE->JpsiKE_B_mass->at(i);
	pt_comp = TREE->JpsiKE_B_pt->at(i);
      }
    }
    if (mass>0.1)
      aux->Fill();
  }

  ntuple->Write();
  ntuple->Close();

  cout << endl;


}
