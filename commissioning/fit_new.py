import ROOT
import math
import json

def fit_new(
    isMC=True,
    region=None,
    sample=None,
    tag=None,
    trigger=None,
    var=None,
    verbose=0,
    read_signal_params=True,write_signal_params=True,fix_signal_params=True,
    read_comb_params=True,write_comb_params=True,fix_comb_params=True,
    add_part_bkgd=True,read_part_params=True,write_part_params=True,fix_part_params=True,
    ) :

  print("#####################")
  print("Calling fit_new() ...")
  print("isMC:   ",isMC)
  print("region: ",region)
  print("sample: ",sample)
  print("trigger:",trigger)
  print("tag:    ",tag)
  print("verbose:",verbose)
  print("#####################")
  
  ################################################################################
  # INITIALISE AND PREPARE DATA SET

  # Suppress ROOT output messages?
  if verbose<1:
    ROOT.RooMsgService.instance().setSilentMode(ROOT.kTRUE)

  # Style
  ROOT.gStyle.SetOptStat(0)
  ROOT.gStyle.SetOptFit(0)

  input_path = "./slimmed/"+tag+"/slimmed_"+tag+"_"+sample+".root"
  input_file = ROOT.TFile(input_path,"READ")
  tree = input_file.Get("tree")
  print("input_file:",input_path)
  print("IsValid?",not input_file.IsZombie())
  
  # Trigger and fitted variables
  mass = ROOT.RooRealVar(var,"Mass [GeV]",4.7,5.7)
  if trigger != None and trigger != "":
    trg = ROOT.RooRealVar(trigger,"Trigger result",0.,1.)
    variables = ROOT.RooArgSet(mass,trg)
    print("Trigger variable:",trigger)
  else:
    variables = ROOT.RooArgSet(mass)
  print("Fitted variable: ",var)
  
  # Build (and select) dataset
  dataset = ROOT.RooDataSet("dataset","dataset",tree,variables)

  # Select subset of dataset (e.g. apply trigger requirement)
  #cuts = ROOT.TCut("L1_10p5_HLT_6p5>0.")
  if trigger != None and trigger != "": cuts = ROOT.TCut(trigger+">0.5")
  else: cuts = ROOT.TCut("1")
  dataset_selected = dataset.reduce(cuts.GetTitle())
  if verbose>0: dataset_selected.Print("V")

  ################################################################################
  # SIGNAL PARAMETERS (DEFAULTS AND PARSING JSON)
  
  # Default initial parameter values for signal PDF
  defaults = {
      "Jpsi":{
          "cb_mean":(5.279,5.26,5.30),
          "cb_sigma":(0.057,0.04,0.07),
          "cb_alphaL":(2.,0.5,3.),
          "cb_nL":(10.,1.,100.),
          "cb_alphaR":(2.,0.5,3.),
          "cb_nR":(10.,1.,100.),
          "exp_slope":(-0.5,-100.,0.), # combinatorial
          "expo_slope":(3.8,3.0,5.0),       # (2.25,1.,10.)
          #"expo_offset":(5.13, 5.11, 5.15), # (5.13, 5.1, 5.15)
          "erfc_mean":(5.16,5.15,5.17),     # (5.13,5.1,5.15)
          "erfc_sigma":(0.06,0.05,0.10),    # (0.03,0.015,0.05)
          },
      "Psi2S":{
          "cb_mean":(5.279,5.26,5.30),
          "cb_sigma":(0.063,0.04,0.07),
          "cb_alphaL":(2.,0.5,3.),
          "cb_nL":(10.,1.,100.),
          "cb_alphaR":(2.,0.5,3.),
          "cb_nR":(10.,1.,100.),
          "exp_slope":(-0.5,-100.,0.),
          "expo_slope":(3.8,3.0,5.0),       # (2.25,1.,10.)
          #"expo_offset":(5.13, 5.11, 5.15), # (5.13, 5.1, 5.15)
          "erfc_mean":(5.16,5.15,5.17),     # (5.13,5.1,5.15)
          "erfc_sigma":(0.06,0.05,0.10),    # (0.03,0.015,0.05)
          },
      "LowQ2":{
          "cb_mean":(5.279,5.26,5.30),
          "cb_sigma":(0.05,0.04,0.07),
          "cb_alphaL":(2.,0.5,3.),
          "cb_nL":(10.,1.,100.),
          "cb_alphaR":(2.,0.5,3.),
          "cb_nR":(10.,1.,100.),
          "exp_slope":(-0.5,-100.,0.),
          "expo_slope":(3.8,3.0,5.0),       # (2.25,1.,10.)
          #"expo_offset":(5.13, 5.11, 5.15), # (5.13, 5.1, 5.15)
          "erfc_mean":(5.16,5.15,5.17),     # (5.13,5.1,5.15)
          "erfc_sigma":(0.06,0.05,0.10),    # (0.03,0.015,0.05)
          },
  }.get(region)

  if ( read_signal_params==True or read_comb_params==True ) and trigger != None:
    trigger_str = "trigger_OR" if trigger == "" else trigger
    filename = 'parameters.json'
    try:
      with open(filename,'r') as f:
        try:
          dct = json.load(f)
          if read_signal_params==True:
              isMC_str = 'mc'
              if isMC_str in dct.keys() and region in dct[isMC_str].keys() and trigger_str in dct[isMC_str][region].keys():
                  for param in ["cb_mean","cb_sigma","cb_alphaL","cb_nL","cb_alphaR","cb_nR"]:
                      if param in dct[isMC_str][region][trigger_str]:
                          defaults[param] = dct[isMC_str][region][trigger_str][param]
                      else:
                          print("Unable to read param:",isMC_str,region,trigger_str,param)
          if read_comb_params==True:
              isMC_str = 'data'
              if isMC_str in dct.keys() and region in dct[isMC_str].keys() and trigger_str in dct[isMC_str][region].keys():
                  for param in ["exp_slope"]:
                      if param in dct[isMC_str][region][trigger_str]:
                        defaults[param] = dct[isMC_str][region][trigger_str][param]
                      else:
                          print("Unable to read param:",isMC_str,region,trigger_str,param)
          if read_part_params==True:
              isMC_str = 'data'
              if isMC_str in dct.keys() and region in dct[isMC_str].keys() and trigger_str in dct[isMC_str][region].keys():
                  for param in ["expo_slope","erfc_mean","erfc_sigma"]: # "expo_offset"
                      if param in dct[isMC_str][region][trigger_str]:
                        defaults[param] = dct[isMC_str][region][trigger_str][param]
                      else:
                          print("Unable to read param:",isMC_str,region,trigger_str,param)
        except json.decoder.JSONDecodeError:
          print("Problem parsing json contained in file:",filename)
    except FileNotFoundError:
      print("Problem opening file:",filename)
  print("Initial parameter values:",defaults)

  ################################################################################
  # SIGNAL PARAMETERS

  # Fixed or constrained signal shapes
  (idx0,idx1,idx2) = (0,1,2) if fix_signal_params==False else (0,0,0) # (central,low,high)
  
  # Signal (double-sided CB)
  #gaus_mean = ROOT.RooRealVar("gaus_mean","gaussian mean",5.27,5.25,5.3)
  #gaus_sigma = ROOT.RooRealVar("gaus_sigma","gaussian sigma",0.01,0.,1.)
  #gaus_pdf = ROOT.RooGaussian("gaus_pdf","gaussian (signal) pdf",mass,gaus_mean,gaus_sigma)
  
  # Signal (double-sided CB)
  # https://root.cern/doc/v624/classRooCrystalBall.html#ae323c7f61647b4fb193d552bf393083d
  cb_mean = ROOT.RooRealVar(
      "cb_mean",
      "DS-CB: location parameter of the Gaussian component",
      defaults["cb_mean"][idx0],defaults["cb_mean"][idx1],defaults["cb_mean"][idx2])
  cb_sigma = ROOT.RooRealVar(
      "cb_sigma",
      "DS-CB: width parameter of the Gaussian component",
      defaults["cb_sigma"][idx0],defaults["cb_sigma"][idx1],defaults["cb_sigma"][idx2])
  cb_alphaL = ROOT.RooRealVar(
      "cb_alphaL",
      "DS-CB: location of transition to a power law on the left, in std devs away from mean",
      defaults["cb_alphaL"][idx0],defaults["cb_alphaL"][idx1],defaults["cb_alphaL"][idx2])
  cb_nL = ROOT.RooRealVar(
      "cb_nL",
      "DS-CB: exponent of power-law tail on the left",
      defaults["cb_nL"][idx0],defaults["cb_nL"][idx1],defaults["cb_nL"][idx2])
  cb_alphaR = ROOT.RooRealVar(
      "cb_alphaR",
      "DS-CB: location of transition to a power law on the right, in std devs away from mean",
      defaults["cb_alphaR"][idx0],defaults["cb_alphaR"][idx1],defaults["cb_alphaR"][idx2])
  cb_nR = ROOT.RooRealVar(
      "cb_nR",
      "DS-CB: exponent of power-law tail on the right",
      defaults["cb_nR"][idx0],defaults["cb_nR"][idx1],defaults["cb_nR"][idx2])
  cb_pdf = ROOT.RooCrystalBall(
      "cb_pdf",
      "Double-sided crystal-ball pdf",
      mass,cb_mean,cb_sigma,cb_alphaL,cb_nL,cb_alphaR,cb_nR)
  
  # Fraction of signal pdf (CB:val=0, Gaus:val=1), HACKED: Gaus contribution = 0
  #gaus_frac = ROOT.RooRealVar("gaus_frac","fraction of gausian (signal) component",0.,0.,0.)
  #sum_of_pdf = ROOT.RooAddPdf("sum_of_pdf","sum of signal pdf",ROOT.RooArgList(gaus_pdf,cb_pdf),gaus_frac)
  #signal_num = ROOT.RooRealVar("signal_num","signal num",1.e4,0.,1.e6)
  #signal_pdf = ROOT.RooExtendPdf("signal_pdf","signal pdf",sum_of_pdf,signal_num)

  # Signal pdf
  signal_num = ROOT.RooRealVar("signal_num","signal num",dataset_selected.sumEntries(),0.,1.e6) # estimate S from selected events
  signal_pdf = ROOT.RooExtendPdf("signal_pdf","signal pdf",cb_pdf,signal_num)

  ################################################################################
  # BKGD PARAMETERS

  # Fixed or constrained bkgd shapes
  (idx0,idx1,idx2) = (0,1,2) if fix_comb_params==False else (0,0,0) # (central,low,high)
  
  # Combinatorial background
  #exp_slope = ROOT.RooRealVar("exp_slope","slope of exponential",-0.5,-100.,0.)
  exp_slope = ROOT.RooRealVar(
      "exp_slope",
      "slope of exponential",
      defaults["exp_slope"][idx0],defaults["exp_slope"][idx1],defaults["exp_slope"][idx2])
  expo_pdf = ROOT.RooExponential("expo_pdf","Exponential PDF",mass,exp_slope)
  comb_num = ROOT.RooRealVar("comb_num", "combinatorial num",dataset_selected.sumEntries(),0.,1.e6)
  comb_pdf = ROOT.RooExtendPdf("comb_pdf","combinatorial pdf",expo_pdf,comb_num)

  # Fixed or constrained bkgd shapes
  (idx0,idx1,idx2) = (0,1,2) if fix_part_params==False else (0,0,0) # (central,low,high)

  # Partially reconstructed background (Exp*Erfc)
  expo_slope = ROOT.RooRealVar(
      "expo_slope",
      "slope of exponential",
      defaults["expo_slope"][idx0],defaults["expo_slope"][idx1],defaults["expo_slope"][idx2])
#  expo_offset = ROOT.RooRealVar(
#      "expo_offset",
#      "offset of exponential",
#      defaults["expo_offset"][idx0],defaults["expo_offset"][idx1],defaults["expo_offset"][idx2])
  erfc_mean = ROOT.RooRealVar(
      "erfc_mean",
      "mean of the Erfc gaussian",
      defaults["erfc_mean"][idx0],defaults["erfc_mean"][idx1],defaults["erfc_mean"][idx2])
  erfc_sigma = ROOT.RooRealVar(
      "erfc_sigma",
      "width of the Erfc gaussian",
      defaults["erfc_sigma"][idx0],defaults["erfc_sigma"][idx1],defaults["erfc_sigma"][idx2])
  #function = "TMath::Exp(TMath::Abs(expo_slope)*("+var+"-expo_offset))*TMath::Erfc(("+var+"-erfc_mean)/erfc_sigma)"
  function = "TMath::Exp(TMath::Abs(expo_slope)*("+var+"-erfc_mean))*TMath::Erfc(("+var+"-erfc_mean)/erfc_sigma)"
  generic_pdf = ROOT.RooGenericPdf(
      "generic_pdf",
      "generic pdf (expo*erfc)",
      function,ROOT.RooArgSet(mass,erfc_mean,erfc_sigma,expo_slope))#,expo_offset))
  part_num = ROOT.RooRealVar("part_num", "partially reco'ed num",3.e4,0.,1.e7)
  part_pdf = ROOT.RooExtendPdf("part_pdf","partially reco'ed pdf",generic_pdf,part_num)

  ################################################################################
  # MODEL
  
  # Total (S+B) shape
  model = None
  if isMC==True:             model = ROOT.RooAddPdf("total", "total", ROOT.RooArgSet(signal_pdf))
  elif add_part_bkgd==False: model = ROOT.RooAddPdf("total", "total", ROOT.RooArgSet(comb_pdf, signal_pdf))
  else:                      model = ROOT.RooAddPdf("total", "total", ROOT.RooArgSet(comb_pdf, signal_pdf, part_pdf))
  
  if verbose>2:
    # Get list of observables
    print("getObservables")
    model_obs = model.getObservables(dataset_selected)
    model_obs.Print("v")
    # Get list of parameters
    print("getParameters")
    model_params = model.getParameters({mass})
    model_params.Print("v")
    # Get list of component objects, top-level node
    print("getComponents")
    model_comps = model.getComponents()
    model_comps.Print("v")
  
  ################################################################################
  # FITTING

  # Perform fit
  result = None
#  if verbose>0:
#      result = model.fitTo(
#          dataset_selected,
#          ROOT.RooFit.NumCPU(4, ROOT.kTRUE),
#          ROOT.RooFit.Save(),
#          ROOT.RooFit.Extended()
#          )
#  else:
  result = model.fitTo(
    dataset_selected,
    ROOT.RooFit.NumCPU(4, ROOT.kTRUE),
    ROOT.RooFit.Save(),
    ROOT.RooFit.Extended(),
    ROOT.RooFit.PrintEvalErrors(-1 if verbose<1 else 0 if verbose<4 else 100)
      )
  params = result.floatParsFinal()

  if ( write_signal_params==True or write_comb_params==True or write_part_params==True ) and trigger != None :
    print("WRITE")
    isMC_str = 'mc' if isMC else 'data'
    trigger_str = "trigger_none" if trigger == "" else trigger

    # Open file and parse json
    dct = {}
    filename = 'parameters.json'
    try:
      with open(filename,'r') as f:
        try:
          dct = json.load(f)
        except json.decoder.JSONDecodeError:
          print("Problem parsing json contained in file:",filename)
    except FileNotFoundError:
      print("Problem opening file:",filename)

    # Append to dict
    if isMC_str not in dct.keys():
      dct[isMC_str] = {}
    if region not in dct[isMC_str].keys():
      dct[isMC_str][region] = {}
    if trigger_str not in dct[isMC_str][region].keys():
      dct[isMC_str][region][trigger_str] = {}
    dct[isMC_str][region][trigger_str]["status"] = result.status()
    dct[isMC_str][region][trigger_str]["covQual"] = result.covQual()
    dct[isMC_str][region][trigger_str]["edm"] = result.edm()
    dct[isMC_str][region][trigger_str]["minNll"] = result.minNll()
    if write_signal_params==True:
      for param in params:
        if param.GetName() in ["signal_num","cb_alphaL","cb_alphaR","cb_mean","cb_nL","cb_nR","cb_sigma"]:
          dct[isMC_str][region][trigger_str][param.GetName()] = (param.getVal(),param.getVal()-param.getError(),param.getVal()+param.getError())
    if write_comb_params==True:
      for param in params:
        if param.GetName() in ["comb_num","exp_slope"]:
          dct[isMC_str][region][trigger_str][param.GetName()] = (param.getVal(),param.getVal()-param.getError(),param.getVal()+param.getError())
    if write_part_params==True:
      for param in params:
        if param.GetName() in ["part_num","expo_slope","erfc_mean","erfc_sigma"]: #"expo_offset"
          dct[isMC_str][region][trigger_str][param.GetName()] = (param.getVal(),param.getVal()-param.getError(),param.getVal()+param.getError())

    # Write json to output file
    try:
      with open(filename,'w') as f:
        try:
          json.dump(dct,f,indent=4) #ensure_ascii=False,
        except json.decoder.JSONDecodeError:
          print("Problem parsing json to file:",filename)
    except FileNotFoundError:
      print("Problem writing to file:",filename)

  if verbose>1:
    
    # Print details
    print("RESULT:")
    result.Print("v")

    # Status:
    # status = 1    : Covariance was made pos defined
    # status = 2    : Hesse is invalid
    # status = 3    : Edm is above max
    # status = 4    : Reached call limit
    # status = 5    : Any other failure
    print("Status = ",result.status())

    # Access basic information
    print("EDM = ", result.edm())
    print("-log(L) minimum = ", result.minNll())
  
    # Access list of final fit parameter values
    print("final value of floating parameters")
    params.Print("v")
  
    print("final value of floating parameters AGAIN")
    print(type(params))
    print(params)
    for param in params:
      if param.GetName() in ["cb_alphaL","cb_alphaR","cb_mean","cb_nL","cb_nR","cb_sigma","signal_num"]:
        print("PARAM:",param.GetName(),param.getVal(),param.getError())
    
    # Extract covariance and correlation matrix as ROOT.TMatrixDSym
    print("covariance matrix quality",result.covQual())
    cor = result.correlationMatrix()
    cov = result.covarianceMatrix()
    print("covariance matrix:")
    cov.Print()
    print("correlation matrix:")
    cor.Print()
                
    # Access correlation matrix elements
    #print("correlation between signal_num and comb_num is  ", result.correlation(signal_num, comb_num))
    #print("correlation between signal_num and part_num is  ", result.correlation(signal_num, part_num))
    #print("correlation between comb_num and part_num is  ", result.correlation(comb_num, part_num))

  ################################################################################
  # PLOTTING
  
  # Binning
  #nbins = 75 if region != "LowQ2" else 20
  nbins = 100
  if isMC==False:
    #if   dataset_selected.sumEntries() > 10000: nbins = 100
    #elif dataset_selected.sumEntries() >  7500: nbins =  75
    #elif dataset_selected.sumEntries() >  5000: nbins =  50
    #else:                                       nbins =  25
    if   dataset_selected.sumEntries() > 2000: nbins = 100
    elif dataset_selected.sumEntries() >  500: nbins =  50
    else:                                      nbins =  25
  
  # Plot residuals panel
  draw_residuals = True

  title = "An example title"
  frame_main = mass.frame(ROOT.RooFit.Title(title),ROOT.RooFit.Bins(nbins))

#  # Colors
#  index_erf = 1756#ROOT.TColor.GetFreeColorIndex()
#  index_sig = 1757#ROOT.TColor.GetFreeColorIndex()+1
#  index_exp = 1758#ROOT.TColor.GetFreeColorIndex()+2
#  color_erf = ROOT.TColor(index_erf,  27./255.,158./255.,119./255.)
#  color_sig = ROOT.TColor(index_sig, 217./255., 95./255.,  2./255.)
#  color_exp = ROOT.TColor(index_exp, 117./255.,112./255.,179./255.)

  # Data
  dataset_selected.plotOn(
      frame_main,
      ROOT.RooFit.XErrorSize(0),
      ROOT.RooFit.Name("data"),
      )
  # Total pdf
  model.plotOn(
      frame_main,
      ROOT.RooFit.LineColor(ROOT.kAzure+1),
      ROOT.RooFit.Name("model"),
      )
  # Combinatorial pdf
  if isMC==False:
    model.plotOn(
      frame_main,
      ROOT.RooFit.Components("comb_pdf"),
      ROOT.RooFit.DrawOption("FL"),
      ROOT.RooFit.LineColor(ROOT.kAzure+8),
      ROOT.RooFit.FillColor(ROOT.kViolet+6),#1758),#color_exp),#index_exp),
      ROOT.RooFit.FillStyle(1004),
      ROOT.RooFit.Name("comb"),
      )
  # Signal pdf
  model.plotOn(
      frame_main,
      ROOT.RooFit.Components(signal_pdf),
      ROOT.RooFit.DrawOption("FL"),
      ROOT.RooFit.LineColor(ROOT.kAzure+5),
      ROOT.RooFit.FillColor(ROOT.kOrange+2),#1757),#color_sig),#index_sig),
      ROOT.RooFit.FillStyle(1004),
      ROOT.RooFit.Name("signal"),
      )
#  # Partially reco'ed pdf
  if isMC==False and add_part_bkgd==True:
    model.plotOn(
      frame_main,
      ROOT.RooFit.Components("part_pdf"),
      ROOT.RooFit.DrawOption("FL"),
      ROOT.RooFit.LineColor(ROOT.kAzure+10),
      ROOT.RooFit.FillColor(ROOT.kGreen+3),#1756),#color_erf),#index_erf),
      ROOT.RooFit.FillStyle(1004),
      ROOT.RooFit.Name("part"),
      )

    # Replot data to be on top?
  frame_main.GetXaxis().SetLabelSize(0.05)
  frame_main.GetXaxis().SetTitleSize(0.05)
  dataset_selected.plotOn(frame_main,ROOT.RooFit.XErrorSize(0))
  
  canvas = ROOT.TCanvas("fit","fit",800,800)
  # canvas.Divide(2,2)

  #if draw_residuals==True:
    
  frame_main.GetXaxis().SetLabelSize(0.0)
  frame_main.GetXaxis().SetTitleSize(0.0)
    
  dummy_frame = mass.frame(ROOT.RooFit.Title("dummy frame"),ROOT.RooFit.Bins(nbins))
  dataset_selected.plotOn(dummy_frame,ROOT.RooFit.XErrorSize(0))
  model.plotOn(dummy_frame)

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
  
  # Residuals (lower) panel
  pad2 = ROOT.TPad("pad2","pad2",0,0,1,0.22)
  pad2.SetTopMargin(0.)
  pad2.SetRightMargin(0.1)
  pad2.SetBottomMargin(0.3)
  pad2.SetBorderMode(0)
  pad2.SetFillColor(0)

  pad1.Draw()
  pad2.Draw()

  # Draw residuals and lines
  pad2.cd()
  frame_residuals.Draw("same")
  zero_line = ROOT.TF1("zero_line","0",0,1000)
  zero_line.SetLineStyle(1)
  zero_line.SetLineWidth(2)
  zero_line.SetLineColor(ROOT.kGray)
  zero_line.Draw("same")
  # TF1 *f_1 = new TF1("f_1", "1", 0, 116);  f_1.SetLineColor(kBlue); f_1.SetLineStyle(7)
  # TF1 *f_2 = new TF1("f_2", "-1", 0, 116); f_2.SetLineColor(kBlue); f_2.SetLineStyle(7)
  # f_1.Draw("same") f_2.Draw("same")
  
  # Draw main frame
  pad1.cd()
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

  sigma = 2.
  lower = cb_mean.getVal() - sigma*cb_sigma.getVal()
  upper = cb_mean.getVal() + sigma*cb_sigma.getVal()
  mass.setRange("signal_window",lower,upper) 
 
  signal_window = signal_pdf.createIntegral(mass,ROOT.RooFit.NormSet(mass),ROOT.RooFit.Range("signal_window"))
  total_window = model.createIntegral(mass,ROOT.RooFit.NormSet(mass),ROOT.RooFit.Range("signal_window"))
  
  print()
  print(f"Original number of events processed: {dataset.sumEntries():.1f}")
  print(f"Selected number of events processed: {dataset_selected.sumEntries():.1f}")
  print()
  signal_frac = signal_window.getVal()
  print(f"Fraction of signal within +/-{sigma:.0f} sigma window: {signal_frac:.2f}")
  print(f"Signal yield within +/-{sigma:.0f} sigma window: {signal_num.getVal():.1f}")
  print()
  total_frac = total_window.getVal()
  print(f"Fraction of signal within +/-{sigma:.0f} sigma window: {total_frac:.2f}")
  print(f"Signal yield within +/-{sigma:.0f} sigma window: {model.getVal():.1f}")

  ################################################################################
  # LEGEND
  ylower = 0.63 if isMC==False else 0.73 if add_part_bkgd==True else 0.78
  legend = ROOT.TLegend(0.63, ylower, 0.88, 0.88)

  rounded_nearest = int(signal_num.getVal())
  signal = f"{rounded_nearest:.0f}"
  soverb = str( ( signal_window.getVal() * signal_num.getVal() ) / math.sqrt( total_window.getVal() * dataset.sumEntries() ) )
  soberb = str( ( signal_window.getVal() * signal_num.getVal() ) / ( total_window.getVal() * dataset.sumEntries() - signal_window.getVal() * signal_num.getVal() ) )

  print()
  print("signal_num.getVal()",signal_num.getVal())
  print("signal_num.getAsymErrorHi()",signal_num.getAsymErrorHi())
  print("signal_num.getAsymErrorLo()",signal_num.getAsymErrorLo())
  print("signal_window.getVal()",signal_window.getVal())
  print("total_window.getVal()",total_window.getVal())
  print("model.getVal()",model.getVal())
  print("dataset.sumEntries()",dataset.sumEntries())
  print("soverb",soverb) # S/sqrt(S+B) (2sigma)
  print("soberb",soberb) # S/B (2sigma)
  
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

  legend.AddEntry("data", "Data", "ep")
  legend.AddEntry("model", "Total", "l")
  legend.AddEntry("signal", "Signal ("+signal+")", "f") # "Signal ("+s+"#pm"+TString(serr)+")", "f")
  if isMC==False:
    #legend.AddEntry("part", "Bkgd (part.)"+str(dataset_selected.sumEntries()), "f")
    if add_part_bkgd==True: legend.AddEntry("part", "Bkgd (part.)", "f")
    legend.AddEntry("comb", "Bkgd (comb.)", "f")
  legend.Draw()

  # Save canvas
  canvas.SaveAs("plots/"+tag+"/fitted_"+tag+"_"+sample+"_"+var+str("_"+trigger if trigger is not None else "")+".pdf")

################################################################################
# UTILITY 
################################################################################
    
# Define region
def region(sample):
  regions = ["LowQ2","Jpsi","Psi2S"]
  _region = None
  if     "Kee" in sample: _region = regions[0] # MC sample
  elif "LowQ2" in sample: _region = regions[0] # Data sample
  elif  "Jpsi" in sample: _region = regions[1] # Data or MC sample
  elif "Psi2S" in sample: _region = regions[2] # Data or MC sample
  else:                   _region = regions[0] # Data sample
  return _region

# MC or data? (Switch off bkgd shapes for former)
def isMC(sample):
    _isMC = "BuToK" in sample
    return _isMC

################################################################################
# MAIN
################################################################################
  
if __name__ == "__main__":
    print("Starting...")

    # Input variable to be fitted
    _var = "b_mass"

    # Production tag
    _tag = ["2022Sep05","2022Oct12"][1]

    # Sample being considered
    samples = [
        "BuToKJpsi_Toee",
        "BuToKPsi2S_Toee",
        "BuToKee",
        "Run2022_Jpsi",
        "Run2022_Psi2S",
        "Run2022_LowQ2",
        ]

    triggers = [
        "",
        "trigger_OR",
        #"L1_11p0_HLT_6p5",
        #"L1_10p5_HLT_6p5",
        #"L1_10p5_HLT_5p0",
        #"L1_8p5_HLT_5p0",
        #"L1_8p0_HLT_5p0",
        #"L1_7p0_HLT_5p0",
        #"L1_6p5_HLT_4p5",
        #"L1_6p0_HLT_4p0",
        #"L1_5p5_HLT_6p0",
        #"L1_5p5_HLT_4p0",
    ]

    # Test cases
    #sample = samples[-2]
    #fit_new(isMC=isMC,region="Jpsi",sample="Jpsi",tag=_tag,trigger="trigger_OR",var=_var)
    #fit_new(isMC=isMC,region="Jpsi",sample="Jpsi",tag=_tag,trigger="L1_10p5_HLT_6p5",var=_var,verbose=0)
    #fit_new(isMC=isMC,region="Jpsi",sample="Jpsi",tag=_tag,trigger="L1_5p5_HLT_4p0",var=_var)

    # Step-by-step procedure to constrain shapes
    # 1) run over signal, determine signal shape (signal:write)
    # 2) run over signal again, check signal shape (signal:read,fix)
    # 3) run over data, fixed signal shape, determine comb params (signal:read,fix, comb:write)
    # 4) run over data, fixed signal and comb shapes, check part shape (signal:read,fix, comb:read,fix)
    # 5) run over data, fixed signal and comb shapes, determine part shape (signal:read,fix, comb:read,fix, part:add,write)
        
    # Loop
    for _sample in samples:#[:1]:
        _isMC = isMC(_sample)
        _region = region(_sample)
        for _trigger in triggers:#[:1]:
            fit_new(
                isMC=_isMC,
                region=_region,
                sample=_sample,
                tag=_tag,
                trigger=_trigger,
                var=_var,
                verbose=5,
                read_signal_params= True,
                write_signal_params=True,
                fix_signal_params=  True,
                read_comb_params=   True,
                write_comb_params=  True,
                fix_comb_params=    True,
                add_part_bkgd=      True,
                read_part_params=   True,
                write_part_params=  True,
                fix_part_params=    True,
                )

    print("Finished...")
