//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Tue Dec  7 12:19:04 2021 by ROOT version 5.34/11
// from TTree tree/tree
// found on file: flatTuple.root
//////////////////////////////////////////////////////////

#ifndef tree_h
#define tree_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include <vector>
#include <vector>
#include <vector>

// Fixed size dimensions of array or collections stored in the TTree if any.

class tree {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Int_t           EVENT_event;
   Int_t           EVENT_run;
   Int_t           EVENT_lumiBlock;
   Int_t           PV_N;
   Bool_t          PV_filter;
   vector<float>   *PV_chi2;
   vector<float>   *PV_ndof;
   vector<float>   *PV_rho;
   vector<float>   *PV_z;
   vector<float>   *BeamSpot_x0;
   vector<float>   *BeamSpot_y0;
   vector<float>   *BeamSpot_z0;
   Int_t           JpsiKE_nCandidates;
   Float_t         JpsiKE_e1_pt;
   Float_t         JpsiKE_e1_eta;
   Float_t         JpsiKE_e1_phi;
   Float_t         JpsiKE_e1_mass;
   Int_t           JpsiKE_e1_q;
   Float_t         JpsiKE_e1_vx;
   Float_t         JpsiKE_e1_vy;
   Float_t         JpsiKE_e1_vz;
   Float_t         JpsiKE_e2_pt;
   Float_t         JpsiKE_e2_eta;
   Float_t         JpsiKE_e2_phi;
   Float_t         JpsiKE_e2_mass;
   Int_t           JpsiKE_e2_q;
   Float_t         JpsiKE_e2_vx;
   Float_t         JpsiKE_e2_vy;
   Float_t         JpsiKE_e2_vz;
   Float_t         JpsiKE_PV_vx;
   Float_t         JpsiKE_PV_vy;
   Float_t         JpsiKE_PV_vz;
   Float_t         JpsiKE_bbPV_vx;
   Float_t         JpsiKE_bbPV_vy;
   Float_t         JpsiKE_bbPV_vz;
   Float_t         JpsiKE_bbPV_chi2;
   Float_t         JpsiKE_bbPV_ndof;
   Float_t         JpsiKE_bbPV_rho;
   Float_t         JpsiKE_Jpsi_pt;
   Float_t         JpsiKE_Jpsi_eta;
   Float_t         JpsiKE_Jpsi_phi;
   Float_t         JpsiKE_Jpsi_mass;
   Float_t         JpsiKE_Jpsi_vprob;
   Float_t         JpsiKE_Jpsi_lip;
   Float_t         JpsiKE_Jpsi_lips;
   Float_t         JpsiKE_Jpsi_pvip;
   Float_t         JpsiKE_Jpsi_pvips;
   Float_t         JpsiKE_Jpsi_fl3d;
   Float_t         JpsiKE_Jpsi_fls3d;
   Float_t         JpsiKE_Jpsi_alpha;
   Float_t         JpsiKE_Jpsi_maxdoca;
   Float_t         JpsiKE_Jpsi_mindoca;
   Float_t         JpsiKE_Jpsi_vx;
   Float_t         JpsiKE_Jpsi_vy;
   Float_t         JpsiKE_Jpsi_vz;
   vector<float>   *JpsiKE_B_pt;
   vector<float>   *JpsiKE_B_eta;
   vector<float>   *JpsiKE_B_phi;
   vector<float>   *JpsiKE_B_mass;
   vector<float>   *JpsiKE_B_mcorr;
   vector<float>   *JpsiKE_B_vprob;
   vector<float>   *JpsiKE_B_lip;
   vector<float>   *JpsiKE_B_lips;
   vector<float>   *JpsiKE_B_pvip;
   vector<float>   *JpsiKE_B_pvips;
   vector<float>   *JpsiKE_B_fl3d;
   vector<float>   *JpsiKE_B_fls3d;
   vector<float>   *JpsiKE_B_alpha;
   vector<float>   *JpsiKE_B_maxdoca;
   vector<float>   *JpsiKE_B_mindoca;
   vector<float>   *JpsiKE_B_vx;
   vector<float>   *JpsiKE_B_vy;
   vector<float>   *JpsiKE_B_vz;
   vector<float>   *JpsiKE_pi_pt;
   vector<float>   *JpsiKE_pi_eta;
   vector<float>   *JpsiKE_pi_phi;
   vector<float>   *JpsiKE_pi_mass;
   vector<int>     *JpsiKE_pi_q;
   vector<float>   *JpsiKE_pi_doca3d;
   vector<float>   *JpsiKE_pi_doca3de;
   vector<float>   *JpsiKE_pi_doca2d;
   vector<float>   *JpsiKE_pi_doca2de;
   vector<float>   *JpsiKE_pi_dz;
   vector<float>   *JpsiKE_pi_near_dz;
   vector<bool>    *JpsiKE_pi_isAssociate;
   vector<int>     *JpsiKE_pi_pvAssociationQuality;
   vector<float>   *JpsiKE_B_q2;
   vector<float>   *JpsiKE_B_mm2;
   vector<float>   *JpsiKE_B_ptmiss;
   vector<float>   *JpsiKE_B_Es;
   vector<float>   *JpsiKE_B_ptback;

   // List of branches
   TBranch        *b_EVENT_event;   //!
   TBranch        *b_EVENT_run;   //!
   TBranch        *b_EVENT_lumiBlock;   //!
   TBranch        *b_PV_N;   //!
   TBranch        *b_PV_filter;   //!
   TBranch        *b_PV_chi2;   //!
   TBranch        *b_PV_ndof;   //!
   TBranch        *b_PV_rho;   //!
   TBranch        *b_PV_z;   //!
   TBranch        *b_BeamSpot_x0;   //!
   TBranch        *b_BeamSpot_y0;   //!
   TBranch        *b_BeamSpot_z0;   //!
   TBranch        *b_JpsiKE_nCandidates;   //!
   TBranch        *b_JpsiKE_e1_pt;   //!
   TBranch        *b_JpsiKE_e1_eta;   //!
   TBranch        *b_JpsiKE_e1_phi;   //!
   TBranch        *b_JpsiKE_e1_mass;   //!
   TBranch        *b_JpsiKE_e1_q;   //!
   TBranch        *b_JpsiKE_e1_vx;   //!
   TBranch        *b_JpsiKE_e1_vy;   //!
   TBranch        *b_JpsiKE_e1_vz;   //!
   TBranch        *b_JpsiKE_e2_pt;   //!
   TBranch        *b_JpsiKE_e2_eta;   //!
   TBranch        *b_JpsiKE_e2_phi;   //!
   TBranch        *b_JpsiKE_e2_mass;   //!
   TBranch        *b_JpsiKE_e2_q;   //!
   TBranch        *b_JpsiKE_e2_vx;   //!
   TBranch        *b_JpsiKE_e2_vy;   //!
   TBranch        *b_JpsiKE_e2_vz;   //!
   TBranch        *b_JpsiKE_PV_vx;   //!
   TBranch        *b_JpsiKE_PV_vy;   //!
   TBranch        *b_JpsiKE_PV_vz;   //!
   TBranch        *b_JpsiKE_bbPV_vx;   //!
   TBranch        *b_JpsiKE_bbPV_vy;   //!
   TBranch        *b_JpsiKE_bbPV_vz;   //!
   TBranch        *b_JpsiKE_bbPV_chi2;   //!
   TBranch        *b_JpsiKE_bbPV_ndof;   //!
   TBranch        *b_JpsiKE_bbPV_rho;   //!
   TBranch        *b_JpsiKE_Jpsi_pt;   //!
   TBranch        *b_JpsiKE_Jpsi_eta;   //!
   TBranch        *b_JpsiKE_Jpsi_phi;   //!
   TBranch        *b_JpsiKE_Jpsi_mass;   //!
   TBranch        *b_JpsiKE_Jpsi_vprob;   //!
   TBranch        *b_JpsiKE_Jpsi_lip;   //!
   TBranch        *b_JpsiKE_Jpsi_lips;   //!
   TBranch        *b_JpsiKE_Jpsi_pvip;   //!
   TBranch        *b_JpsiKE_Jpsi_pvips;   //!
   TBranch        *b_JpsiKE_Jpsi_fl3d;   //!
   TBranch        *b_JpsiKE_Jpsi_fls3d;   //!
   TBranch        *b_JpsiKE_Jpsi_alpha;   //!
   TBranch        *b_JpsiKE_Jpsi_maxdoca;   //!
   TBranch        *b_JpsiKE_Jpsi_mindoca;   //!
   TBranch        *b_JpsiKE_Jpsi_vx;   //!
   TBranch        *b_JpsiKE_Jpsi_vy;   //!
   TBranch        *b_JpsiKE_Jpsi_vz;   //!
   TBranch        *b_JpsiKE_B_pt;   //!
   TBranch        *b_JpsiKE_B_eta;   //!
   TBranch        *b_JpsiKE_B_phi;   //!
   TBranch        *b_JpsiKE_B_mass;   //!
   TBranch        *b_JpsiKE_B_mcorr;   //!
   TBranch        *b_JpsiKE_B_vprob;   //!
   TBranch        *b_JpsiKE_B_lip;   //!
   TBranch        *b_JpsiKE_B_lips;   //!
   TBranch        *b_JpsiKE_B_pvip;   //!
   TBranch        *b_JpsiKE_B_pvips;   //!
   TBranch        *b_JpsiKE_B_fl3d;   //!
   TBranch        *b_JpsiKE_B_fls3d;   //!
   TBranch        *b_JpsiKE_B_alpha;   //!
   TBranch        *b_JpsiKE_B_maxdoca;   //!
   TBranch        *b_JpsiKE_B_mindoca;   //!
   TBranch        *b_JpsiKE_B_vx;   //!
   TBranch        *b_JpsiKE_B_vy;   //!
   TBranch        *b_JpsiKE_B_vz;   //!
   TBranch        *b_JpsiKE_pi_pt;   //!
   TBranch        *b_JpsiKE_pi_eta;   //!
   TBranch        *b_JpsiKE_pi_phi;   //!
   TBranch        *b_JpsiKE_pi_mass;   //!
   TBranch        *b_JpsiKE_pi_q;   //!
   TBranch        *b_JpsiKE_pi_doca3d;   //!
   TBranch        *b_JpsiKE_pi_doca3de;   //!
   TBranch        *b_JpsiKE_pi_doca2d;   //!
   TBranch        *b_JpsiKE_pi_doca2de;   //!
   TBranch        *b_JpsiKE_pi_dz;   //!
   TBranch        *b_JpsiKE_pi_near_dz;   //!
   TBranch        *b_JpsiKE_pi_isAssociate;   //!
   TBranch        *b_JpsiKE_pi_pvAssociationQuality;   //!
   TBranch        *b_JpsiKE_B_q2;   //!
   TBranch        *b_JpsiKE_B_mm2;   //!
   TBranch        *b_JpsiKE_B_ptmiss;   //!
   TBranch        *b_JpsiKE_B_Es;   //!
   TBranch        *b_JpsiKE_B_ptback;   //!

   tree(TTree *tree=0);
   virtual ~tree();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef tree_cxx
tree::tree(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("flatTuple.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("flatTuple.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("flatTuple.root:/ntuplizer");
      dir->GetObject("tree",tree);

   }
   Init(tree);
}

tree::~tree()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t tree::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t tree::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void tree::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   PV_chi2 = 0;
   PV_ndof = 0;
   PV_rho = 0;
   PV_z = 0;
   BeamSpot_x0 = 0;
   BeamSpot_y0 = 0;
   BeamSpot_z0 = 0;
   JpsiKE_B_pt = 0;
   JpsiKE_B_eta = 0;
   JpsiKE_B_phi = 0;
   JpsiKE_B_mass = 0;
   JpsiKE_B_mcorr = 0;
   JpsiKE_B_vprob = 0;
   JpsiKE_B_lip = 0;
   JpsiKE_B_lips = 0;
   JpsiKE_B_pvip = 0;
   JpsiKE_B_pvips = 0;
   JpsiKE_B_fl3d = 0;
   JpsiKE_B_fls3d = 0;
   JpsiKE_B_alpha = 0;
   JpsiKE_B_maxdoca = 0;
   JpsiKE_B_mindoca = 0;
   JpsiKE_B_vx = 0;
   JpsiKE_B_vy = 0;
   JpsiKE_B_vz = 0;
   JpsiKE_pi_pt = 0;
   JpsiKE_pi_eta = 0;
   JpsiKE_pi_phi = 0;
   JpsiKE_pi_mass = 0;
   JpsiKE_pi_q = 0;
   JpsiKE_pi_doca3d = 0;
   JpsiKE_pi_doca3de = 0;
   JpsiKE_pi_doca2d = 0;
   JpsiKE_pi_doca2de = 0;
   JpsiKE_pi_dz = 0;
   JpsiKE_pi_near_dz = 0;
   JpsiKE_pi_isAssociate = 0;
   JpsiKE_pi_pvAssociationQuality = 0;
   JpsiKE_B_q2 = 0;
   JpsiKE_B_mm2 = 0;
   JpsiKE_B_ptmiss = 0;
   JpsiKE_B_Es = 0;
   JpsiKE_B_ptback = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("EVENT_event", &EVENT_event, &b_EVENT_event);
   fChain->SetBranchAddress("EVENT_run", &EVENT_run, &b_EVENT_run);
   fChain->SetBranchAddress("EVENT_lumiBlock", &EVENT_lumiBlock, &b_EVENT_lumiBlock);
   fChain->SetBranchAddress("PV_N", &PV_N, &b_PV_N);
   fChain->SetBranchAddress("PV_filter", &PV_filter, &b_PV_filter);
   fChain->SetBranchAddress("PV_chi2", &PV_chi2, &b_PV_chi2);
   fChain->SetBranchAddress("PV_ndof", &PV_ndof, &b_PV_ndof);
   fChain->SetBranchAddress("PV_rho", &PV_rho, &b_PV_rho);
   fChain->SetBranchAddress("PV_z", &PV_z, &b_PV_z);
   fChain->SetBranchAddress("BeamSpot_x0", &BeamSpot_x0, &b_BeamSpot_x0);
   fChain->SetBranchAddress("BeamSpot_y0", &BeamSpot_y0, &b_BeamSpot_y0);
   fChain->SetBranchAddress("BeamSpot_z0", &BeamSpot_z0, &b_BeamSpot_z0);
   fChain->SetBranchAddress("JpsiKE_nCandidates", &JpsiKE_nCandidates, &b_JpsiKE_nCandidates);
   fChain->SetBranchAddress("JpsiKE_e1_pt", &JpsiKE_e1_pt, &b_JpsiKE_e1_pt);
   fChain->SetBranchAddress("JpsiKE_e1_eta", &JpsiKE_e1_eta, &b_JpsiKE_e1_eta);
   fChain->SetBranchAddress("JpsiKE_e1_phi", &JpsiKE_e1_phi, &b_JpsiKE_e1_phi);
   fChain->SetBranchAddress("JpsiKE_e1_mass", &JpsiKE_e1_mass, &b_JpsiKE_e1_mass);
   fChain->SetBranchAddress("JpsiKE_e1_q", &JpsiKE_e1_q, &b_JpsiKE_e1_q);
   fChain->SetBranchAddress("JpsiKE_e1_vx", &JpsiKE_e1_vx, &b_JpsiKE_e1_vx);
   fChain->SetBranchAddress("JpsiKE_e1_vy", &JpsiKE_e1_vy, &b_JpsiKE_e1_vy);
   fChain->SetBranchAddress("JpsiKE_e1_vz", &JpsiKE_e1_vz, &b_JpsiKE_e1_vz);
   fChain->SetBranchAddress("JpsiKE_e2_pt", &JpsiKE_e2_pt, &b_JpsiKE_e2_pt);
   fChain->SetBranchAddress("JpsiKE_e2_eta", &JpsiKE_e2_eta, &b_JpsiKE_e2_eta);
   fChain->SetBranchAddress("JpsiKE_e2_phi", &JpsiKE_e2_phi, &b_JpsiKE_e2_phi);
   fChain->SetBranchAddress("JpsiKE_e2_mass", &JpsiKE_e2_mass, &b_JpsiKE_e2_mass);
   fChain->SetBranchAddress("JpsiKE_e2_q", &JpsiKE_e2_q, &b_JpsiKE_e2_q);
   fChain->SetBranchAddress("JpsiKE_e2_vx", &JpsiKE_e2_vx, &b_JpsiKE_e2_vx);
   fChain->SetBranchAddress("JpsiKE_e2_vy", &JpsiKE_e2_vy, &b_JpsiKE_e2_vy);
   fChain->SetBranchAddress("JpsiKE_e2_vz", &JpsiKE_e2_vz, &b_JpsiKE_e2_vz);
   fChain->SetBranchAddress("JpsiKE_PV_vx", &JpsiKE_PV_vx, &b_JpsiKE_PV_vx);
   fChain->SetBranchAddress("JpsiKE_PV_vy", &JpsiKE_PV_vy, &b_JpsiKE_PV_vy);
   fChain->SetBranchAddress("JpsiKE_PV_vz", &JpsiKE_PV_vz, &b_JpsiKE_PV_vz);
   fChain->SetBranchAddress("JpsiKE_bbPV_vx", &JpsiKE_bbPV_vx, &b_JpsiKE_bbPV_vx);
   fChain->SetBranchAddress("JpsiKE_bbPV_vy", &JpsiKE_bbPV_vy, &b_JpsiKE_bbPV_vy);
   fChain->SetBranchAddress("JpsiKE_bbPV_vz", &JpsiKE_bbPV_vz, &b_JpsiKE_bbPV_vz);
   fChain->SetBranchAddress("JpsiKE_bbPV_chi2", &JpsiKE_bbPV_chi2, &b_JpsiKE_bbPV_chi2);
   fChain->SetBranchAddress("JpsiKE_bbPV_ndof", &JpsiKE_bbPV_ndof, &b_JpsiKE_bbPV_ndof);
   fChain->SetBranchAddress("JpsiKE_bbPV_rho", &JpsiKE_bbPV_rho, &b_JpsiKE_bbPV_rho);
   fChain->SetBranchAddress("JpsiKE_Jpsi_pt", &JpsiKE_Jpsi_pt, &b_JpsiKE_Jpsi_pt);
   fChain->SetBranchAddress("JpsiKE_Jpsi_eta", &JpsiKE_Jpsi_eta, &b_JpsiKE_Jpsi_eta);
   fChain->SetBranchAddress("JpsiKE_Jpsi_phi", &JpsiKE_Jpsi_phi, &b_JpsiKE_Jpsi_phi);
   fChain->SetBranchAddress("JpsiKE_Jpsi_mass", &JpsiKE_Jpsi_mass, &b_JpsiKE_Jpsi_mass);
   fChain->SetBranchAddress("JpsiKE_Jpsi_vprob", &JpsiKE_Jpsi_vprob, &b_JpsiKE_Jpsi_vprob);
   fChain->SetBranchAddress("JpsiKE_Jpsi_lip", &JpsiKE_Jpsi_lip, &b_JpsiKE_Jpsi_lip);
   fChain->SetBranchAddress("JpsiKE_Jpsi_lips", &JpsiKE_Jpsi_lips, &b_JpsiKE_Jpsi_lips);
   fChain->SetBranchAddress("JpsiKE_Jpsi_pvip", &JpsiKE_Jpsi_pvip, &b_JpsiKE_Jpsi_pvip);
   fChain->SetBranchAddress("JpsiKE_Jpsi_pvips", &JpsiKE_Jpsi_pvips, &b_JpsiKE_Jpsi_pvips);
   fChain->SetBranchAddress("JpsiKE_Jpsi_fl3d", &JpsiKE_Jpsi_fl3d, &b_JpsiKE_Jpsi_fl3d);
   fChain->SetBranchAddress("JpsiKE_Jpsi_fls3d", &JpsiKE_Jpsi_fls3d, &b_JpsiKE_Jpsi_fls3d);
   fChain->SetBranchAddress("JpsiKE_Jpsi_alpha", &JpsiKE_Jpsi_alpha, &b_JpsiKE_Jpsi_alpha);
   fChain->SetBranchAddress("JpsiKE_Jpsi_maxdoca", &JpsiKE_Jpsi_maxdoca, &b_JpsiKE_Jpsi_maxdoca);
   fChain->SetBranchAddress("JpsiKE_Jpsi_mindoca", &JpsiKE_Jpsi_mindoca, &b_JpsiKE_Jpsi_mindoca);
   fChain->SetBranchAddress("JpsiKE_Jpsi_vx", &JpsiKE_Jpsi_vx, &b_JpsiKE_Jpsi_vx);
   fChain->SetBranchAddress("JpsiKE_Jpsi_vy", &JpsiKE_Jpsi_vy, &b_JpsiKE_Jpsi_vy);
   fChain->SetBranchAddress("JpsiKE_Jpsi_vz", &JpsiKE_Jpsi_vz, &b_JpsiKE_Jpsi_vz);
   fChain->SetBranchAddress("JpsiKE_B_pt", &JpsiKE_B_pt, &b_JpsiKE_B_pt);
   fChain->SetBranchAddress("JpsiKE_B_eta", &JpsiKE_B_eta, &b_JpsiKE_B_eta);
   fChain->SetBranchAddress("JpsiKE_B_phi", &JpsiKE_B_phi, &b_JpsiKE_B_phi);
   fChain->SetBranchAddress("JpsiKE_B_mass", &JpsiKE_B_mass, &b_JpsiKE_B_mass);
   fChain->SetBranchAddress("JpsiKE_B_mcorr", &JpsiKE_B_mcorr, &b_JpsiKE_B_mcorr);
   fChain->SetBranchAddress("JpsiKE_B_vprob", &JpsiKE_B_vprob, &b_JpsiKE_B_vprob);
   fChain->SetBranchAddress("JpsiKE_B_lip", &JpsiKE_B_lip, &b_JpsiKE_B_lip);
   fChain->SetBranchAddress("JpsiKE_B_lips", &JpsiKE_B_lips, &b_JpsiKE_B_lips);
   fChain->SetBranchAddress("JpsiKE_B_pvip", &JpsiKE_B_pvip, &b_JpsiKE_B_pvip);
   fChain->SetBranchAddress("JpsiKE_B_pvips", &JpsiKE_B_pvips, &b_JpsiKE_B_pvips);
   fChain->SetBranchAddress("JpsiKE_B_fl3d", &JpsiKE_B_fl3d, &b_JpsiKE_B_fl3d);
   fChain->SetBranchAddress("JpsiKE_B_fls3d", &JpsiKE_B_fls3d, &b_JpsiKE_B_fls3d);
   fChain->SetBranchAddress("JpsiKE_B_alpha", &JpsiKE_B_alpha, &b_JpsiKE_B_alpha);
   fChain->SetBranchAddress("JpsiKE_B_maxdoca", &JpsiKE_B_maxdoca, &b_JpsiKE_B_maxdoca);
   fChain->SetBranchAddress("JpsiKE_B_mindoca", &JpsiKE_B_mindoca, &b_JpsiKE_B_mindoca);
   fChain->SetBranchAddress("JpsiKE_B_vx", &JpsiKE_B_vx, &b_JpsiKE_B_vx);
   fChain->SetBranchAddress("JpsiKE_B_vy", &JpsiKE_B_vy, &b_JpsiKE_B_vy);
   fChain->SetBranchAddress("JpsiKE_B_vz", &JpsiKE_B_vz, &b_JpsiKE_B_vz);
   fChain->SetBranchAddress("JpsiKE_pi_pt", &JpsiKE_pi_pt, &b_JpsiKE_pi_pt);
   fChain->SetBranchAddress("JpsiKE_pi_eta", &JpsiKE_pi_eta, &b_JpsiKE_pi_eta);
   fChain->SetBranchAddress("JpsiKE_pi_phi", &JpsiKE_pi_phi, &b_JpsiKE_pi_phi);
   fChain->SetBranchAddress("JpsiKE_pi_mass", &JpsiKE_pi_mass, &b_JpsiKE_pi_mass);
   fChain->SetBranchAddress("JpsiKE_pi_q", &JpsiKE_pi_q, &b_JpsiKE_pi_q);
   fChain->SetBranchAddress("JpsiKE_pi_doca3d", &JpsiKE_pi_doca3d, &b_JpsiKE_pi_doca3d);
   fChain->SetBranchAddress("JpsiKE_pi_doca3de", &JpsiKE_pi_doca3de, &b_JpsiKE_pi_doca3de);
   fChain->SetBranchAddress("JpsiKE_pi_doca2d", &JpsiKE_pi_doca2d, &b_JpsiKE_pi_doca2d);
   fChain->SetBranchAddress("JpsiKE_pi_doca2de", &JpsiKE_pi_doca2de, &b_JpsiKE_pi_doca2de);
   fChain->SetBranchAddress("JpsiKE_pi_dz", &JpsiKE_pi_dz, &b_JpsiKE_pi_dz);
   fChain->SetBranchAddress("JpsiKE_pi_near_dz", &JpsiKE_pi_near_dz, &b_JpsiKE_pi_near_dz);
   fChain->SetBranchAddress("JpsiKE_pi_isAssociate", &JpsiKE_pi_isAssociate, &b_JpsiKE_pi_isAssociate);
   fChain->SetBranchAddress("JpsiKE_pi_pvAssociationQuality", &JpsiKE_pi_pvAssociationQuality, &b_JpsiKE_pi_pvAssociationQuality);
   fChain->SetBranchAddress("JpsiKE_B_q2", &JpsiKE_B_q2, &b_JpsiKE_B_q2);
   fChain->SetBranchAddress("JpsiKE_B_mm2", &JpsiKE_B_mm2, &b_JpsiKE_B_mm2);
   fChain->SetBranchAddress("JpsiKE_B_ptmiss", &JpsiKE_B_ptmiss, &b_JpsiKE_B_ptmiss);
   fChain->SetBranchAddress("JpsiKE_B_Es", &JpsiKE_B_Es, &b_JpsiKE_B_Es);
   fChain->SetBranchAddress("JpsiKE_B_ptback", &JpsiKE_B_ptback, &b_JpsiKE_B_ptback);
   Notify();
}

Bool_t tree::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void tree::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t tree::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef tree_cxx
