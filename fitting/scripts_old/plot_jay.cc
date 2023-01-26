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

void plot_jay(){

    TFile* f = TFile::Open("./input/ntuples/jay/singlemudenominator20220901.root");

    TTree* events = (TTree*)f->Get("nano/tree");
    TString dir = "./plots/";
    
    TCanvas* c1 = new TCanvas("c1"); 
    TH1F* histo;
    TString name;
    TString var;

    // Initial cuts ...
    TCut cuts = "JpsiKE_e1_pt<100. && JpsiKE_e2_pt<100.";
    TCut e1_reco_eta = "TMath::Abs(JpsiKE_e1_eta)<1.2";
    TCut e2_reco_eta = "TMath::Abs(JpsiKE_e2_eta)<1.2";
    cuts += e1_reco_eta;
    cuts += e2_reco_eta;

    // N-1 plots ...

    // Leading ele 
    name = "e1_reco_pt";
    var = "JpsiKE_e1_pt";
    histo = new TH1F(name,name,100,0.,50.);
    events->Draw(var+">>"+name,cuts);
    c1->SaveAs(dir+name+".pdf");   
    TCut e1_reco_pt = "JpsiKE_e1_pt>4.";
    //cuts += e1_reco_pt;
    
    // Sub-leading ele 
    name = "e2_reco_pt";
    var = "JpsiKE_e2_pt";
    histo = new TH1F(name,name,100,0.,50.);
    events->Draw(var+">>"+name,cuts);
    c1->SaveAs(dir+name+".pdf");
    TCut e2_reco_pt = "JpsiKE_e2_pt>4.";
    //cuts += e2_reco_pt;

    // J/psi candidate
    name = "mll";
    var = "JpsiKE_Jpsi_mass_nofit";
    histo = new TH1F(name,name,100,0.,6.);
    events->Draw(var+">>"+name,cuts);
    c1->SaveAs(dir+name+".pdf");
    TCut mll = "JpsiKE_Jpsi_mass_nofit>2.9 && JpsiKE_Jpsi_mass_nofit<3.2";
    //TCut mll = "JpsiKE_Jpsi_mass_nofit>1.05 && JpsiKE_Jpsi_mass_nofit<2.45";
    cuts += mll;

    // Kaon
    name = "b_k_pt";
    var = "JpsiKE_pi_pt";
    histo = new TH1F(name,name,100,0.,20.);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(0);
    c1->SaveAs(dir+name+".pdf");
    TCut b_k_pt = "JpsiKE_pi_pt>2.";
    //cuts += b_k_pt;

    // cos2d
    name = "cos2d";
    var = "JpsiKE_B_alpha";
    histo = new TH1F(name,name,100,-1.,1.);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(1);
    c1->SaveAs(dir+name+".pdf");

    // ip3d
    name = "ip3d";
    var = "JpsiKE_B_lips";
    histo = new TH1F(name,name,100,-10.,10.);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(1);
    c1->SaveAs(dir+name+".pdf");

    // Lxysig
    name = "b_lxysig";
    var = "JpsiKE_B_fls3d";
    histo = new TH1F(name,name,100,0.,10.);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(1);
    c1->SaveAs(dir+name+".pdf");

    // SV prob
    name = "b_svprob";
    var = "JpsiKE_B_vprob";
    histo = new TH1F(name,name,100,0.,1.);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(1);
    c1->SaveAs(dir+name+".pdf");

    // B pT
    name = "b_pt";
    var = "JpsiKE_B_pt";
    histo = new TH1F(name,name,100,0.,50.);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(0);
    c1->SaveAs(dir+name+".pdf");

    // B mass
    name = "b_mass";
    var = "JpsiKE_B_mass_nofit";
    histo = new TH1F(name,name,30,4.5,6.0);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(0);
    c1->SaveAs(dir+name+".pdf");

    // B mass (corrected)
    name = "b_mass_corr";
    var = "JpsiKE_B_mass_corr";
    histo = new TH1F(name,name,30,4.5,6.0);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(0);
    c1->SaveAs(dir+name+".pdf");

    //TCut bdt = "bdt>7.";
    TCut bdt = "JpsiKE_pi_pt>2. && JpsiKE_B_alpha>0.8 && JpsiKE_B_vprob>0.01 && JpsiKE_B_fls3d>0.";
    cuts += bdt;

    // Kaon (post cuts)
    name = "b_k_pt_post_cuts";
    var = "JpsiKE_pi_pt";
    histo = new TH1F(name,name,100,0.,20.);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(1);
    c1->SaveAs(dir+name+".pdf");

    //TCut b_k_pt = "b_k_pt>4.";
    //cuts += b_k_pt;

    std::cout << "TCut: " << cuts.GetTitle() << std::endl;

    // B mass (post cuts)
    name = "b_mass_post_cuts";
    var = "JpsiKE_B_mass_nofit";
    histo = new TH1F(name,name,30,4.5,6.0);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(0);
    c1->SaveAs(dir+name+".pdf");

    // B mass (corrected, post cuts)
    name = "b_mass_corr_post_cuts";
    var = "JpsiKE_B_mass_corr";
    histo = new TH1F(name,name,30,4.5,6.0);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(0);
    c1->SaveAs(dir+name+".pdf");

    f = TFile::Open(dir+"output.root","RECREATE");
    histo->Write();
    f->Close();

}
