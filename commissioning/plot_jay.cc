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

void peak(){

    TFile* f = TFile::Open("./data/data_2022Aug24.root");
    TTree* events = (TTree*)f->Get("tree");
    TString dir = "./plots/";
    
    TCanvas* c1 = new TCanvas("c1"); 
    TH1F* histo;
    TString name;
    TString var;

    // Initial cuts ...
    TCut cuts = "e1_reco_pt<50. && e2_reco_pt<50.";
    TCut e1_reco_eta = "TMath::Abs(e1_reco_eta)<1.2";
    TCut e2_reco_eta = "TMath::Abs(e2_reco_eta)<1.2";
    cuts += e1_reco_eta;
    cuts += e2_reco_eta;

    // N-1 plots ...

    // Leading ele 
    name = "e1_reco_pt";
    histo = new TH1F(name,name,100,0.,50.);
    events->Draw(name+">>"+name,cuts);
    c1->SaveAs(dir+name+".pdf");   
    TCut e1_reco_pt = "e1_reco_pt>4.";
    cuts += e1_reco_pt;
    
    // Sub-leading ele 
    name = "e2_reco_pt";
    histo = new TH1F(name,name,100,0.,50.);
    events->Draw(name+">>"+name,cuts);
    c1->SaveAs(dir+name+".pdf");
    TCut e2_reco_pt = "e2_reco_pt>4.";
    cuts += e2_reco_pt;

    // J/psi candidate
    name = "mll";
    histo = new TH1F(name,name,100,0.,6.);
    events->Draw(name+">>"+name,cuts);
    c1->SaveAs(dir+name+".pdf");
    TCut mll = "mll>2.9 && mll<3.2";
    //TCut mll = "mll>1.05 && mll<2.45";
    cuts += mll;

    // Kaon
    name = "b_k_pt";
    histo = new TH1F(name,name,100,0.,20.);
    events->Draw(name+">>"+name,cuts);
    c1->SetLogy(1);
    c1->SaveAs(dir+name+".pdf");
    //TCut b_k_pt = "b_k_pt>8.";
    //cuts += b_k_pt;

    // cos2d
    name = "cos2d";
    histo = new TH1F(name,name,100,-1.,1.);
    events->Draw(name+">>"+name,cuts);
    c1->SetLogy(1);
    c1->SaveAs(dir+name+".pdf");

    // ip3d
    name = "ip3d";
    histo = new TH1F(name,name,100,-10.,10.);
    events->Draw(name+">>"+name,cuts);
    c1->SetLogy(1);
    c1->SaveAs(dir+name+".pdf");

    // Lxysig
    name = "b_lxysig";
    var = "b_lxy/b_lxyerr";
    histo = new TH1F(name,name,100,0.,10.);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(1);
    c1->SaveAs(dir+name+".pdf");

    // SV prob
    name = "b_svprob";
    histo = new TH1F(name,name,1000,0.,1.);
    events->Draw(name+">>"+name,cuts);
    c1->SetLogy(0);
    c1->SaveAs(dir+name+".pdf");

    // B pT
    name = "b_pt";
    histo = new TH1F(name,name,100,0.,50.);
    events->Draw(name+">>"+name,cuts);
    c1->SetLogy(0);
    c1->SaveAs(dir+name+".pdf");

    // BDT
    name = "bdt";
    histo = new TH1F(name,name,100,-20.,20.);
    events->Draw(name+">>"+name,cuts);
    c1->SetLogy(1);
    c1->SaveAs(dir+name+".pdf");

    // B mass
    name = "b_mass";
    histo = new TH1F(name,name,15,4.5,6.0);
    events->Draw(name+">>"+name,cuts);
    c1->SetLogy(0);
    c1->SaveAs(dir+name+".pdf");

    //TCut bdt = "bdt>7.";
    TCut bdt = "b_svprob>0.1 && b_lxy/b_lxyerr>3. && cos2d>0.99 && b_k_pt>4. && bdt>5.";
    cuts += bdt;

    // Kaon (post BDT)
    name = "b_k_pt_post_bdt";
    var = "b_k_pt";
    histo = new TH1F(name,name,100,0.,20.);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(1);
    c1->SaveAs(dir+name+".pdf");

    //TCut b_k_pt = "b_k_pt>4.";
    //cuts += b_k_pt;

    std::cout << "TCut: " << cuts.GetTitle() << std::endl;

    // B mass (post BDT)
    name = "b_mass_post_bdt";
    var = "b_mass";
    histo = new TH1F(name,name,15,4.5,6.0);
    events->Draw(var+">>"+name,cuts);
    c1->SetLogy(0);
    c1->SaveAs(dir+name+".pdf");

    f = TFile::Open(dir+"output.root","RECREATE");
    histo->Write();
    f->Close();

}
