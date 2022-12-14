#include <TAttMarker.h>
#include <TCanvas.h>
#include <TCut.h>
#include <TFile.h>
#include <TH1F.h>
#include <TH2F.h>
#include <TMath.h>
#include <TString.h>
#include <TTree.h>
#include <iostream>
#include <string>
#include <typeinfo>
#include <vector>

void plot_rob(){

  int isMC = 1;
  int rare = 0;

  //TString tag = "2022Sep05";
  TString tag = "2022Oct12";
  
  TString sample = "";
  if      (isMC==0)            { sample = "Run2022D"; }
  else if (isMC==1 && rare==1) { sample = "BuToKee"; }
  else if (isMC==1 && rare==0) { sample = "BuToKJpsi_Toee"; }
  else { std::cout << "Unknown config!" << std::endl; exit(1); }

  TFile* f = TFile::Open("./input/ntuples/"+tag+"/ntuple_"+tag+"_"+sample+".root");

  TTree* events = (TTree*)f->Get("tree");
  TString dir = "./output/plots/"+tag+"/";

  TCanvas* c1 = new TCanvas("c1"); 
  TH1F* histo;
  TString name;
  TString var;
  
  // Initial cuts ...
  TCut cuts = "";

  // GEN-level
  if (isMC==1) {
    TCut gen = "inAcc==1 && isMatched==1";
    cuts += gen;
  }

  // B mass (pre-cuts)
  name = "b_mass_pre";
  var = "b_mass";
  histo = new TH1F(name,name,50,4.7,5.7);
  events->Draw(var+">>"+name,cuts);
  c1->SetLogy(0);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");

  // Trigger
  TCut trg = "HLT_DoubleEle6p5==1";
  cuts += trg;

  // B mass (post-trg)
  name = "b_mass_post_trg";
  var = "b_mass";
  histo = new TH1F(name,name,50,4.7,5.7);
  events->Draw(var+">>"+name,cuts);
  c1->SetLogy(0);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");

  // Electron ID
  cuts += "e1_reco_loose==1 && e2_reco_loose==1";
  cuts += "e1_reco_pt<100. && e2_reco_pt<100.";

  ///////////////////////////
  // Cuts and "N-1 plots" ...
  ///////////////////////////

  // Electron eta acceptance
  name = "e1_reco_eta";
  histo = new TH1F(name,name,100,-2.5,2.5);
  events->Draw(name+">>"+name,cuts);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");
  name = "e2_reco_eta";
  histo = new TH1F(name,name,100,-2.5,2.5);
  events->Draw(name+">>"+name,cuts);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");
  TCut e1_reco_eta = "TMath::Abs(e1_reco_eta)<1.2";
  TCut e2_reco_eta = "TMath::Abs(e2_reco_eta)<1.2";
  cuts += e1_reco_eta;
  cuts += e2_reco_eta;
  
  // Leading ele 
  name = "e1_reco_pt";
  histo = new TH1F(name,name,100,0.,50.);
  events->Draw(name+">>"+name,cuts);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");   
  TCut e1_reco_pt = "e1_reco_pt>5.";
  cuts += e1_reco_pt;
  
  // Sub-leading ele 
  name = "e2_reco_pt";
  histo = new TH1F(name,name,100,0.,50.);
  events->Draw(name+">>"+name,cuts);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");
  TCut e2_reco_pt = "e2_reco_pt>5.";
  cuts += e2_reco_pt;
  
  // J/psi candidate
  name = "mll";
  histo = new TH1F(name,name,100,0.,6.);
  events->Draw(name+">>"+name,cuts);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");
  TCut mll = "";
  if (rare==1) { mll = "mll>1.05 && mll<2.45"; }
  else         { mll = "mll>2.8 && mll<3.2"; } // 2.9 < mll < 3.2 ???
  cuts += mll;
  
  // Kaon
  name = "b_k_pt";
  histo = new TH1F(name,name,100,0.,20.);
  events->Draw(name+">>"+name,cuts);
  c1->SetLogy(0);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");
  TCut b_k_pt = "b_k_pt>1.";
  cuts += b_k_pt;
  
  // B mass (pre-sel)
  name = "b_mass_pre_sel";
  var = "b_mass";
  histo = new TH1F(name,name,50,4.7,5.7);
  events->Draw(var+">>"+name,cuts);
  c1->SetLogy(0);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");
  
  // cos2d
  name = "cos2d";
  histo = new TH1F(name,name,100,-1.,1.);
  events->Draw(name+">>"+name,cuts);
  c1->SetLogy(1);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");
  
  // SV prob
  name = "b_svprob";
  histo = new TH1F(name,name,1000,0.,1.);
  events->Draw(name+">>"+name,cuts);
  c1->SetLogy(1);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");
  
  // B pT
  name = "b_pt";
  histo = new TH1F(name,name,100,0.,50.);
  events->Draw(name+">>"+name,cuts);
  c1->SetLogy(0);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");
  
  // Lxysig
  name = "b_lxysig";
  var = "b_lxy/b_lxyerr";
  histo = new TH1F(name,name,100,0.,10.);
  events->Draw(var+">>"+name,cuts);
  c1->SetLogy(1);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");
  
//  // ip3d
//  name = "ip3d";
//  histo = new TH1F(name,name,100,-10.,10.);
//  events->Draw(name+">>"+name,cuts);
//  c1->SetLogy(1);
//  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");

  // BDT (pre-sel)
  name = "bdt_pre_sel";
  var = "bdt";
  histo = new TH1F(name,name,100,-20.,20.);
  events->Draw(var+">>"+name,cuts);
  c1->SetLogy(1);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");

  // Analysis selection (cut-based or BDT)
  //TCut bdt = "bdt>7.";
  TCut sel = "cos2d>0.8 && b_svprob>0.01 && b_pt > 15. && b_lxy/b_lxyerr>0.5 && bdt>8.";
  cuts += sel;
  
  std::cout << "TCut: " << cuts.GetTitle() << std::endl;

  // BDT (post-sel)
  name = "bdt_post_sel";
  var = "bdt";
  histo = new TH1F(name,name,100,-20.,20.);
  events->Draw(var+">>"+name,cuts);
  c1->SetLogy(1);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");
  
  // B mass (post-sel)
  name = "b_mass_post_sel";
  var = "b_mass";
  histo = new TH1F(name,name,50,4.7,5.7);
  events->Draw(var+">>"+name,cuts);
  c1->SetLogy(0);
  c1->SaveAs(dir+"plot_"+tag+"_"+sample+"_"+name+".pdf");
  
  f = TFile::Open(dir+"output_"+tag+"_"+sample+".root","RECREATE");
  histo->Write();
  f->Close();
  
}
