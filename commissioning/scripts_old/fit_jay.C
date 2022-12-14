// signal histo ===> "bg_res"
//
// please fit data_obs with parameterized signal histo + whatever function you want

#ifndef __CINT__
#include "RooGlobalFunc.h"
#endif
#include "RooAddPdf.h"
#include "RooAbsReal.h"
#include "RooBinning.h"
#include "RooCBShape.h"
#include "RooCategory.h"
#include "RooChebychev.h"
#include "RooConstVar.h"
#include "RooDLLSignificanceMCSModule.h"
#include "RooDataHist.h"
#include "RooDataSet.h"
#include "RooDecay.h"
#include "RooErrorVar.h"
#include "RooExponential.h"
#include "RooExtendPdf.h"
#include "RooFFTConvPdf.h"
#include "RooFitResult.h"
#include "RooFormulaVar.h"
#include "RooGaussModel.h"
#include "RooGaussian.h"
#include "RooGenericPdf.h"
#include "RooHist.h"
#include "RooHistPdf.h"
#include "RooMCStudy.h"
#include "RooNLLVar.h"
#include "RooNumConvPdf.h"
#include "RooLandau.h"
#include "RooPlot.h"
#include "RooPolynomial.h"
#include "RooProdPdf.h"
#include "RooProfileLL.h"
#include "RooRealVar.h"
#include "RooSimultaneous.h"
#include "RooStats/HypoTestResult.h"
#include "RooStats/LikelihoodIntervalPlot.h"
#include "TColor.h"
#include "TString.h"
#include "RooStats/MaxLikelihoodEstimateTestStat.h"
#include "RooStats/ModelConfig.h"
#include "RooStats/NumberCountingPdfFactory.h"
#include "RooStats/ProfileLikelihoodCalculator.h"
#include "RooStats/RatioOfProfiledLikelihoodsTestStat.h"
#include "RooStats/SPlot.h"
#include "RooVoigtian.h"
#include "RooWorkspace.h"
#include "RooArgusBG.h"
#include "TArrow.h"
#include "TAxis.h"
#include "TCanvas.h"
#include "TCut.h"
#include "TF1.h"
#include "TFile.h"
#include "TGraph.h"
#include "TH1D.h"
#include "TH3.h"
#include "TLatex.h"
#include "TLegend.h"
#include "TMath.h"
#include "TPaveLabel.h"
#include "TRandom3.h"
#include "TStyle.h"
#include "TTree.h"
#include "RooKeysPdf.h"
#include "RooNDKeysPdf.h"
#include <string>
#include <cmath>
#include <iostream>
#include <sstream>

#define DrawResiduals

using namespace RooFit ;
using namespace RooStats ;

//void fit_jpsik();
//void Fit_jpsik() { fit_jpsik(); }
void fit() {

  gStyle->SetOptStat(0);
  gStyle->SetOptFit(0);

  TF1 *f_straighline = new TF1("f_straighline", "0", 0, 1000);
  f_straighline->SetLineColor(kBlack);
  TF1 *f_1 = new TF1("f_1", "1", 0, 116);  f_1->SetLineColor(kBlue); f_1->SetLineStyle(7);
  TF1 *f_2 = new TF1("f_2", "-1", 0, 116); f_2->SetLineColor(kBlue); f_2->SetLineStyle(7);

  RooRealVar mass("b_mass", "Mass [J/#psiK] [GeV]", 4.700, 5.7);

  int Bc_bins = 50;

  TFile *ntuple_mc = new TFile("./output/slimmed/2022Oct12/slimmed_2022Oct12_BuToKJpsi_Toee.root"); 

  TTree* tree_mc   = (TTree*) ntuple_mc->Get("tree");

  RooArgSet Variables(mass); 

  RooDataSet *mc          = new RooDataSet("mc", "mc", tree_mc, Variables); //, puweight.GetName());

  TCut SelectionCut = "1";

  RooDataSet *cut_mc    = (RooDataSet*)mc   ->reduce(SelectionCut);

  // exponential
  RooRealVar        c0("c0", "c0", -.5, -40., 0.);
  RooExponential mBkg0("mBkg0", "exponential", mass, c0);
  RooRealVar N_mBkg0 ("N_mBkg0", "N_mBkg0", 10000., 0., 100000000.);
  RooExtendPdf e_mBkg0 ("e_mBkg0", "e_mBkg0", mBkg0, N_mBkg0);

  //Error Function1
  RooRealVar ErfSlope ("ErfSlope", "Erf Slope", 5., 2., 10.);
  RooRealVar meanErf ("meanErf", "mean of the Erf gaussian", 5.224, 5.100, 5.30);  //5300
  RooRealVar sigmaErf ("sigmaErf", "width of the Erf gaussian", 0.0386, 0.010, 0.040); // 200
  RooRealVar ErfOffset ("ErfOffset", "Offset of Erf exponential", 5.100, 5.000, 5.200); //4930.
  RooGenericPdf Erf("Erf", "Error Function", "TMath::Exp(TMath::Abs(ErfSlope)*(b_mass-ErfOffset))*TMath::Erfc((b_mass-meanErf)/sigmaErf)", RooArgSet(mass, meanErf, sigmaErf,ErfSlope,ErfOffset));
//  RooGenericPdf Erf("Erf", "Error Function", "TMath::Erfc((mass-meanErf)/sigmaErf)", RooArgSet(mass, meanErf, sigmaErf, ErfOffset));

  RooRealVar N_Erf ("N_Erf", "N_Erf", 30000, 0, 10000000);
  RooExtendPdf e_Erf ("e_Erf", "e_Erf", Erf, N_Erf);

  // signal
  RooRealVar mean_m  ("mean_m","mean of gaussian", 5.2749, 5.26, 5.3);
  RooRealVar sigma_m ("sigma_m","Scale Factor 1",  0.034, 0.01, 0.040);
  RooGaussian mSig1   ("mSig1","signal p.d.f.", mass, mean_m, sigma_m);
  RooRealVar sigma_m2 ("sigma_m2","Scale Factor 1",  0.08, 0.0, 0.2);
  RooGaussian mSig2   ("mSig2","signal p.d.f.", mass, mean_m, sigma_m2);
  RooRealVar frac ("frac", "frac", 0.8, 0., 1);

  RooRealVar sigma_cb ("sigma_cb","Scale Factor 1", 0.034, 0.02, 0.075);
  RooRealVar alpha("alpha", "Alpha", 1.2); //5,0.1,10);
  RooRealVar n("n", "Order", 10);//6,0.1,10);
  RooCBShape  mSig3   ("mSig3","signa p.d.f.", mass, mean_m, sigma_cb, alpha,n);

  RooAddPdf mSig ("mSig", "mSig", RooArgList(mSig1, mSig3), frac);
  RooRealVar N_mSig  ("N_mSig", "N_mSig", 80000., 0., 1000000000.);
  RooExtendPdf e_mSig ("e_mSig", "e_mSig", mSig, N_mSig);

  RooRealVar frac1 ("frac1", "frac1", 0.1, 0., 1.);
  RooRealVar frac2 ("frac2", "frac2", 0.1, 0., 1.);

  RooRealVar signalYield ("signalYield", "signalYield", 100000, 0, 100000000);
  RooAddPdf total ("total", "total", RooArgSet(e_mBkg0, e_mSig, e_Erf));

  RooFitResult *fr = total.fitTo(*cut_mc, NumCPU(4, kTRUE), Save(), Extended());

  // plot
  RooPlot *frame_main_fit1 = mass.frame(Title("J/#psi(ee)K Candidate Mass ~4.58 (/fb) ParkingDoubleElectronLowMass"), Bins(Bc_bins));
  Int_t cerf = 1756;
  Int_t csig = 1757;
  Int_t cexp = 1758;

  TColor *colorerf = new TColor(cerf, 27./255.,158./255.,119./255.);
  TColor *colorsig = new TColor(csig,  217./255.,95./255.,2./255.);
  TColor *colorexp = new TColor(cexp,  117./255.,112./255.,179./255.);


  cut_mc->plotOn(frame_main_fit1, XErrorSize(0), Name("plotmc"));
  total.plotOn(frame_main_fit1, LineColor(kAzure+1), Name("totalpdf"));
  total.plotOn(frame_main_fit1, Components("e_mBkg0"),DrawOption("FL"), LineColor(kAzure+8),FillColor(1758),FillStyle(1004),Name("bkg"));
  total.plotOn(frame_main_fit1, Components(e_mSig),DrawOption("FL"), LineColor(kAzure+5),FillColor(1757),FillStyle(1004),Name("signal"));
  total.plotOn(frame_main_fit1, Components("e_Erf"),DrawOption("FL"), LineColor(kAzure+10),FillColor(1756),FillStyle(1004),Name("erf"));
  frame_main_fit1->GetXaxis()->SetLabelSize(0.05);

  frame_main_fit1->GetXaxis()->SetTitleSize(0.05);
  cut_mc->plotOn(frame_main_fit1, XErrorSize(0));

  TCanvas *c_mass_1 = new TCanvas("c_mass_1", "c_mass_1", 800, 800); //c_mass_1->Divide(2,2);
#ifdef DrawResiduals
  frame_main_fit1->GetXaxis()->SetLabelSize(0.0);

  frame_main_fit1->GetXaxis()->SetTitleSize(0.0);

  RooPlot* dummy_frame_Z = mass.frame(Title("dummy frame to sdfsdfdsfsextract residuals"), Bins(Bc_bins));
  cut_mc->plotOn(dummy_frame_Z,XErrorSize(0));
  total.plotOn(dummy_frame_Z);

  RooHist* h_residuals_mass = dummy_frame_Z->pullHist();
  RooPlot* frame_residuals_mass_Z = mass.frame(Title("asdad"),Bins(Bc_bins));
  frame_residuals_mass_Z->GetYaxis()->SetTitle("Pull"); //(fit - data)/#sigma");
  frame_residuals_mass_Z->GetYaxis()->CenterTitle(true); //(fit - data)/#sigma");
  frame_residuals_mass_Z->GetYaxis()->SetTitleSize(0.1);
  frame_residuals_mass_Z->GetYaxis()->SetLabelSize(.1);
  frame_residuals_mass_Z->GetYaxis()->SetTitleOffset(0.25);
  frame_residuals_mass_Z->GetYaxis()->SetNdivisions(5);
  frame_residuals_mass_Z->addPlotable(h_residuals_mass, "P");
  frame_residuals_mass_Z->SetTitle("");
  frame_residuals_mass_Z->GetXaxis()->SetLabelSize(0.1);
  frame_residuals_mass_Z->GetXaxis()->SetTitleSize(0.1);


  TPad *pad1 = new TPad("pad1","pad1",0,0.22,1,1);
  TPad *pad2 = new TPad("pad2","pad2",0,0,1,0.22);
  pad1->SetFillColor(0); pad2->SetFillColor(0);
  pad1->SetBottomMargin(0.02);
  pad1->SetBorderMode(0);
  pad2->SetTopMargin(0.);
  pad2->SetBottomMargin(0.3);
  pad2->SetBorderMode(0);
  pad1->Draw();
  pad2->Draw();
  pad2->cd(); frame_residuals_mass_Z->Draw(); f_straighline->Draw("same"); //f_1->Draw("same"); f_2->Draw("same");
  pad1->cd();
#endif
  frame_main_fit1->GetXaxis()->SetNdivisions(504);
  frame_main_fit1->Draw(); //c_mass_1->cd(1)->SetLogy(1);
  c_mass_1->SaveAs("output/plots/canvas_mass.pdf");

  mass.setRange("signal3", mean_m.getVal() - 2*sigma_cb.getVal(),mean_m.getVal() + 2*sigma_cb.getVal()) ;
  //mass.setRange("signal3", 5.3,5.5) ;

  RooAbsReal* signalregionfraction = e_mSig.createIntegral(mass,NormSet(mass), Range("signal3")) ; cout << "first integral: "<< signalregionfraction->getVal()<<"=="<<N_mSig.getVal()<<"==" << cut_mc->sumEntries() << endl; 
  RooAbsReal* totalregionfraction = total.createIntegral(mass,NormSet(mass), Range("signal3")); cout<<"secondintetgr4gal == "<<totalregionfraction->getVal()<<endl;
  cout<<"hhe"<<mc->sumEntries()<<endl;
  cout<<total.getVal()<<endl;
  TLatex *texZ_mumu = new TLatex();
  texZ_mumu->SetTextSize(0.04);
  //texZ_mumu->DrawLatex(2.6, frame_main_fit1->GetMaximum()*1.01, "#bf{CMS} Preliminary" );
#ifdef broadened
  //texZ_mumu->DrawLatex(3.5, frame_main_fit1->GetMaximum()*1.01, "137 fb^{-1} (13 TeV)" );
  TLegend* massLeg_Jpsi = new TLegend(0.5, 0.75, 0.8, 0.9);
#else
  texZ_mumu->DrawLatex(2.95, frame_main_fit1->GetMaximum()*1.01, "137 fb^{-1} (13 TeV)" );
  TLegend* massLeg_Jpsi = new TLegend(0.23, 0.7, 0.5, 0.9);
#endif
  int rounded_nearest = std::roundf(N_mSig.getVal());
  std::string s1 = std::to_string(rounded_nearest);
  std::string soverb =std::to_string((signalregionfraction->getVal()*N_mSig.getVal())/TMath::Sqrt((totalregionfraction->getVal()*mc->sumEntries())));
  std::string soberb =std::to_string((signalregionfraction->getVal()*N_mSig.getVal())/(totalregionfraction->getVal()*mc->sumEntries()-signalregionfraction->getVal()*N_mSig.getVal()));
  TString s(s1);
  TString sb(soverb);
  TString soberbstr(soberb);
  TString tt(std::to_string(mc->sumEntries()));
  massLeg_Jpsi->SetTextFont(42);
  massLeg_Jpsi->SetTextSize(0.038);
  massLeg_Jpsi->SetBorderSize(0);
  massLeg_Jpsi->SetFillColor(0);
  massLeg_Jpsi->AddEntry("plotmc", "Data", "ep");
  massLeg_Jpsi->AddEntry("totalpdf", "Total", "l");
  massLeg_Jpsi->AddEntry("signal", "B+- Signal Nsig = "+s, "f");
  massLeg_Jpsi->AddEntry("erf", "Combinatorial background", "f");
  massLeg_Jpsi->AddEntry("bkg", "exp background", "f");
  massLeg_Jpsi->AddEntry("","S/#sqrt{S+B} in signal region ( 2 #sigma ) =  "+sb,"");
  massLeg_Jpsi->AddEntry("","S/B in signal region ( 2 #sigma ) =  "+soberbstr,"");

  //massLeg_Jpsi->AddEntry("","Total Entries =  "+tt,"");


  massLeg_Jpsi->Draw();

}
