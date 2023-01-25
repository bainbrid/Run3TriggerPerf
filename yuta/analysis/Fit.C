#ifndef __CINT__
#include "RooGlobalFunc.h"
#endif
#include "RooAddPdf.h"
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

using namespace RooFit ;
using namespace RooStats ;

#define Exponential
#define Gaussian
//#define FixGaussianResolution
#define broadened
#define nominal_opositeSign_sameSign
//#define plotSameSign
//#define significance_likelihood_curve

//#define data2016
//#define data2017
//#define data2018
#define dataall
//#define datatest

void fit();
void Fit() { fit(); }
void fit() {

  gStyle->SetOptStat(0);
  gStyle->SetOptFit(0);

  Double_t Red[2]   = { 1.00, .00};
  Double_t Green[2] = { 1.00, .00};
  Double_t Blue[2]  = { 1.00, .00};
  Double_t Stops[2] = { .00, 1.00};

  Int_t nb=5;
  TColor::CreateGradientColorTable(2,Stops,Red,Green,Blue,nb);

  RooRealVar mass ("mass", "mass", 4., 7.);
  //RooRealVar mass ("mass", "mass", 4.5, 6.5);

  int Bc_bins  = 20;

  TFile *ntuple_data          = new TFile("ntupleOutput.root");

  TTree* tree_data          = (TTree*) ntuple_data->Get("tree");

  RooArgSet Variables(mass);

  RooDataSet *data          = new RooDataSet("data", "data", tree_data, Variables);

  TCut SelectionCut = "1.";

  RooDataSet *cut_data      = (RooDataSet*)data     ->reduce(SelectionCut);

  RooRealVar mean_m1  ("mean_m1","mean of gaussian", 5.279, 5.0, 6.0);
  //RooRealVar mean_m1  ("mean_m1","mean of gaussian", 5.279);
  RooRealVar sigma_m1 ("sigma_m1","Scale Factor 1",  0.1, 0.1, 0.15);
  //  RooRealVar width_m1 ("width_m1","Scale Factor 1",  0.2, 0.01, 0.15);
  RooRealVar alpha1("alpha1", "Alpha", 3.01542e+00);
  RooRealVar n1("n1", "Order", 5.13185e-01); //6,0.1,10);
  RooCBShape  mSig1   ("mSig1","signal p.d.f.", mass, mean_m1, sigma_m1,alpha1,n1);

  RooRealVar        c1("c1", "c1", -.5, -20., 0.);
  RooExponential mBkg1("mBkg1", "exponential", mass, c1);

  RooRealVar N_Jpsi1_S_Jpsi2_S_Jpsi3_S ("N_Jpsi1_S_Jpsi2_S_Jpsi3_S", "N_Jpsi1_S_Jpsi2_S_Jpsi3_S", 3);//10., 0., 10000.);
  RooRealVar N_Jpsi1_B_Jpsi2_B_Jpsi3_B ("N_Jpsi1_B_Jpsi2_B_Jpsi3_B", "N_Jpsi1_B_Jpsi2_B_Jpsi3_B", 10., 0., 1000.);

  RooExtendPdf e_Jpsi1_S_Jpsi2_S_Jpsi3_S ("e_Jpsi1_S_Jpsi2_S_Jpsi3_S", "e_Jpsi1_S_Jpsi2_S_Jpsi3_S", mSig1, N_Jpsi1_S_Jpsi2_S_Jpsi3_S);
  RooExtendPdf e_Jpsi1_B_Jpsi2_B_Jpsi3_B ("e_Jpsi1_B_Jpsi2_B_Jpsi3_B", "e_Jpsi1_B_Jpsi2_B_Jpsi3_B", mBkg1, N_Jpsi1_B_Jpsi2_B_Jpsi3_B);

  RooAddPdf eOniaSignal ("eOniaSignal", "eOniaSignal", RooArgList(e_Jpsi1_S_Jpsi2_S_Jpsi3_S, e_Jpsi1_B_Jpsi2_B_Jpsi3_B));

  RooFitResult *fr = eOniaSignal.fitTo(*cut_data, NumCPU(4, kTRUE), Save(), Extended());

  // plot
  RooPlot *frame_main_fit1 = mass.frame(Title("mass 1 fit"), Bins(Bc_bins));
  cut_data->plotOn(frame_main_fit1, XErrorSize(0), Name("plotdata"));
  eOniaSignal.plotOn(frame_main_fit1, Components(mSig1),LineColor(kWhite),DrawOption("F"),FillColor(kBlack),FillStyle(3004), Name("signalpdf"));
  eOniaSignal.plotOn(frame_main_fit1, LineColor(kBlack), Name("totalpdf"));
  cut_data->plotOn(frame_main_fit1, XErrorSize(0));
  TCanvas *c_mass_1 = new TCanvas("c_mass_1", "c_mass_1", 900, 900); c_mass_1->cd();
  frame_main_fit1->GetYaxis()->SetTitle("Events / 50 MeV");
  frame_main_fit1->GetXaxis()->SetNdivisions(504);
  frame_main_fit1->Draw();
//  TLatex *texZ_mumu = new TLatex();
//  texZ_mumu->SetTextSize(0.04);
//  texZ_mumu->DrawLatex(2.6, frame_main_fit1->GetMaximum()*1.01, "#bf{CMS} Preliminary" );
//#ifdef broadened
//  texZ_mumu->DrawLatex(3.5, frame_main_fit1->GetMaximum()*1.01, "137 fb^{-1} (13 TeV)" );
//  TLegend* massLeg_Jpsi = new TLegend(0.5, 0.75, 0.8, 0.9);
//#else
//  texZ_mumu->DrawLatex(2.95, frame_main_fit1->GetMaximum()*1.01, "137 fb^{-1} (13 TeV)" );
//  TLegend* massLeg_Jpsi = new TLegend(0.23, 0.7, 0.5, 0.9);
//#endif
//  massLeg_Jpsi->SetTextFont(62);
//  massLeg_Jpsi->SetTextSize(0.038);
//  massLeg_Jpsi->SetBorderSize(0);
//  massLeg_Jpsi->SetFillColor(0);
//  massLeg_Jpsi->AddEntry("plotdata", "Data", "ep");
//  massLeg_Jpsi->AddEntry("totalpdf", "Total", "l");
//  massLeg_Jpsi->AddEntry("signalpdf", "J/#psi signal", "f");
//  massLeg_Jpsi->Draw();


}
