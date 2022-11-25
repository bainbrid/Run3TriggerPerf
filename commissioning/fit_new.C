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
#include "RooCrystalBall.h"
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

//using namespace RooFit ;
//using namespace RooStats ;

void fit_new() {

  ////////////////////////////////////////////////////////////////////////////////
  // OPTIONS
  
  //TString tag = "2022Sep05";
  TString tag = "2022Oct12";

  //TString sample = "Run2022_Jpsi";
  //TString sample = "Run2022D_rare";
  
  //TString sample = "Run2022";
  //TString sample = "Run2022_riccardo";
  //TString sample = "Run2022_rare_riccardo";
  //TString sample = "Run2022_Psi2S";

  TString sample = "BuToKJpsi_Toee";
  //TString sample = "BuToKPsi2S_Toee";
  //TString sample = "BuToKee";

  TString var = "b_mass";
  
#define isMC // switch off bkgd shapes
  //#define isRARE // rare vs J/psi
  //#define isPsi2S // rare vs J/psi
  
#ifdef isRARE
  int Bc_bins = 20;
#else
#ifdef isPsi2S
  int Bc_bins = 75;
#else
  int Bc_bins = 75;
#endif
#endif
  
////////////////////////////////////////////////////////////////////////////////

  gStyle->SetOptStat(0);
  gStyle->SetOptFit(0);

  TF1 *f_straighline = new TF1("f_straighline", "0", 0, 1000);
  f_straighline->SetLineColor(kBlack);
  TF1 *f_1 = new TF1("f_1", "1", 0, 116);  f_1->SetLineColor(kBlue); f_1->SetLineStyle(7);
  TF1 *f_2 = new TF1("f_2", "-1", 0, 116); f_2->SetLineColor(kBlue); f_2->SetLineStyle(7);
  
  RooRealVar mass(var, "Mass [GeV]", 4.7, 5.7);

  TFile *ntuple_mc = new TFile("./output/slimmed/"+tag+"/slimmed_"+tag+"_"+sample+".root"); 

  TTree* tree_mc   = (TTree*) ntuple_mc->Get("tree");

  RooArgSet Variables(mass); 

  RooDataSet *mc          = new RooDataSet("mc", "mc", tree_mc, Variables); //, puweight.GetName());

  TCut SelectionCut = "1";

  RooDataSet *cut_mc    = (RooDataSet*)mc   ->reduce(SelectionCut);

  // Combinatorial bkgd
  RooRealVar        c0("c0", "c0", -.5, -40., 0.);
  RooExponential mBkg0("mBkg0", "exponential", mass, c0);
  RooRealVar N_mBkg0 ("N_mBkg0", "N_mBkg0", 10000., 0., 100000000.);
  RooExtendPdf e_mBkg0 ("e_mBkg0", "e_mBkg0", mBkg0, N_mBkg0);

  // Partially reco'ed bkgd
  RooRealVar ErfSlope ("ErfSlope", "Erf Slope", 2.25, 2., 3.);
  RooRealVar meanErf ("meanErf", "mean of the Erf gaussian", 5.2, 5.15, 5.25);  //5300
  RooRealVar sigmaErf ("sigmaErf", "width of the Erf gaussian", 0.03, 0.025, 0.035); // 200
  RooRealVar ErfOffset ("ErfOffset", "Offset of Erf exponential", 5.15, 5.1, 5.2); //4930.
  RooGenericPdf Erf("Erf", "Error Function", "TMath::Exp(TMath::Abs(ErfSlope)*("+var+"-ErfOffset))*TMath::Erfc(("+var+"-meanErf)/sigmaErf)", RooArgSet(mass, meanErf, sigmaErf,ErfSlope,ErfOffset));
  RooRealVar N_Erf ("N_Erf", "N_Erf", 30000, 0, 10000000);
  RooExtendPdf e_Erf ("e_Erf", "e_Erf", Erf, N_Erf);

//  // Signal (Gaus)
//  RooRealVar mean_m  ("mean_m","mean of gaussian", 5.27, 5.27, 5.27); // fixed @ J/psi
//  RooRealVar sigma_m ("sigma_m","Scale Factor 1",  0.15, 0.15, 0.15); // fixed @ J/psi
//  RooGaussian mSig1   ("mSig1","signal p.d.f.", mass, mean_m, sigma_m);
  
//  // Signal (CB)
//  RooRealVar sigma_cb ("sigma_cb","Scale Factor 1", 0.05, 0.05, 0.05); // fixed @ J/psi
//  RooRealVar alpha("alpha", "Alpha", 1.2); //5,0.1,10);
//  RooRealVar n("n", "Order", 10);//6,0.1,10);
//  RooCBShape  mSig3   ("mSig3","signa p.d.f.", mass, mean_m, sigma_cb, alpha,n);

//  // Signal (Gaus vs CB)
//  RooRealVar frac ("frac", "frac", 0., 0., 0.); // fixed @ J/psi

//  // Combine PDFs
//  RooAddPdf mSig ("mSig", "mSig", RooArgList(mSig1, mSig3), frac);
//  RooRealVar N_mSig  ("N_mSig", "N_mSig", 80000., 0., 1000000000.);
//  RooExtendPdf e_mSig ("e_mSig", "e_mSig", mSig, N_mSig);


  // Hack - include Gaus but set frac to zero (i.e. no contribution)
  //RooRealVar mean_m("mean_m","mu",5.27,4.7,5.7); // open
  //RooRealVar sigma_m("sigma_m","width",0.1,0.,1.); // open
#ifdef isRARE
  RooRealVar mean_m("mean_m","mu",5.27); // fixed @ low q2
  RooRealVar sigma_m("sigma_m","width",0.); // fixed @ low q2
#else
#ifdef isPsi2S
  RooRealVar mean_m("mean_m","mu",5.27); // fixed @ Psi2S
  RooRealVar sigma_m("sigma_m","width",0.); // fixed @ Psi2S
#else
  RooRealVar mean_m("mean_m","mu",5.27); // fixed @ J/psi
  RooRealVar sigma_m("sigma_m","width",0.); // fixed @ J/psi
#endif
#endif
  RooGaussian mSig1("mSig1","signal p.d.f.", mass, mean_m, sigma_m);

  // Signal (double-sided CB)
  //RooRealVar sigma_cb("sigma_cb","width",0.0578,0.,1.); // open
  //RooRealVar a1("a1","a1",0.815,0.,100.); // open
  //RooRealVar p1("p1","p1",100.,0.,1000.); // open
  //RooRealVar a2("a2","a2",3.111,0.,100.); // open
  //RooRealVar p2("p2","p2",2.01,0.,100.); // open
#ifdef isRARE
  RooRealVar sigma_cb("sigma_cb","width",0.0509); // fixed @ low q2
  RooRealVar a1("a1","a1",0.920); // fixed @ low q2
  RooRealVar p1("p1","p1",1.26); // fixed @ low q2
  RooRealVar a2("a2","a2",1.86); // fixed @ low q2
  RooRealVar p2("p2","p2",3.20); // fixed @ low q2
#else
#ifdef isPsi2S
  RooRealVar sigma_cb("sigma_cb","width",0.0633); // fixed @ Psi(2S)
  RooRealVar a1("a1","a1",2.08); // fixed @ Psi(2S)
  RooRealVar p1("p1","p1",132.); // fixed @ Psi(2S)
  RooRealVar a2("a2","a2",3.27); // fixed @ Psi(2S)
  RooRealVar p2("p2","p2",2.27); // fixed @ Psi(2S)
#else
  RooRealVar sigma_cb("sigma_cb","width",0.0577); // fixed @ J/psi
  RooRealVar a1("a1","a1",0.819); // fixed @ J/psi
  RooRealVar p1("p1","p1",130.); // fixed @ J/psi
  RooRealVar a2("a2","a2",3.10); // fixed @ J/psi
  RooRealVar p2("p2","p2",2.04); // fixed @ J/psi
#endif
#endif
  RooCrystalBall mSig3("dcbPdf","DoubleSidedCB",mass,mean_m,sigma_cb,a1,p1,a2,p2);

  // Signal (Gaus vs CB)
 RooRealVar frac ("frac", "frac", 0., 0., 0.); // fixed to zero for all 

  //RooAddPdf mSig ("mSig", "mSig", RooArgList(mSig3));
  RooAddPdf mSig ("mSig", "mSig", RooArgList(mSig1, mSig3), frac);
  RooRealVar N_mSig  ("N_mSig", "N_mSig", 80000., 0., 1000000000.);
  RooExtendPdf e_mSig ("e_mSig", "e_mSig", mSig, N_mSig);
  
  // Total shape
#ifdef isMC
  RooAddPdf total("total", "total", RooArgSet(e_mSig));
#else
  RooAddPdf total("total", "total", RooArgSet(e_mBkg0, e_mSig, e_Erf));
#endif
  RooFitResult *fr = total.fitTo(*cut_mc, RooFit::NumCPU(4, kTRUE), RooFit::Save(), RooFit::Extended());

  // plot
  //RooPlot *frame_main_fit1 = mass.frame(Title("J/#psi(ee)K Candidate Mass ~4.58 (/fb) ParkingDoubleElectronLowMass"), Bins(Bc_bins));
  RooPlot *frame_main_fit1 = mass.frame(RooFit::Title(" "), RooFit::Bins(Bc_bins));
  Int_t cerf = 1756;
  Int_t csig = 1757;
  Int_t cexp = 1758;

  TColor *colorerf = new TColor(cerf, 27./255.,158./255.,119./255.);
  TColor *colorsig = new TColor(csig,  217./255.,95./255.,2./255.);
  TColor *colorexp = new TColor(cexp,  117./255.,112./255.,179./255.);

  cut_mc->plotOn(frame_main_fit1, RooFit::XErrorSize(0), RooFit::Name("plotmc"));
  total.plotOn(frame_main_fit1, RooFit::LineColor(kAzure+1), RooFit::Name("totalpdf"));
#ifndef isMC
  total.plotOn(frame_main_fit1, RooFit::Components("e_mBkg0"),RooFit::DrawOption("FL"), RooFit::LineColor(kAzure+8),RooFit::FillColor(1758),RooFit::FillStyle(1004),RooFit::Name("bkg"));
#endif
  total.plotOn(frame_main_fit1, RooFit::Components(e_mSig),RooFit::DrawOption("FL"), RooFit::LineColor(kAzure+5),RooFit::FillColor(1757),RooFit::FillStyle(1004),RooFit::Name("signal"));
#ifndef isMC
  total.plotOn(frame_main_fit1, RooFit::Components("e_Erf"),RooFit::DrawOption("FL"), RooFit::LineColor(kAzure+10),RooFit::FillColor(1756),RooFit::FillStyle(1004),RooFit::Name("erf"));
#endif
  frame_main_fit1->GetXaxis()->SetLabelSize(0.05);

  frame_main_fit1->GetXaxis()->SetTitleSize(0.05);
  cut_mc->plotOn(frame_main_fit1, RooFit::XErrorSize(0));

  TCanvas *c_mass_1 = new TCanvas("c_mass_1", "c_mass_1", 800, 800); //c_mass_1->Divide(2,2);
#ifdef DrawResiduals
  frame_main_fit1->GetXaxis()->SetLabelSize(0.0);

  frame_main_fit1->GetXaxis()->SetTitleSize(0.0);

  RooPlot* dummy_frame_Z = mass.frame(RooFit::Title("dummy frame to sdfsdfdsfsextract residuals"), RooFit::Bins(Bc_bins));
  cut_mc->plotOn(dummy_frame_Z,RooFit::XErrorSize(0));
  total.plotOn(dummy_frame_Z);

  RooHist* h_residuals_mass = dummy_frame_Z->pullHist();
  RooPlot* frame_residuals_mass_Z = mass.frame(RooFit::Title("asdad"),RooFit::Bins(Bc_bins));
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
  pad2->SetRightMargin(0.1);
  pad2->SetBottomMargin(0.3);
  pad2->SetBorderMode(0);
  pad1->Draw();
  pad2->Draw();
  pad2->cd(); frame_residuals_mass_Z->Draw(); f_straighline->Draw("same"); //f_1->Draw("same"); f_2->Draw("same");
  pad1->cd();
#endif
  frame_main_fit1->GetXaxis()->SetNdivisions(504);
  frame_main_fit1->Draw(); //c_mass_1->cd(1)->SetLogy(1);
  //c_mass_1->SaveAs("plots/canvas_mass.pdf");

  mass.setRange("signal3", mean_m.getVal() - 2.*sigma_cb.getVal(),mean_m.getVal() + 2.*sigma_cb.getVal()) ;
  //mass.setRange("signal3", 5.3,5.5) ;
  
  RooAbsReal* signalregionfraction = e_mSig.createIntegral(mass,RooFit::NormSet(mass), RooFit::Range("signal3")) ;
  cout << "e_mSig.createIntegral: "<< signalregionfraction->getVal()<<endl;
  cout <<"N_mSig: "<<N_mSig.getVal()<<endl;
  cout << "cut_mc->sumEntries(): "<<cut_mc->sumEntries() << endl; 
  RooAbsReal* totalregionfraction = total.createIntegral(mass,RooFit::NormSet(mass), RooFit::Range("signal3"));
  cout<<"total.createIntegral: "<<totalregionfraction->getVal()<<endl;
  cout<<"mc->sumEntries(): "<<mc->sumEntries()<<endl;
  cout<<"total.getVal(): "<<total.getVal()<<endl;
  TLatex *texZ_mumu = new TLatex();
  texZ_mumu->SetTextSize(0.04);
  //texZ_mumu->DrawLatex(2.6, frame_main_fit1->GetMaximum()*1.01, "#bf{CMS} Preliminary" );
#ifdef broadened
  //texZ_mumu->DrawLatex(3.5, frame_main_fit1->GetMaximum()*1.01, "137 fb^{-1} (13 TeV)" );
  TLegend* massLeg_Jpsi = new TLegend(0.5, 0.75, 0.8, 0.9);
#else
  texZ_mumu->DrawLatex(2.95, frame_main_fit1->GetMaximum()*1.01, "137 fb^{-1} (13 TeV)" );
  TLegend* massLeg_Jpsi = new TLegend(0.65, 0.65, 0.88, 0.88);
#endif
  int rounded_nearest = std::roundf(N_mSig.getVal());
  std::string s1 = std::to_string(rounded_nearest);
  int b_rounded = std::roundf(e_mSig.getVal());
  std::string serr = std::to_string(b_rounded);
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
  massLeg_Jpsi->AddEntry("totalpdf", "S+B shape", "l");
  massLeg_Jpsi->AddEntry("signal", "Signal ("+s+")", "f");
  //massLeg_Jpsi->AddEntry("signal", "Signal ("+s+"#pm"+TString(serr)+")", "f");
  massLeg_Jpsi->AddEntry("erf", "Bkgd (part.)", "f");
  massLeg_Jpsi->AddEntry("bkg", "Bkgd (comb.)", "f");
  //massLeg_Jpsi->AddEntry("","S/#sqrt{S+B}(2#sigma):"+sb,"");
  //massLeg_Jpsi->AddEntry("","S/B(2#sigma):"+soberbstr,"");

  //massLeg_Jpsi->AddEntry("","Total Entries =  "+tt,"");


  massLeg_Jpsi->Draw();
  c_mass_1->SaveAs("./output/plots/"+tag+"/fitted_"+tag+"_"+sample+"_"+var+".pdf");

}
