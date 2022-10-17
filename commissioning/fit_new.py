import ROOT
import math

def fit_new() :
  
  ################################################################################
  # FITTING TO THE DATA

  # Style
  ROOT.gStyle.SetOptStat(0)
  ROOT.gStyle.SetOptFit(0)

  input_path = "./slimmed/"+tag+"/slimmed_"+tag+"_"+sample+".root"
  input_file = ROOT.TFile(input_path,"READ")
  tree = input_file.Get("tree")
  print("input_file:",input_path)
  print("IsValid?",not input_file.IsZombie())
  
  # Fitted variable
  mass = ROOT.RooRealVar(var,"Mass [GeV]",4.7,5.7)
  variables = ROOT.RooArgSet(mass)

  # Build (and select) dataset
  dataset = ROOT.RooDataSet("dataset","dataset",tree,variables)
  cuts = ROOT.TCut("b_mass>0.") # i.e. null atm ...
  dataset_selected = dataset.reduce(cuts.GetTitle())
  dataset_selected.Print("V")

  # Combinatorial background
  #c0 = ROOT.RooRealVar("c0","c0",-0.5,-100.,0.) # decay term (args: start,min,max)
  #combinatorial = ROOT.RooExponential("combinatorial","exponential",mass,c0)
  #N_combinatorial = ROOT.RooRealVar("N_combinatorial", "N_combinatorial",1.e4,0.,1.e8)
  #ex_combinatorial = ROOT.RooExtendPdf("ex_combinatorial","ex_combinatorial",combinatorial,N_combinatorial)
  c0 = ROOT.RooRealVar("c0", "c0",-0.5,-40.,0.)
  mBkg0 = ROOT.RooExponential("mBkg0","exponential",mass,c0)
  N_mBkg0 = ROOT.RooRealVar("N_mBkg0","N_mBkg0",10000.,0.,100000000.);
  e_mBkg0 = ROOT.RooExtendPdf("e_mBkg0","e_mBkg0",mBkg0,N_mBkg0);

  # Partially reconstructed background (Exp*Erfc)
  #exp_slope = ROOT.RooRealVar("exp_slope","slope of exponential",2.25,2.,3.)
  #exp_offset = ROOT.RooRealVar("exp_offset", "offset of exponential", 5.15, 5.1, 5.2)
  #erfc_mean = ROOT.RooRealVar("erfc_mean", "mean of the Erfc gaussian",5.2,5.15,5.25)
  #erfc_sigma = ROOT.RooRealVar("erfc_sigma", "width of the Erfc gaussian",0.03,0.025,0.035)
  #function = "TMath::Exp(TMath::Abs(exp_slope)*("+var+"-exp_offset))*TMath::Erfc(("+var+"-erfc_mean)/erfc_sigma)"
  #partial = ROOT.RooGenericPdf("partial","Exp*Erfc",function,ROOT.RooArgSet(mass,erfc_mean,erfc_sigma,exp_slope,exp_offset))
  #N_partial = ROOT.RooRealVar("N_partial", "N_partial",3.e4,0.,1.e7)
  #ex_partial = ROOT.RooExtendPdf("ex_partial","ex_partial",partial,N_partial)
  ErfSlope = ROOT.RooRealVar("ErfSlope", "Erf Slope", 2.25, 2., 3.)
  meanErf = ROOT.RooRealVar("meanErf", "mean of the Erf gaussian", 5.2, 5.15, 5.25)
  sigmaErf = ROOT.RooRealVar("sigmaErf", "width of the Erf gaussian", 0.03, 0.025, 0.035)
  ErfOffset = ROOT.RooRealVar("ErfOffset", "Offset of Erf exponential", 5.15, 5.1, 5.2)
  Erf = ROOT.RooGenericPdf("Erf", "Error Function", "TMath::Exp(TMath::Abs(ErfSlope)*("+var+"-ErfOffset))*TMath::Erfc(("+var+"-meanErf)/sigmaErf)", ROOT.RooArgSet(mass, meanErf, sigmaErf,ErfSlope,ErfOffset))
  N_Erf = ROOT.RooRealVar("N_Erf", "N_Erf", 30000, 0, 10000000)
  e_Erf = ROOT.RooExtendPdf("e_Erf", "e_Erf", Erf, N_Erf)
  
  # Signal (double-sided CB)
  #gaus_mean = ROOT.RooRealVar("gaus_mean","mu",5.27)
  #gaus_sigma = ROOT.RooRealVar("gaus_sigma","width",0.,0.,1.e3)
  #signal_gaus = ROOT.RooGaussian("signal_gaus","signal, gaussian",mass,gaus_mean,gaus_sigma)
  mean_m = ROOT.RooRealVar("mean_m","mu",5.27)
  sigma_m = ROOT.RooRealVar("sigma_m","width",0.)
  mSig1 = ROOT.RooGaussian("mSig1","signal p.d.f.", mass, mean_m, sigma_m)
  
  # Signal (double-sided CB)
  #sigma_cb = ROOT.RooRealVar("sigma_cb","width",0.0577)
  #a1 = ROOT.RooRealVar("a1","a1",0.819)
  #p1 = ROOT.RooRealVar("p1","p1",130.)
  #a2 = ROOT.RooRealVar("a2","a2",3.10)
  #p2 = ROOT.RooRealVar("p2","p2",2.04)
  #signal_cb = ROOT.RooCrystalBall("signal_cb","signal, double-sided CB",mass,gaus_mean,sigma_cb,a1,p1,a2,p2)
  sigma_cb = ROOT.RooRealVar("sigma_cb","width",0.0577)
  a1 = ROOT.RooRealVar("a1","a1",0.819)
  p1 = ROOT.RooRealVar("p1","p1",130.)
  a2 = ROOT.RooRealVar("a2","a2",3.10)
  p2 = ROOT.RooRealVar("p2","p2",2.04)
  mSig3 = ROOT.RooCrystalBall("dcbPdf","DoubleSidedCB",mass,mean_m,sigma_cb,a1,p1,a2,p2)

  # Fraction of signal pdf (CB:val=0, Gaus:val=1), HACKED: Gaus contribution = 0
  #frac = ROOT.RooRealVar("frac","frac",0.,0.,0.)
  #signal = ROOT.RooAddPdf("signal","signal",ROOT.RooArgList(signal_gaus,signal_cb),frac)
  #N_signal = ROOT.RooRealVar("N_signal","N_signal",8.e4,0.,1.e8)
  #ex_signal = ROOT.RooExtendPdf("ex_signal","ex_signal",signal,N_signal)
  frac = ROOT.RooRealVar("frac", "frac", 0., 0., 0.)
  mSig = ROOT.RooAddPdf("mSig", "mSig", ROOT.RooArgList(mSig1, mSig3), frac)
  N_mSig = ROOT.RooRealVar("N_mSig", "N_mSig", 80000., 0., 1000000000.)
  e_mSig = ROOT.RooExtendPdf("e_mSig", "e_mSig", mSig, N_mSig)
  
  # Total (S+B) shape
  total = None
#  if isMC == True: total = ROOT.RooAddPdf("total","total",ROOT.RooArgSet(ex_signal))
#  else : total = ROOT.RooAddPdf("total","total",ROOT.RooArgSet(ex_combinatorial,ex_signal,ex_partial))
#  result = total.fitTo(dataset_selected,ROOT.RooFit.NumCPU(4,ROOT.kTRUE),ROOT.RooFit.Save(),ROOT.RooFit.Extended())
  if isMC == True: total = ROOT.RooAddPdf("total", "total", ROOT.RooArgSet(e_mSig))
  else : total = ROOT.RooAddPdf("total", "total", ROOT.RooArgSet(e_mBkg0, e_mSig, e_Erf))
  fr = total.fitTo(dataset_selected, ROOT.RooFit.NumCPU(4, ROOT.kTRUE), ROOT.RooFit.Save(), ROOT.RooFit.Extended())
  
  ################################################################################
  # PLOTTING
  
  # Binning
  nbins = 75 if region != "LowQ2" else 20

  # Plot residuals panel
  draw_residuals = True

  title = "An example title"
  frame_main = mass.frame(ROOT.RooFit.Title(title),ROOT.RooFit.Bins(nbins))

  # Colors
  index_erf = 1756#ROOT.TColor.GetFreeColorIndex()
  index_sig = 1757#ROOT.TColor.GetFreeColorIndex()+1
  index_exp = 1758#ROOT.TColor.GetFreeColorIndex()+2
  color_erf = ROOT.TColor(index_erf,  27./255.,158./255.,119./255.)
  color_sig = ROOT.TColor(index_sig, 217./255., 95./255.,  2./255.)
  color_exp = ROOT.TColor(index_exp, 117./255.,112./255.,179./255.)

  # Data
  dataset_selected.plotOn(
      frame_main,
      ROOT.RooFit.XErrorSize(0),
      #ROOT.RooFit.Name("data"),
      ROOT.RooFit.Name("plotmc"),
      )
  # Total pdf
  total.plotOn(
      frame_main,
      ROOT.RooFit.LineColor(ROOT.kAzure+1),
      ROOT.RooFit.Name("totalpdf"),
      )
  # Combinatorial pdf
  if isMC==True:
    total.plotOn(
      frame_main,
      #ROOT.RooFit.Components("ex_combinatorial"),
      ROOT.RooFit.Components("e_mBkg0"),
      ROOT.RooFit.DrawOption("FL"),
      ROOT.RooFit.LineColor(ROOT.kAzure+8),
      ROOT.RooFit.FillColor(ROOT.kViolet+2),#color_exp),#index_exp),
      ROOT.RooFit.FillStyle(1004),
      #ROOT.RooFit.Name("combinatorial"),
      ROOT.RooFit.Name("bkg"),
      )
  # Signal pdf
  total.plotOn(
      frame_main,
      #ROOT.RooFit.Components(ex_signal),
      ROOT.RooFit.Components(e_mSig),
      ROOT.RooFit.DrawOption("FL"),
      ROOT.RooFit.LineColor(ROOT.kAzure+5),
      ROOT.RooFit.FillColor(ROOT.kOrange+2),#color_sig),#index_sig),
      ROOT.RooFit.FillStyle(1004),
      #ROOT.RooFit.Name("signal"),
      ROOT.RooFit.Name("signalpdf"),
      )
  # Partially reco'ed pdf
  if isMC==False:
    total.plotOn(
      frame_main,
      #ROOT.RooFit.Components("ex_partial"),
      ROOT.RooFit.Components("e_Erf"),
      ROOT.RooFit.DrawOption("FL"),
      ROOT.RooFit.LineColor(ROOT.kAzure+10),
      ROOT.RooFit.FillColor(ROOT.kGreen+3),#color_erf),#index_erf),
      ROOT.RooFit.FillStyle(1004),
      #ROOT.RooFit.Name("partial"),
      ROOT.RooFit.Name("erf"),
      )
  # Replot data to be on top?
  dataset_selected.plotOn(frame_main,ROOT.RooFit.XErrorSize(0))

  frame_main.GetXaxis().SetLabelSize(0.05)
  frame_main.GetXaxis().SetTitleSize(0.05)
  
  canvas = ROOT.TCanvas("fit","fit",800,800)
  # canvas.Divide(2,2)

  #if draw_residuals==True:
    
  frame_main.GetXaxis().SetLabelSize(0.0)
  frame_main.GetXaxis().SetTitleSize(0.0)
    
  dummy_frame = mass.frame(ROOT.RooFit.Title("dummy frame"),ROOT.RooFit.Bins(nbins))
  dataset_selected.plotOn(dummy_frame,ROOT.RooFit.XErrorSize(0))
  total.plotOn(dummy_frame)
  h_residuals_mass = dummy_frame.pullHist()
    
  frame_residuals = mass.frame(ROOT.RooFit.Title("residuals"),ROOT.RooFit.Bins(nbins))
  frame_residuals.GetYaxis().SetTitle("Pull")
  frame_residuals.GetYaxis().CenterTitle(True)
  frame_residuals.GetYaxis().SetTitleSize(0.1)
  frame_residuals.GetYaxis().SetLabelSize(.1)
  frame_residuals.GetYaxis().SetTitleOffset(0.25)
  frame_residuals.GetYaxis().SetNdivisions(5)
  frame_residuals.addPlotable(h_residuals_mass,"P")
  frame_residuals.SetTitle("")
  frame_residuals.GetXaxis().SetLabelSize(0.1)
  frame_residuals.GetXaxis().SetTitleSize(0.1)
  
  # Fit (upper) panel
  pad1 = ROOT.TPad("pad1","pad1",0,0.22,1,1)
  pad1.SetFillColor(0)
  pad1.SetBottomMargin(0.02)
  pad1.SetBorderMode(0)
  pad1.Draw()
  
  # Residuals (lower) panel
  pad2 = ROOT.TPad("pad2","pad2",0,0,1,0.22)
  pad2.SetTopMargin(0.)
  pad2.SetRightMargin(0.1)
  pad2.SetBottomMargin(0.3)
  pad2.SetBorderMode(0)
  pad2.SetFillColor(0)
  pad2.Draw()
  
  # Draw residuals and lines
  pad2.cd()
  zero_line = ROOT.TF1("zero_line","0",0,1000)
  zero_line.SetLineStyle(1)
  zero_line.SetLineWidth(2)
  zero_line.SetLineColor(ROOT.kGray)
  zero_line.Draw("same")
  # TF1 *f_1 = new TF1("f_1", "1", 0, 116);  f_1.SetLineColor(kBlue); f_1.SetLineStyle(7)
  # TF1 *f_2 = new TF1("f_2", "-1", 0, 116); f_2.SetLineColor(kBlue); f_2.SetLineStyle(7)
  # f_1.Draw("same") f_2.Draw("same")
  frame_residuals.Draw("same")
  pad1.cd()
  
  # Draw main frame
  frame_main.GetXaxis().SetNdivisions(504)
  frame_main.Draw()
  # canvas.cd(1).SetLogy(1)
  
  # CMS Preliminary label
  latex = ROOT.TLatex()
  latex.SetTextSize(0.04)
  latex.DrawLatex(2.60,frame_main.GetMaximum()*1.01,"#bf{CMS} Preliminary")
  latex.DrawLatex(2.95,frame_main.GetMaximum()*1.01,"137 fb^{-1} (13 TeV)")

  ################################################################################
  # DIAGNOSTIC

#  sigma = 2.
#  lower = gaus_mean.getVal() - sigma*sigma_cb.getVal()
#  upper = gaus_mean.getVal() + sigma*sigma_cb.getVal()
#  mass.setRange("signal_frac",lower,upper) 
# 
#  signal_window = ex_signal.createIntegral(mass,ROOT.RooFit.NormSet(mass),ROOT.RooFit.Range("signal_window"))
#  total_window = total.createIntegral(mass,ROOT.RooFit.NormSet(mass),ROOT.RooFit.Range("signal_window"))
#  
#  print()
#  print(f"Original number of events processed: {dataset.sumEntries():.1f}")
#  print(f"Selected number of events processed: {dataset_selected.sumEntries():.1f}")
#  print()
#  signal_window_frac = signal_window.getVal()
#  signal_N = N_signal.getVal()
#  print(f"Fraction of signal within +/-{sigma:.0f} sigma window: {signal_window_frac:.2f}")
#  print(f"Signal yield within +/-{sigma:.0f} sigma window: {signal_N:.1f}")
#  print()
##  total_window_frac = total_window.getVal()
##  N_total = N_total.getVal()
##  print(f"Fraction of signal within +/-{sigma:.0f} sigma window: {total_window_frac:.2f}")
##  print(f"Signal yield within +/-{sigma:.0f} sigma window: {N_total:.1f}")

  ################################################################################
  # LEGEND
  
  legend = ROOT.TLegend(0.65,0.65,0.88,0.88)

  rounded_nearest = 0#int(N_signal.getVal())
  signal = f"{rounded_nearest:.0f}"
  b_rounded = 0#int(ex_signal.getVal())
  serr   = str(b_rounded)
  #soverb = str((signal_window.getVal()*N_signal.getVal())/math.sqrt((total_window.getVal()*dataset.sumEntries())))
  #soberb = str((signal_window.getVal()*N_signal.getVal())/(total_window.getVal()*mc.sumEntries()-signal_window.getVal()*N_signal.getVal()))
  #TString sb(soverb)
  #TString soberbstr(soberb)
  #TString tt(std::to_string(mc.sumEntries()))

  legend.SetTextFont(42)
  legend.SetTextSize(0.038)
  legend.SetBorderSize(0)
  legend.SetFillColor(0)

#  legend.AddEntry("data", "Data", "ep")
#  legend.AddEntry("totalpdf", "S+B shape", "l")
#  legend.AddEntry("signalpdf", "Signal ("+signal+")", "f") # "Signal ("+s+"#pm"+TString(serr)+")", "f")
#  legend.AddEntry("bkgd1", "Bkgd (comb.)", "f")
#  legend.AddEntry("bkgd2", "Bkgd (part.)", "f")
#  #legend.AddEntry("","S/#sqrt{S+B}(2#sigma):"+sb,"")
#  #legend.AddEntry("","S/B(2#sigma):"+soberbstr,"")
#  #legend.AddEntry("","Total Entries =  "+tt,"")

  legend.AddEntry("plotmc", "Data", "ep")
  legend.AddEntry("totalpdf", "S+B shape", "l")
  legend.AddEntry("signal", "Signal ("+signal+")", "f") # "Signal ("+s+"#pm"+TString(serr)+")", "f")
  legend.AddEntry("erf", "Bkgd (part.)", "f")
  legend.AddEntry("bkg", "Bkgd (comb.)", "f")
  legend.Draw()

  # Save canvas
  canvas.SaveAs("plots/"+tag+"/fitted_"+tag+"_"+sample+"_"+var+"_new.pdf")

################################################################################
# MAIN
################################################################################
  
if __name__ == "__main__":
    print("Starting...")

    # Input variable to be fitted
    var = "b_mass"

    # MC or data? (Switch off bkgd shapes for former|)
    isMC = False

    # Q2 region
    regions = ["LowQ2","Jpsi","Psi2S"]
    region = regions[1]

    # Production tag
    tag = ["2022Sep05","2022Oct12"][1]

    # Sample being considered
    sample = [
        "BuToKee",
        "BuToKJpsi_Toee",
        "BuToKPsi2S_Toee",
        "Run2022",
        "Run2022_Jpsi",
        ][-1]

    # Override region if using an MC sample
    if   "BuToKee" in sample:         region = regions[0]
    elif "BuToKJpsi_Toee" in sample:  region = regions[1]
    elif "BuToKPsi2S_Toee" in sample: region = regions[2]

    fit_new()
    print("Finished...")
