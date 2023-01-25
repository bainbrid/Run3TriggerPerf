# hltGetConfiguration /users/swmukher/testv3/egm_ele5_open/V2 --setup /dev/CMSSW_12_1_0/GRun --globaltag auto:run3_hlt --input /store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/497/00000/00C024D9-C893-E811-BE8B-FA163E085754.root --data --process MYHLT --unprescale --max-events 20 --output none --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2018Input,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev

# /users/swmukher/testv3/egm_ele5_open/V2 (CMSSW_12_1_0)

import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')
#options.inputFiles = 'bob','peter'

options.parseArguments()

#print(options.inputFiles)


print(options.outputFile)


process = cms.Process( "MYHLT" )
process.load("setup_dev_CMSSW_12_1_0_GRun_cff")

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/swmukher/testv3/egm_ele5_open/V2')
)

process.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    verbose = cms.untracked.bool( False ),
    toGet = cms.VPSet( 
    )
)
process.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
process.hltPSetMap = cms.EDProducer( "ParameterSetBlobProducer" )
process.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    FedIds = cms.vint32( 1404 ),
    Setup = cms.string( "stage2::GTSetup" ),
    FWId = cms.uint32( 0 ),
    DmxFWId = cms.uint32( 0 ),
    FWOverride = cms.bool( False ),
    TMTCheck = cms.bool( True ),
    CTP7 = cms.untracked.bool( False ),
    MTF7 = cms.untracked.bool( False ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    debug = cms.untracked.bool( False ),
    MinFeds = cms.uint32( 0 )
)
process.hltGtStage2ObjectMap = cms.EDProducer( "L1TGlobalProducer",
    MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    AlgoBlkInputTag = cms.InputTag( "hltGtStage2Digis" ),
    GetPrescaleColumnFromData = cms.bool( False ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    RequireMenuToMatchAlgoBlkInput = cms.bool( True ),
    AlgorithmTriggersUnmasked = cms.bool( True ),
    ProduceL1GtDaqRecord = cms.bool( True ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    EmulateBxInEvent = cms.int32( 1 ),
    L1DataBxInEvent = cms.int32( 5 ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    BstLengthBytes = cms.int32( -1 ),
    PrescaleSet = cms.uint32( 1 ),
    Verbosity = cms.untracked.int32( 0 ),
    PrintL1Menu = cms.untracked.bool( False ),
    TriggerMenuLuminosity = cms.string( "startup" ),
    PrescaleCSVFile = cms.string( "prescale_L1TGlobal.csv" )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    changeToCMSCoordinates = cms.bool( False ),
    maxZ = cms.double( 40.0 ),
    setSigmaZ = cms.double( 0.0 ),
    beamMode = cms.untracked.uint32( 11 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    maxRadius = cms.double( 2.0 ),
    useTransientRecord = cms.bool( False )
)
process.hltL1sSingleEGor = cms.EDFilter( "HLTL1TSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleLooseIsoEG26er2p5 OR L1_SingleLooseIsoEG26er1p5 OR L1_SingleLooseIsoEG28er2p5 OR L1_SingleLooseIsoEG28er2p1 OR L1_SingleLooseIsoEG28er1p5 OR L1_SingleLooseIsoEG30er2p5 OR L1_SingleLooseIsoEG30er1p5 OR L1_SingleEG26er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleIsoEG24er2p1 OR L1_SingleIsoEG26er2p1 OR L1_SingleIsoEG28er2p1 OR L1_SingleIsoEG30er2p1 OR L1_SingleIsoEG32er2p1 OR L1_SingleIsoEG26er2p5 OR L1_SingleIsoEG28er2p5 OR L1_SingleIsoEG30er2p5 OR L1_SingleIsoEG32er2p5 OR L1_SingleIsoEG34er2p5" ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' )
)
process.hltPreEle32WPTightGsf = cms.EDFilter( "HLTPrescaler",
    offset = cms.uint32( 0 ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltEcalDigis = cms.EDProducer( "EcalRawToDigi",
    tccUnpacking = cms.bool( True ),
    FedLabel = cms.InputTag( "listfeds" ),
    srpUnpacking = cms.bool( True ),
    syncCheck = cms.bool( True ),
    feIdCheck = cms.bool( True ),
    silentMode = cms.untracked.bool( True ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    eventPut = cms.bool( True ),
    numbTriggerTSamples = cms.int32( 1 ),
    numbXtalTSamples = cms.int32( 10 ),
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    FEDs = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    DoRegional = cms.bool( False ),
    feUnpacking = cms.bool( True ),
    forceToKeepFRData = cms.bool( False ),
    headerUnpacking = cms.bool( True ),
    memUnpacking = cms.bool( True )
)
process.hltEcalPreshowerDigis = cms.EDProducer( "ESRawToDigi",
    sourceTag = cms.InputTag( "rawDataCollector" ),
    debugMode = cms.untracked.bool( False ),
    InstanceES = cms.string( "" ),
    LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ),
    ESdigiCollection = cms.string( "" )
)
process.hltEcalUncalibRecHit = cms.EDProducer( "EcalUncalibRecHitProducer",
    EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    EBhitCollection = cms.string( "EcalUncalibRecHitsEB" ),
    algo = cms.string( "EcalUncalibRecHitWorkerMultiFit" ),
    algoPSet = cms.PSet( 
      ebSpikeThreshold = cms.double( 1.042 ),
      EBtimeFitLimits_Upper = cms.double( 1.4 ),
      EEtimeFitLimits_Lower = cms.double( 0.2 ),
      timealgo = cms.string( "None" ),
      EBtimeNconst = cms.double( 28.5 ),
      prefitMaxChiSqEE = cms.double( 10.0 ),
      outOfTimeThresholdGain12mEB = cms.double( 5.0 ),
      outOfTimeThresholdGain12mEE = cms.double( 1000.0 ),
      EEtimeFitParameters = cms.vdouble( -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 140.7432, -75.41106, 16.20277 ),
      prefitMaxChiSqEB = cms.double( 25.0 ),
      simplifiedNoiseModelForGainSwitch = cms.bool( True ),
      EBtimeFitParameters = cms.vdouble( -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 91.01147, -50.35761, 11.05621 ),
      selectiveBadSampleCriteriaEB = cms.bool( False ),
      dynamicPedestalsEB = cms.bool( False ),
      useLumiInfoRunHeader = cms.bool( False ),
      EBamplitudeFitParameters = cms.vdouble( 1.138, 1.652 ),
      doPrefitEE = cms.bool( False ),
      dynamicPedestalsEE = cms.bool( False ),
      selectiveBadSampleCriteriaEE = cms.bool( False ),
      outOfTimeThresholdGain61pEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain61pEB = cms.double( 5.0 ),
      activeBXs = cms.vint32( -5, -4, -3, -2, -1, 0, 1, 2, 3, 4 ),
      EcalPulseShapeParameters = cms.PSet( 
        EEPulseShapeTemplate = cms.vdouble( 0.116442, 0.756246, 1.0, 0.897182, 0.686831, 0.491506, 0.344111, 0.245731, 0.174115, 0.123361, 0.0874288, 0.061957 ),
        EEdigiCollection = cms.string( "" ),
        EcalPreMixStage2 = cms.bool( False ),
        EcalPreMixStage1 = cms.bool( False ),
        EBPulseShapeCovariance = cms.vdouble( 3.001E-6, 1.233E-5, 0.0, -4.416E-6, -4.571E-6, -3.614E-6, -2.636E-6, -1.286E-6, -8.41E-7, -5.296E-7, 0.0, 0.0, 1.233E-5, 6.154E-5, 0.0, -2.2E-5, -2.309E-5, -1.838E-5, -1.373E-5, -7.334E-6, -5.088E-6, -3.745E-6, -2.428E-6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -4.416E-6, -2.2E-5, 0.0, 8.319E-6, 8.545E-6, 6.792E-6, 5.059E-6, 2.678E-6, 1.816E-6, 1.223E-6, 8.245E-7, 5.589E-7, -4.571E-6, -2.309E-5, 0.0, 8.545E-6, 9.182E-6, 7.219E-6, 5.388E-6, 2.853E-6, 1.944E-6, 1.324E-6, 9.083E-7, 6.335E-7, -3.614E-6, -1.838E-5, 0.0, 6.792E-6, 7.219E-6, 6.016E-6, 4.437E-6, 2.385E-6, 1.636E-6, 1.118E-6, 7.754E-7, 5.556E-7, -2.636E-6, -1.373E-5, 0.0, 5.059E-6, 5.388E-6, 4.437E-6, 3.602E-6, 1.917E-6, 1.322E-6, 9.079E-7, 6.529E-7, 4.752E-7, -1.286E-6, -7.334E-6, 0.0, 2.678E-6, 2.853E-6, 2.385E-6, 1.917E-6, 1.375E-6, 9.1E-7, 6.455E-7, 4.693E-7, 3.657E-7, -8.41E-7, -5.088E-6, 0.0, 1.816E-6, 1.944E-6, 1.636E-6, 1.322E-6, 9.1E-7, 9.115E-7, 6.062E-7, 4.436E-7, 3.422E-7, -5.296E-7, -3.745E-6, 0.0, 1.223E-6, 1.324E-6, 1.118E-6, 9.079E-7, 6.455E-7, 6.062E-7, 7.217E-7, 4.862E-7, 3.768E-7, 0.0, -2.428E-6, 0.0, 8.245E-7, 9.083E-7, 7.754E-7, 6.529E-7, 4.693E-7, 4.436E-7, 4.862E-7, 6.509E-7, 4.418E-7, 0.0, 0.0, 0.0, 5.589E-7, 6.335E-7, 5.556E-7, 4.752E-7, 3.657E-7, 3.422E-7, 3.768E-7, 4.418E-7, 6.142E-7 ),
        ESdigiCollection = cms.string( "" ),
        EBdigiCollection = cms.string( "" ),
        EBCorrNoiseMatrixG01 = cms.vdouble( 1.0, 0.73354, 0.64442, 0.58851, 0.55425, 0.53082, 0.51916, 0.51097, 0.50732, 0.50409 ),
        EBCorrNoiseMatrixG12 = cms.vdouble( 1.0, 0.71073, 0.55721, 0.46089, 0.40449, 0.35931, 0.33924, 0.32439, 0.31581, 0.30481 ),
        EBCorrNoiseMatrixG06 = cms.vdouble( 1.0, 0.70946, 0.58021, 0.49846, 0.45006, 0.41366, 0.39699, 0.38478, 0.37847, 0.37055 ),
        EEPulseShapeCovariance = cms.vdouble( 3.941E-5, 3.333E-5, 0.0, -1.449E-5, -1.661E-5, -1.424E-5, -1.183E-5, -6.842E-6, -4.915E-6, -3.411E-6, 0.0, 0.0, 3.333E-5, 2.862E-5, 0.0, -1.244E-5, -1.431E-5, -1.233E-5, -1.032E-5, -5.883E-6, -4.154E-6, -2.902E-6, -2.128E-6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.449E-5, -1.244E-5, 0.0, 5.84E-6, 6.649E-6, 5.72E-6, 4.812E-6, 2.708E-6, 1.869E-6, 1.33E-6, 9.186E-7, 6.446E-7, -1.661E-5, -1.431E-5, 0.0, 6.649E-6, 7.966E-6, 6.898E-6, 5.794E-6, 3.157E-6, 2.184E-6, 1.567E-6, 1.084E-6, 7.575E-7, -1.424E-5, -1.233E-5, 0.0, 5.72E-6, 6.898E-6, 6.341E-6, 5.347E-6, 2.859E-6, 1.991E-6, 1.431E-6, 9.839E-7, 6.886E-7, -1.183E-5, -1.032E-5, 0.0, 4.812E-6, 5.794E-6, 5.347E-6, 4.854E-6, 2.628E-6, 1.809E-6, 1.289E-6, 9.02E-7, 6.146E-7, -6.842E-6, -5.883E-6, 0.0, 2.708E-6, 3.157E-6, 2.859E-6, 2.628E-6, 1.863E-6, 1.296E-6, 8.882E-7, 6.108E-7, 4.283E-7, -4.915E-6, -4.154E-6, 0.0, 1.869E-6, 2.184E-6, 1.991E-6, 1.809E-6, 1.296E-6, 1.217E-6, 8.669E-7, 5.751E-7, 3.882E-7, -3.411E-6, -2.902E-6, 0.0, 1.33E-6, 1.567E-6, 1.431E-6, 1.289E-6, 8.882E-7, 8.669E-7, 9.522E-7, 6.717E-7, 4.293E-7, 0.0, -2.128E-6, 0.0, 9.186E-7, 1.084E-6, 9.839E-7, 9.02E-7, 6.108E-7, 5.751E-7, 6.717E-7, 7.911E-7, 5.493E-7, 0.0, 0.0, 0.0, 6.446E-7, 7.575E-7, 6.886E-7, 6.146E-7, 4.283E-7, 3.882E-7, 4.293E-7, 5.493E-7, 7.027E-7 ),
        EBPulseShapeTemplate = cms.vdouble( 0.0113979, 0.758151, 1.0, 0.887744, 0.673548, 0.474332, 0.319561, 0.215144, 0.147464, 0.101087, 0.0693181, 0.0475044 ),
        EECorrNoiseMatrixG01 = cms.vdouble( 1.0, 0.72698, 0.62048, 0.55691, 0.51848, 0.49147, 0.47813, 0.47007, 0.46621, 0.46265 ),
        EECorrNoiseMatrixG12 = cms.vdouble( 1.0, 0.71373, 0.44825, 0.30152, 0.21609, 0.14786, 0.11772, 0.10165, 0.09465, 0.08098 ),
        UseLCcorrection = cms.untracked.bool( True ),
        EECorrNoiseMatrixG06 = cms.vdouble( 1.0, 0.71217, 0.47464, 0.34056, 0.26282, 0.20287, 0.17734, 0.16256, 0.15618, 0.14443 )
      ),
      doPrefitEB = cms.bool( False ),
      addPedestalUncertaintyEE = cms.double( 0.0 ),
      addPedestalUncertaintyEB = cms.double( 0.0 ),
      gainSwitchUseMaxSampleEB = cms.bool( True ),
      EEtimeNconst = cms.double( 31.8 ),
      EEamplitudeFitParameters = cms.vdouble( 1.89, 1.4 ),
      chi2ThreshEE_ = cms.double( 50.0 ),
      eePulseShape = cms.vdouble( 5.2E-5, -5.26E-5, 6.66E-5, 0.1168, 0.7575, 1.0, 0.8876, 0.6732, 0.4741, 0.3194 ),
      outOfTimeThresholdGain12pEB = cms.double( 5.0 ),
      gainSwitchUseMaxSampleEE = cms.bool( False ),
      mitigateBadSamplesEB = cms.bool( False ),
      outOfTimeThresholdGain12pEE = cms.double( 1000.0 ),
      ebPulseShape = cms.vdouble( 5.2E-5, -5.26E-5, 6.66E-5, 0.1168, 0.7575, 1.0, 0.8876, 0.6732, 0.4741, 0.3194 ),
      ampErrorCalculation = cms.bool( False ),
      mitigateBadSamplesEE = cms.bool( False ),
      amplitudeThresholdEB = cms.double( 10.0 ),
      kPoorRecoFlagEB = cms.bool( True ),
      amplitudeThresholdEE = cms.double( 10.0 ),
      EBtimeFitLimits_Lower = cms.double( 0.2 ),
      kPoorRecoFlagEE = cms.bool( False ),
      EEtimeFitLimits_Upper = cms.double( 1.4 ),
      outOfTimeThresholdGain61mEE = cms.double( 1000.0 ),
      EEtimeConstantTerm = cms.double( 1.0 ),
      EBtimeConstantTerm = cms.double( 0.6 ),
      chi2ThreshEB_ = cms.double( 65.0 ),
      outOfTimeThresholdGain61mEB = cms.double( 5.0 )
    )
)
process.hltEcalDetIdToBeRecovered = cms.EDProducer( "EcalDetIdToBeRecoveredProducer",
    ebIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebDetIdToBeRecovered = cms.string( "ebDetId" ),
    integrityTTIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityTTIdErrors' ),
    eeIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    ebFEToBeRecovered = cms.string( "ebFE" ),
    ebIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    eeDetIdToBeRecovered = cms.string( "eeDetId" ),
    eeIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    eeIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    ebSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    eeFEToBeRecovered = cms.string( "eeFE" ),
    integrityBlockSizeErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityBlockSizeErrors' ),
    eeSrFlagCollection = cms.InputTag( "hltEcalDigis" )
)
process.hltEcalRecHit = cms.EDProducer( "EcalRecHitProducer",
    recoverEEVFE = cms.bool( False ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    recoverEBIsolatedChannels = cms.bool( False ),
    recoverEBVFE = cms.bool( False ),
    laserCorrection = cms.bool( True ),
    EBLaserMIN = cms.double( 0.5 ),
    killDeadChannels = cms.bool( True ),
    dbStatusToBeExcludedEB = cms.vint32( 14, 78, 142 ),
    EEuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEE' ),
    dbStatusToBeExcludedEE = cms.vint32( 14, 78, 142 ),
    EELaserMIN = cms.double( 0.5 ),
    ebFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebFE' ),
    cleaningConfig = cms.PSet( 
      e6e2thresh = cms.double( 0.04 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 ),
      cThreshold_endcap = cms.double( 15.0 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      cThreshold_double = cms.double( 10.0 )
    ),
    logWarningEtThreshold_EE_FE = cms.double( 50.0 ),
    eeDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeDetId' ),
    recoverEBFE = cms.bool( True ),
    eeFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeFE' ),
    ebDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebDetId' ),
    singleChannelRecoveryThreshold = cms.double( 8.0 ),
    sum8ChannelRecoveryThreshold = cms.double( 0.0 ),
    bdtWeightFileNoCracks = cms.FileInPath( "RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_noCracks_ZskimData2017_v1.xml" ),
    bdtWeightFileCracks = cms.FileInPath( "RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_onlyCracks_ZskimData2017_v1.xml" ),
    ChannelStatusToBeExcluded = cms.vstring(  ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    triggerPrimitiveDigiCollection = cms.InputTag( 'hltEcalDigis','EcalTriggerPrimitives' ),
    recoverEEFE = cms.bool( True ),
    singleChannelRecoveryMethod = cms.string( "NeuralNetworks" ),
    EBLaserMAX = cms.double( 3.0 ),
    flagsMapDBReco = cms.PSet( 
      kGood = cms.vstring( 'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy' ),
      kNeighboursRecovered = cms.vstring( 'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE' ),
      kDead = cms.vstring( 'kNoDataNoTP' ),
      kNoisy = cms.vstring( 'kNNoisy',
        'kFixedG6',
        'kFixedG1' ),
      kTowerRecovered = cms.vstring( 'kDeadFE' )
    ),
    EBuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    algoRecover = cms.string( "EcalRecHitWorkerRecover" ),
    algo = cms.string( "EcalRecHitWorkerSimple" ),
    EELaserMAX = cms.double( 8.0 ),
    logWarningEtThreshold_EB_FE = cms.double( 50.0 ),
    recoverEEIsolatedChannels = cms.bool( False ),
    skipTimeCalib = cms.bool( True )
)
process.hltEcalPreshowerRecHit = cms.EDProducer( "ESRecHitProducer",
    ESrechitCollection = cms.string( "EcalRecHitsES" ),
    ESdigiCollection = cms.InputTag( "hltEcalPreshowerDigis" ),
    algo = cms.string( "ESRecHitWorker" ),
    ESRecoAlgo = cms.int32( 0 )
)
process.hltRechitInRegionsECAL = cms.EDProducer( "HLTEcalRecHitInAllL1RegionsProducer",
    productLabels = cms.vstring( 'EcalRecHitsEB',
      'EcalRecHitsEE' ),
    recHitLabels = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    l1InputRegions = cms.VPSet( 
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "EGamma" ),
        minEt = cms.double( 5.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Jet' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Jet" ),
        minEt = cms.double( 170.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Tau' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Tau" ),
        minEt = cms.double( 100.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      )
    )
)
process.hltRechitInRegionsES = cms.EDProducer( "HLTEcalRecHitInAllL1RegionsProducer",
    productLabels = cms.vstring( 'EcalRecHitsES' ),
    recHitLabels = cms.VInputTag( 'hltEcalPreshowerRecHit:EcalRecHitsES' ),
    l1InputRegions = cms.VPSet( 
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "EGamma" ),
        minEt = cms.double( 5.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Jet' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Jet" ),
        minEt = cms.double( 170.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Tau' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Tau" ),
        minEt = cms.double( 100.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      )
    )
)
process.hltParticleFlowRecHitECALL1Seeded = cms.EDProducer( "PFRecHitProducer",
    navigator = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitECALNavigator" )
    ),
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEB' ),
        srFlags = cms.InputTag( "" ),
        name = cms.string( "PFEBRecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  name = cms.string( "PFRecHitQTestDBThreshold" ),
            applySelectionsToAllCrystals = cms.bool( True )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        )
      ),
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEE' ),
        srFlags = cms.InputTag( "" ),
        name = cms.string( "PFEERecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  name = cms.string( "PFRecHitQTestDBThreshold" ),
            applySelectionsToAllCrystals = cms.bool( True )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        )
      )
    )
)
process.hltParticleFlowRecHitPSL1Seeded = cms.EDProducer( "PFRecHitProducer",
    navigator = cms.PSet(  name = cms.string( "PFRecHitPreshowerNavigator" ) ),
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsES','EcalRecHitsES' ),
        name = cms.string( "PFPSRecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 7.0E-6 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          )
        )
      )
    )
)
process.hltParticleFlowClusterPSL1Seeded = cms.EDProducer( "PFClusterProducer",
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitPSL1Seeded" ),
    recHitCleaners = cms.VPSet( 
    ),
    seedCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 4 )
    ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( False )
    ),
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 6.0E-5 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 50 ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS2" )
        )
      ),
      showerSigma = cms.double( 0.3 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet(  ),
    energyCorrector = cms.PSet(  )
)
process.hltParticleFlowClusterECALUncorrectedL1Seeded = cms.EDProducer( "PFClusterProducer",
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitECALL1Seeded" ),
    recHitCleaners = cms.VPSet( 
    ),
    seedCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThresholdPt = cms.double( 0.15 ),
          seedingThreshold = cms.double( 0.6 ),
          detector = cms.string( "ECAL_ENDCAP" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 0.23 ),
          detector = cms.string( "ECAL_BARREL" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 8 )
    ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.08 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.3 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( True )
    ),
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 9 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet( 
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet( 
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      maxIterations = cms.uint32( 50 ),
      positionCalcForConvergence = cms.PSet( 
        minAllowedNormalization = cms.double( 0.0 ),
        T0_ES = cms.double( 1.2 ),
        algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
        T0_EE = cms.double( 3.1 ),
        T0_EB = cms.double( 7.4 ),
        X0 = cms.double( 0.89 ),
        minFractionInCalc = cms.double( 0.0 ),
        W0 = cms.double( 4.2 )
      ),
      allCellsPositionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet( 
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet( 
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  recHitEnergyNorm = cms.double( 0.08 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 0.3 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      showerSigma = cms.double( 1.5 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet( 
      minAllowedNormalization = cms.double( 0.0 ),
      T0_ES = cms.double( 1.2 ),
      algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
      T0_EE = cms.double( 3.1 ),
      T0_EB = cms.double( 7.4 ),
      X0 = cms.double( 0.89 ),
      minFractionInCalc = cms.double( 0.0 ),
      W0 = cms.double( 4.2 )
    ),
    energyCorrector = cms.PSet(  )
)
process.hltParticleFlowClusterECALL1Seeded = cms.EDProducer( "CorrectedECALPFClusterProducer",
    minimumPSEnergy = cms.double( 0.0 ),
    skipPS = cms.bool( False ),
    inputPS = cms.InputTag( "hltParticleFlowClusterPSL1Seeded" ),
    energyCorrector = cms.PSet(  applyCrackCorrections = cms.bool( False ) ),
    inputECAL = cms.InputTag( "hltParticleFlowClusterECALUncorrectedL1Seeded" )
)
process.hltParticleFlowSuperClusterECALL1Seeded = cms.EDProducer( "PFECALSuperClusterProducer",
    PFSuperClusterCollectionEndcap = cms.string( "hltParticleFlowSuperClusterECALEndcap" ),
    doSatelliteClusterMerge = cms.bool( False ),
    thresh_PFClusterBarrel = cms.double( 0.5 ),
    PFBasicClusterCollectionBarrel = cms.string( "hltParticleFlowBasicClusterECALBarrel" ),
    useRegression = cms.bool( True ),
    satelliteMajorityFraction = cms.double( 0.5 ),
    thresh_PFClusterEndcap = cms.double( 0.5 ),
    ESAssociation = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    PFBasicClusterCollectionPreshower = cms.string( "hltParticleFlowBasicClusterECALPreshower" ),
    use_preshower = cms.bool( True ),
    verbose = cms.untracked.bool( False ),
    thresh_SCEt = cms.double( 4.0 ),
    etawidth_SuperClusterEndcap = cms.double( 0.04 ),
    phiwidth_SuperClusterEndcap = cms.double( 0.6 ),
    useDynamicDPhiWindow = cms.bool( True ),
    PFSuperClusterCollectionBarrel = cms.string( "hltParticleFlowSuperClusterECALBarrel" ),
    regressionConfig = cms.PSet( 
      uncertaintyKeyEB = cms.string( "pfscecal_EBUncertainty_online" ),
      ecalRecHitsEE = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
      ecalRecHitsEB = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      regressionKeyEE = cms.string( "pfscecal_EECorrection_online" ),
      regressionKeyEB = cms.string( "pfscecal_EBCorrection_online" ),
      uncertaintyKeyEE = cms.string( "pfscecal_EEUncertainty_online" ),
      isHLT = cms.bool( True )
    ),
    applyCrackCorrections = cms.bool( False ),
    satelliteClusterSeedThreshold = cms.double( 50.0 ),
    etawidth_SuperClusterBarrel = cms.double( 0.04 ),
    PFBasicClusterCollectionEndcap = cms.string( "hltParticleFlowBasicClusterECALEndcap" ),
    PFClusters = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    thresh_PFClusterSeedBarrel = cms.double( 1.0 ),
    ClusteringType = cms.string( "Mustache" ),
    EnergyWeight = cms.string( "Raw" ),
    BeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    thresh_PFClusterSeedEndcap = cms.double( 1.0 ),
    phiwidth_SuperClusterBarrel = cms.double( 0.6 ),
    thresh_PFClusterES = cms.double( 0.5 ),
    seedThresholdIsET = cms.bool( True ),
    isOOTCollection = cms.bool( False ),
    barrelRecHits = cms.InputTag( 'ecalRecHit','EcalRecHitsEE' ),
    endcapRecHits = cms.InputTag( 'ecalRecHit','EcalRecHitsEB' ),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string( "hltParticleFlowSuperClusterECALEndcapWithPreshower" ),
    dropUnseedable = cms.bool( False )
)
process.hltEgammaCandidates = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scHybridBarrelProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALBarrel' ),
    scIslandEndcapProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltEgammaTriggerFilterObjectWrapper = cms.EDFilter( "HLTEgammaTriggerFilterObjectWrapper",
    saveTags = cms.bool( True ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    candNonIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    doIsolated = cms.bool( False )
)
process.hltEGL1SingleEGOrFilter = cms.EDFilter( "HLTEgammaL1TMatchFilterRegional",
    saveTags = cms.bool( True ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    l1IsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1SeedFilterTag = cms.InputTag( "hltL1sSingleEGor" ),
    l1CenJetsTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    l1TausTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
process.hltEG5L1SingleEGOrEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEGOrFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEB = cms.double( 5.0 ),
    etcutEE = cms.double( 5.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEgammaClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    ecalRechitEB = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEE' ),
    isIeta = cms.bool( True ),
    multThresEB = cms.double( 1.0 ),
    multThresEE = cms.double( 1.25 )
)
process.hltEle5WPTightClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    saveTags = cms.bool( True ),
    candTag = cms.InputTag( "hltEG5L1SingleEGOrEtFilter" ),
    varTag = cms.InputTag( 'hltEgammaClusterShape','sigmaIEtaIEta5x5' ),
    rhoTag = cms.InputTag( "" ),
    energyLowEdges = cms.vdouble( 0.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.vdouble( 0.011 ),
    thrRegularEE = cms.vdouble( 0.0305 ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrOverE2EE = cms.vdouble( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doRhoCorrection = cms.bool( False ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" )
)
process.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
    HcalFirstFED = cms.untracked.int32( 700 ),
    firstSample = cms.int32( 0 ),
    lastSample = cms.int32( 9 ),
    FilterDataQuality = cms.bool( True ),
    FEDs = cms.untracked.vint32(  ),
    UnpackZDC = cms.untracked.bool( True ),
    UnpackCalib = cms.untracked.bool( True ),
    UnpackUMNio = cms.untracked.bool( True ),
    UnpackTTP = cms.untracked.bool( False ),
    silent = cms.untracked.bool( True ),
    saveQIE10DataNSamples = cms.untracked.vint32(  ),
    saveQIE10DataTags = cms.untracked.vstring(  ),
    saveQIE11DataNSamples = cms.untracked.vint32(  ),
    saveQIE11DataTags = cms.untracked.vstring(  ),
    ComplainEmptyData = cms.untracked.bool( False ),
    UnpackerMode = cms.untracked.int32( 0 ),
    ExpectedOrbitMessageTime = cms.untracked.int32( -1 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ElectronicsMap = cms.string( "" )
)
process.hltHbhereco = cms.EDProducer( "HBHEPhase1Reconstructor",
    digiLabelQIE8 = cms.InputTag( "hltHcalDigis" ),
    processQIE8 = cms.bool( False ),
    digiLabelQIE11 = cms.InputTag( "hltHcalDigis" ),
    processQIE11 = cms.bool( True ),
    tsFromDB = cms.bool( False ),
    recoParamsFromDB = cms.bool( True ),
    saveEffectivePedestal = cms.bool( True ),
    dropZSmarkedPassed = cms.bool( True ),
    makeRecHits = cms.bool( True ),
    saveInfos = cms.bool( False ),
    saveDroppedInfos = cms.bool( False ),
    use8ts = cms.bool( True ),
    sipmQTSShift = cms.int32( 0 ),
    sipmQNTStoSum = cms.int32( 3 ),
    algorithm = cms.PSet( 
      ts4Thresh = cms.double( 0.0 ),
      meanTime = cms.double( 0.0 ),
      nnlsThresh = cms.double( 1.0E-11 ),
      nMaxItersMin = cms.int32( 50 ),
      timeSigmaSiPM = cms.double( 2.5 ),
      applyTimeSlew = cms.bool( True ),
      timeSlewParsType = cms.int32( 3 ),
      ts4Max = cms.vdouble( 100.0, 20000.0, 30000.0 ),
      samplesToAdd = cms.int32( 2 ),
      deltaChiSqThresh = cms.double( 0.001 ),
      applyTimeConstraint = cms.bool( False ),
      timeSigmaHPD = cms.double( 5.0 ),
      useMahi = cms.bool( True ),
      correctForPhaseContainment = cms.bool( True ),
      respCorrM3 = cms.double( 1.0 ),
      pulseJitter = cms.double( 1.0 ),
      applyPedConstraint = cms.bool( False ),
      fitTimes = cms.int32( 1 ),
      nMaxItersNNLS = cms.int32( 500 ),
      applyTimeSlewM3 = cms.bool( True ),
      meanPed = cms.double( 0.0 ),
      ts4Min = cms.double( 0.0 ),
      applyPulseJitter = cms.bool( False ),
      useM2 = cms.bool( False ),
      timeMin = cms.double( -12.5 ),
      useM3 = cms.bool( False ),
      chiSqSwitch = cms.double( -1.0 ),
      dynamicPed = cms.bool( False ),
      tdcTimeShift = cms.double( 0.0 ),
      correctionPhaseNS = cms.double( 6.0 ),
      firstSampleShift = cms.int32( 0 ),
      activeBXs = cms.vint32( -3, -2, -1, 0, 1, 2, 3, 4 ),
      ts4chi2 = cms.vdouble( 15.0, 15.0 ),
      timeMax = cms.double( 12.5 ),
      Class = cms.string( "SimpleHBHEPhase1Algo" ),
      calculateArrivalTime = cms.bool( False ),
      applyLegacyHBMCorrection = cms.bool( False )
    ),
    algoConfigClass = cms.string( "" ),
    setNegativeFlagsQIE8 = cms.bool( False ),
    setNegativeFlagsQIE11 = cms.bool( False ),
    setNoiseFlagsQIE8 = cms.bool( False ),
    setNoiseFlagsQIE11 = cms.bool( False ),
    setPulseShapeFlagsQIE8 = cms.bool( False ),
    setPulseShapeFlagsQIE11 = cms.bool( False ),
    setLegacyFlagsQIE8 = cms.bool( False ),
    setLegacyFlagsQIE11 = cms.bool( False ),
    flagParametersQIE8 = cms.PSet( 
      hitEnergyMinimum = cms.double( 1.0 ),
      pulseShapeParameterSets = cms.VPSet( 
        cms.PSet(  pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )        )
      ),
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 )
    ),
    flagParametersQIE11 = cms.PSet(  ),
    pulseShapeParametersQIE8 = cms.PSet( 
      UseDualFit = cms.bool( True ),
      LinearCut = cms.vdouble( -3.0, -0.054, -0.054 ),
      TriangleIgnoreSlow = cms.bool( False ),
      TS4TS5LowerThreshold = cms.vdouble( 100.0, 120.0, 160.0, 200.0, 300.0, 500.0 ),
      LinearThreshold = cms.vdouble( 20.0, 100.0, 100000.0 ),
      RightSlopeSmallCut = cms.vdouble( 1.08, 1.16, 1.16 ),
      TS4TS5UpperThreshold = cms.vdouble( 70.0, 90.0, 100.0, 400.0 ),
      TS3TS4ChargeThreshold = cms.double( 70.0 ),
      R45PlusOneRange = cms.double( 0.2 ),
      TS4TS5LowerCut = cms.vdouble( -1.0, -0.7, -0.5, -0.4, -0.3, 0.1 ),
      RightSlopeThreshold = cms.vdouble( 250.0, 400.0, 100000.0 ),
      TS3TS4UpperChargeThreshold = cms.double( 20.0 ),
      MinimumChargeThreshold = cms.double( 20.0 ),
      RightSlopeCut = cms.vdouble( 5.0, 4.15, 4.15 ),
      RMS8MaxThreshold = cms.vdouble( 20.0, 100.0, 100000.0 ),
      MinimumTS4TS5Threshold = cms.double( 100.0 ),
      LeftSlopeThreshold = cms.vdouble( 250.0, 500.0, 100000.0 ),
      TS5TS6ChargeThreshold = cms.double( 70.0 ),
      TrianglePeakTS = cms.uint32( 10000 ),
      TS5TS6UpperChargeThreshold = cms.double( 20.0 ),
      RightSlopeSmallThreshold = cms.vdouble( 150.0, 200.0, 100000.0 ),
      RMS8MaxCut = cms.vdouble( -13.5, -11.5, -11.5 ),
      TS4TS5ChargeThreshold = cms.double( 70.0 ),
      R45MinusOneRange = cms.double( 0.2 ),
      LeftSlopeCut = cms.vdouble( 5.0, 2.55, 2.55 ),
      TS4TS5UpperCut = cms.vdouble( 1.0, 0.8, 0.75, 0.72 )
    ),
    pulseShapeParametersQIE11 = cms.PSet(  )
)
process.hltHfprereco = cms.EDProducer( "HFPreReconstructor",
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    dropZSmarkedPassed = cms.bool( True ),
    tsFromDB = cms.bool( False ),
    sumAllTimeSlices = cms.bool( False ),
    forceSOI = cms.int32( -1 ),
    soiShift = cms.int32( 0 )
)
process.hltHfreco = cms.EDProducer( "HFPhase1Reconstructor",
    inputLabel = cms.InputTag( "hltHfprereco" ),
    useChannelQualityFromDB = cms.bool( False ),
    checkChannelQualityForDepth3and4 = cms.bool( False ),
    algorithm = cms.PSet( 
      tfallIfNoTDC = cms.double( -101.0 ),
      triseIfNoTDC = cms.double( -100.0 ),
      rejectAllFailures = cms.bool( True ),
      energyWeights = cms.vdouble( 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 1.0 ),
      soiPhase = cms.uint32( 1 ),
      timeShift = cms.double( 0.0 ),
      tlimits = cms.vdouble( -1000.0, 1000.0, -1000.0, 1000.0 ),
      Class = cms.string( "HFFlexibleTimeCheck" )
    ),
    algoConfigClass = cms.string( "HFPhase1PMTParams" ),
    setNoiseFlags = cms.bool( True ),
    runHFStripFilter = cms.bool( False ),
    S9S1stat = cms.PSet( 
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      isS8S1 = cms.bool( False ),
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    S8S1stat = cms.PSet( 
      shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      isS8S1 = cms.bool( True ),
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    PETstat = cms.PSet( 
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_R_29 = cms.vdouble( 0.8 ),
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      short_R_29 = cms.vdouble( 0.8 ),
      long_R = cms.vdouble( 0.98 ),
      short_R = cms.vdouble( 0.8 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    HFStripFilter = cms.PSet( 
      timeMax = cms.double( 6.0 ),
      seedHitIetaMax = cms.int32( 35 ),
      gap = cms.int32( 2 ),
      verboseLevel = cms.untracked.int32( 10 ),
      wedgeCut = cms.double( 0.05 ),
      stripThreshold = cms.double( 40.0 ),
      maxStripTime = cms.double( 10.0 ),
      maxThreshold = cms.double( 100.0 ),
      lstrips = cms.int32( 2 )
    )
)
process.hltHoreco = cms.EDProducer( "HcalHitReconstructor",
    correctForPhaseContainment = cms.bool( True ),
    correctionPhaseNS = cms.double( 13.0 ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    Subdetector = cms.string( "HO" ),
    correctForTimeslew = cms.bool( True ),
    dropZSmarkedPassed = cms.bool( True ),
    firstSample = cms.int32( 4 ),
    samplesToAdd = cms.int32( 4 ),
    tsFromDB = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    useLeakCorrection = cms.bool( False ),
    dataOOTCorrectionName = cms.string( "" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    mcOOTCorrectionName = cms.string( "" ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    correctTiming = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    setNoiseFlags = cms.bool( False ),
    digiTimeFromDB = cms.bool( True ),
    setHSCPFlags = cms.bool( False ),
    setSaturationFlags = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    digistat = cms.PSet(  ),
    HFInWindowStat = cms.PSet(  ),
    S9S1stat = cms.PSet(  ),
    S8S1stat = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    hfTimingTrustParameters = cms.PSet(  )
)
process.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    HF2Weight = cms.double( 1.0 ),
    EBWeight = cms.double( 1.0 ),
    hfInput = cms.InputTag( "hltHfreco" ),
    EESumThreshold = cms.double( 0.45 ),
    HOThreshold0 = cms.double( 3.5 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HBGrid = cms.vdouble(  ),
    HBThreshold1 = cms.double( 0.1 ),
    HBThreshold2 = cms.double( 0.2 ),
    HBThreshold = cms.double( 0.3 ),
    EEWeights = cms.vdouble(  ),
    HF1Threshold = cms.double( 0.5 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    HEDWeight = cms.double( 1.0 ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HESWeight = cms.double( 1.0 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0E-99 ),
    EBThreshold = cms.double( 0.07 ),
    EEThreshold = cms.double( 0.3 ),
    UseEtEBTreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Threshold = cms.double( 0.85 ),
    HESThreshold1 = cms.double( 0.1 ),
    HESThreshold = cms.double( 0.2 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HESGrid = cms.vdouble(  ),
    HESWeights = cms.vdouble(  ),
    HEDThreshold1 = cms.double( 0.1 ),
    HEDThreshold = cms.double( 0.2 ),
    EcutTower = cms.double( -1000.0 ),
    HEDGrid = cms.vdouble(  ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    UseHcalRecoveredHits = cms.bool( False ),
    UseEcalRecoveredHits = cms.bool( False ),
    UseRejectedHitsOnly = cms.bool( False ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    missingHcalRescaleFactorForEcal = cms.double( 0.0 ),
    AllowMissingInputs = cms.bool( False ),
    HcalPhase = cms.int32( 1 )
)
process.hltFixedGridRhoFastjetAllCaloForMuons = cms.EDProducer( "FixedGridRhoProducerFastjet",
    pfCandidatesTag = cms.InputTag( "hltTowerMakerForAll" ),
    maxRapidity = cms.double( 2.5 ),
    gridSpacing = cms.double( 0.55 )
)
process.hltEgammaHoverE = cms.EDProducer( "EgammaHLTBcHcalIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    caloTowerProducer = cms.InputTag( "hltTowerMakerForAll" ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    doRhoCorrection = cms.bool( False ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    etMin = cms.double( 0.0 ),
    innerCone = cms.double( 0.0 ),
    outerCone = cms.double( 0.14 ),
    depth = cms.int32( -1 ),
    doEtSum = cms.bool( False ),
    useSingleTower = cms.bool( False ),
    effectiveAreas = cms.vdouble( 0.105, 0.17 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 )
)
process.hltEle5WPTightHEFilter = cms.EDFilter( "HLTEgammaGenericQuadraticEtaFilter",
    saveTags = cms.bool( True ),
    candTag = cms.InputTag( "hltEle5WPTightClusterShapeFilter" ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    rhoTag = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    energyLowEdges = cms.vdouble( 0.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    etaBoundaryEB12 = cms.double( 1.0 ),
    etaBoundaryEE12 = cms.double( 2.1 ),
    thrRegularEB1 = cms.vdouble( 0.75 ),
    thrRegularEE1 = cms.vdouble( 3.0 ),
    thrOverEEB1 = cms.vdouble( 0.03 ),
    thrOverEEE1 = cms.vdouble( 0.03 ),
    thrOverE2EB1 = cms.vdouble( 0.0 ),
    thrOverE2EE1 = cms.vdouble( 0.0 ),
    thrRegularEB2 = cms.vdouble( 2.25 ),
    thrRegularEE2 = cms.vdouble( 5.0 ),
    thrOverEEB2 = cms.vdouble( 0.03 ),
    thrOverEEE2 = cms.vdouble( 0.03 ),
    thrOverE2EB2 = cms.vdouble( 0.0 ),
    thrOverE2EE2 = cms.vdouble( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doRhoCorrection = cms.bool( True ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreas = cms.vdouble( 0.1, 0.1, 0.3, 0.5 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.0, 1.479, 2.1 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" )
)
process.hltEgammaEcalPFClusterIso = cms.EDProducer( "EgammaHLTEcalPFClusterIsolationProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    pfClusterProducer = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    doRhoCorrection = cms.bool( False ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    drMax = cms.double( 0.3 ),
    drVetoBarrel = cms.double( 0.0 ),
    drVetoEndcap = cms.double( 0.0 ),
    etaStripBarrel = cms.double( 0.0 ),
    etaStripEndcap = cms.double( 0.0 ),
    energyBarrel = cms.double( 0.0 ),
    energyEndcap = cms.double( 0.0 ),
    effectiveAreas = cms.vdouble( 0.29, 0.21 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 )
)
process.hltEle5WPTightEcalIsoFilter = cms.EDFilter( "HLTEgammaGenericQuadraticEtaFilter",
    saveTags = cms.bool( True ),
    candTag = cms.InputTag( "hltEle5WPTightHEFilter" ),
    varTag = cms.InputTag( "hltEgammaEcalPFClusterIso" ),
    rhoTag = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    energyLowEdges = cms.vdouble( 0.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    etaBoundaryEB12 = cms.double( 1.0 ),
    etaBoundaryEE12 = cms.double( 2.1 ),
    thrRegularEB1 = cms.vdouble( 1.75 ),
    thrRegularEE1 = cms.vdouble( 1.0 ),
    thrOverEEB1 = cms.vdouble( 0.03 ),
    thrOverEEE1 = cms.vdouble( 0.025 ),
    thrOverE2EB1 = cms.vdouble( 0.0 ),
    thrOverE2EE1 = cms.vdouble( 0.0 ),
    thrRegularEB2 = cms.vdouble( 1.75 ),
    thrRegularEE2 = cms.vdouble( 2.0 ),
    thrOverEEB2 = cms.vdouble( 0.03 ),
    thrOverEEE2 = cms.vdouble( 0.025 ),
    thrOverE2EB2 = cms.vdouble( 0.0 ),
    thrOverE2EE2 = cms.vdouble( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doRhoCorrection = cms.bool( True ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreas = cms.vdouble( 0.2, 0.2, 0.25, 0.3 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.0, 1.479, 2.1 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" )
)
process.hltParticleFlowRecHitHBHE = cms.EDProducer( "PFRecHitProducer",
    navigator = cms.PSet( 
      name = cms.string( "PFRecHitHCALDenseIdNavigator" ),
      hcalEnums = cms.vint32( 1, 2 )
    ),
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( "hltHbhereco" ),
        name = cms.string( "PFHBHERecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.8 ),
            name = cms.string( "PFRecHitQTestThreshold" ),
            cuts = cms.VPSet( 
              cms.PSet(  depth = cms.vint32( 1, 2, 3, 4 ),
                threshold = cms.vdouble( 0.1, 0.2, 0.3, 0.3 ),
                detectorEnum = cms.int32( 1 )
              ),
              cms.PSet(  depth = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
                threshold = cms.vdouble( 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2 ),
                detectorEnum = cms.int32( 2 )
              )
            )
          ),
          cms.PSet(  flags = cms.vstring( 'Standard' ),
            cleaningThresholds = cms.vdouble( 0.0 ),
            name = cms.string( "PFRecHitQTestHCALChannel" ),
            maxSeverities = cms.vint32( 11 )
          )
        )
      )
    )
)
process.hltParticleFlowClusterHBHE = cms.EDProducer( "PFClusterProducer",
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitHBHE" ),
    recHitCleaners = cms.VPSet( 
    ),
    seedCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          depths = cms.vint32( 1, 2, 3, 4 ),
          seedingThreshold = cms.vdouble( 0.125, 0.25, 0.35, 0.35 ),
          seedingThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
          seedingThreshold = cms.vdouble( 0.1375, 0.275, 0.275, 0.275, 0.275, 0.275, 0.275 ),
          seedingThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 4 )
    ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          depths = cms.vint32( 1, 2, 3, 4 ),
          gatheringThreshold = cms.vdouble( 0.1, 0.2, 0.3, 0.3 ),
          gatheringThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
          gatheringThreshold = cms.vdouble( 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2 ),
          gatheringThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( True )
    ),
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominatorByDetector = cms.VPSet( 
          cms.PSet(  depths = cms.vint32( 1, 2, 3, 4 ),
            detector = cms.string( "HCAL_BARREL1" ),
            logWeightDenominator = cms.vdouble( 0.1, 0.2, 0.3, 0.3 )
          ),
          cms.PSet(  depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
            detector = cms.string( "HCAL_ENDCAP" ),
            logWeightDenominator = cms.vdouble( 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2 )
          )
        )
      ),
      maxIterations = cms.uint32( 50 ),
      minChi2Prob = cms.double( 0.0 ),
      allCellsPositionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominatorByDetector = cms.VPSet( 
          cms.PSet(  depths = cms.vint32( 1, 2, 3, 4 ),
            detector = cms.string( "HCAL_BARREL1" ),
            logWeightDenominator = cms.vdouble( 0.1, 0.2, 0.3, 0.3 )
          ),
          cms.PSet(  depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
            detector = cms.string( "HCAL_ENDCAP" ),
            logWeightDenominator = cms.vdouble( 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2 )
          )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          depths = cms.vint32( 1, 2, 3, 4 ),
          recHitEnergyNorm = cms.vdouble( 0.1, 0.2, 0.3, 0.3 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
          recHitEnergyNorm = cms.vdouble( 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2 )
        )
      ),
      maxNSigmaTime = cms.double( 10.0 ),
      showerSigma = cms.double( 10.0 ),
      timeSigmaEE = cms.double( 10.0 ),
      clusterTimeResFromSeed = cms.bool( False ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      timeResolutionCalcBarrel = cms.PSet( 
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 6.0 ),
        noiseTerm = cms.double( 21.86 ),
        constantTermLowE = cms.double( 4.24 ),
        noiseTermLowE = cms.double( 8.0 ),
        threshHighE = cms.double( 15.0 ),
        constantTerm = cms.double( 2.82 )
      ),
      timeResolutionCalcEndcap = cms.PSet( 
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 6.0 ),
        noiseTerm = cms.double( 21.86 ),
        constantTermLowE = cms.double( 4.24 ),
        noiseTermLowE = cms.double( 8.0 ),
        threshHighE = cms.double( 15.0 ),
        constantTerm = cms.double( 2.82 )
      ),
      timeSigmaEB = cms.double( 10.0 )
    ),
    positionReCalc = cms.PSet(  ),
    energyCorrector = cms.PSet(  )
)
process.hltParticleFlowClusterHCAL = cms.EDProducer( "PFMultiDepthClusterProducer",
    clustersSource = cms.InputTag( "hltParticleFlowClusterHBHE" ),
    pfClusterBuilder = cms.PSet( 
      allCellsPositionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominatorByDetector = cms.VPSet( 
          cms.PSet(  depths = cms.vint32( 1, 2, 3, 4 ),
            detector = cms.string( "HCAL_BARREL1" ),
            logWeightDenominator = cms.vdouble( 0.1, 0.2, 0.3, 0.3 )
          ),
          cms.PSet(  depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
            detector = cms.string( "HCAL_ENDCAP" ),
            logWeightDenominator = cms.vdouble( 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2 )
          )
        )
      ),
      algoName = cms.string( "PFMultiDepthClusterizer" ),
      nSigmaPhi = cms.double( 2.0 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      nSigmaEta = cms.double( 2.0 )
    ),
    positionReCalc = cms.PSet(  ),
    energyCorrector = cms.PSet(  )
)
process.hltEgammaHcalPFClusterIso = cms.EDProducer( "EgammaHLTHcalPFClusterIsolationProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    pfClusterProducerHCAL = cms.InputTag( "hltParticleFlowClusterHCAL" ),
    useHF = cms.bool( False ),
    pfClusterProducerHFEM = cms.InputTag( "" ),
    pfClusterProducerHFHAD = cms.InputTag( "" ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    doRhoCorrection = cms.bool( False ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    drMax = cms.double( 0.3 ),
    drVetoBarrel = cms.double( 0.0 ),
    drVetoEndcap = cms.double( 0.0 ),
    etaStripBarrel = cms.double( 0.0 ),
    etaStripEndcap = cms.double( 0.0 ),
    energyBarrel = cms.double( 0.0 ),
    energyEndcap = cms.double( 0.0 ),
    useEt = cms.bool( True ),
    effectiveAreas = cms.vdouble( 0.2, 0.25 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 )
)
process.hltEle5WPTightHcalIsoFilter = cms.EDFilter( "HLTEgammaGenericQuadraticEtaFilter",
    saveTags = cms.bool( True ),
    candTag = cms.InputTag( "hltEle5WPTightEcalIsoFilter" ),
    varTag = cms.InputTag( "hltEgammaHcalPFClusterIso" ),
    rhoTag = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    energyLowEdges = cms.vdouble( 0.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    etaBoundaryEB12 = cms.double( 1.0 ),
    etaBoundaryEE12 = cms.double( 2.0 ),
    thrRegularEB1 = cms.vdouble( 2.5 ),
    thrRegularEE1 = cms.vdouble( 1.0 ),
    thrOverEEB1 = cms.vdouble( 0.03 ),
    thrOverEEE1 = cms.vdouble( 0.03 ),
    thrOverE2EB1 = cms.vdouble( 0.0 ),
    thrOverE2EE1 = cms.vdouble( 0.0 ),
    thrRegularEB2 = cms.vdouble( 3.0 ),
    thrRegularEE2 = cms.vdouble( 2.0 ),
    thrOverEEB2 = cms.vdouble( 0.03 ),
    thrOverEEE2 = cms.vdouble( 0.03 ),
    thrOverE2EB2 = cms.vdouble( 0.0 ),
    thrOverE2EE2 = cms.vdouble( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doRhoCorrection = cms.bool( True ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreas = cms.vdouble( 0.2, 0.2, 0.4, 0.5 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.0, 1.479, 2.0 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" )
)
process.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    IncludeErrors = cms.bool( True ),
    UseQualityInfo = cms.bool( False ),
    ErrorList = cms.vint32( 29 ),
    UserErrorList = cms.vint32(  ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    Regions = cms.PSet(  ),
    UsePilotBlade = cms.bool( False ),
    UsePhase1 = cms.bool( True ),
    CablingMapLabel = cms.string( "" )
)
process.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigis" ),
    ClusterMode = cms.string( "PixelThresholdClusterizer" ),
    maxNumberOfClusters = cms.int32( 40000 ),
    payloadType = cms.string( "HLT" ),
    ChannelThreshold = cms.int32( 1000 ),
    MissCalibrate = cms.bool( True ),
    SplitClusters = cms.bool( False ),
    VCaltoElectronGain = cms.int32( 1 ),
    VCaltoElectronGain_L1 = cms.int32( 1 ),
    VCaltoElectronOffset = cms.int32( 0 ),
    VCaltoElectronOffset_L1 = cms.int32( 0 ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold_L1 = cms.int32( 2000 ),
    ClusterThreshold = cms.int32( 4000 ),
    ElectronPerADCGain = cms.double( 135.0 ),
    Phase2Calibration = cms.bool( False ),
    Phase2ReadoutMode = cms.int32( -1 ),
    Phase2DigiBaseline = cms.double( 1200.0 ),
    Phase2KinkADC = cms.int32( 8 )
)
process.hltSiPixelClustersCache = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltSiPixelClusters" ),
    onDemand = cms.bool( False )
)
process.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    src = cms.InputTag( "hltSiPixelClusters" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" ),
    VerboseLevel = cms.untracked.int32( 0 )
)
process.hltSiStripExcludedFEDListProducer = cms.EDProducer( "SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
process.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripClusterizerFromRaw",
    onDemand = cms.bool( True ),
    Clusterizer = cms.PSet( 
      ClusterThreshold = cms.double( 5.0 ),
      SeedThreshold = cms.double( 3.0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      ChannelThreshold = cms.double( 2.0 ),
      MaxAdjacentBad = cms.uint32( 0 ),
      setDetId = cms.bool( True ),
      MaxSequentialHoles = cms.uint32( 0 ),
      RemoveApvShots = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
      MaxSequentialBad = cms.uint32( 1 ),
      ConditionsLabel = cms.string( "" )
    ),
    Algorithms = cms.PSet( 
      CommonModeNoiseSubtractionMode = cms.string( "Median" ),
      useCMMeanMap = cms.bool( False ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( False ),
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      PedestalSubtractionFedMode = cms.bool( True ),
      Use10bitsTruncation = cms.bool( False )
    ),
    DoAPVEmulatorCheck = cms.bool( False ),
    HybridZeroSuppressed = cms.bool( False ),
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
process.hltSiStripClusters = cms.EDProducer( "MeasurementTrackerEventProducer",
    measurementTracker = cms.string( "hltESPMeasurementTracker" ),
    skipClusters = cms.InputTag( "" ),
    pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
    stripClusterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
    Phase2TrackerCluster1DProducer = cms.string( "" ),
    vectorHits = cms.InputTag( "" ),
    vectorHitsRej = cms.InputTag( "" ),
    inactivePixelDetectorLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    pixelCablingMapLabel = cms.string( "" ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    switchOffPixelsIfEmpty = cms.bool( True )
)
process.hltPixelLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix1+BPix4',
      'BPix2+BPix3',
      'BPix2+BPix4',
      'BPix3+BPix4',
      'FPix1_pos+FPix2_pos',
      'FPix1_pos+FPix3_pos',
      'FPix2_pos+FPix3_pos',
      'BPix1+FPix1_pos',
      'BPix1+FPix2_pos',
      'BPix1+FPix3_pos',
      'BPix2+FPix1_pos',
      'BPix2+FPix2_pos',
      'BPix2+FPix3_pos',
      'BPix3+FPix1_pos',
      'BPix3+FPix2_pos',
      'BPix3+FPix3_pos',
      'BPix4+FPix1_pos',
      'BPix4+FPix2_pos',
      'BPix4+FPix3_pos',
      'FPix1_neg+FPix2_neg',
      'FPix1_neg+FPix3_neg',
      'FPix2_neg+FPix3_neg',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_neg',
      'BPix1+FPix3_neg',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_neg',
      'BPix2+FPix3_neg',
      'BPix3+FPix1_neg',
      'BPix3+FPix2_neg',
      'BPix3+FPix3_neg',
      'BPix4+FPix1_neg',
      'BPix4+FPix2_neg',
      'BPix4+FPix3_neg' ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    MTID = cms.PSet(  ),
    MTOB = cms.PSet(  ),
    MTEC = cms.PSet(  )
)
process.hltPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix1+BPix3+BPix4',
      'BPix1+BPix2+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg',
      'BPix1+BPix3+FPix1_pos',
      'BPix1+BPix2+FPix2_pos',
      'BPix1+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix2_neg',
      'BPix1+FPix2_neg+FPix3_neg',
      'BPix1+FPix1_neg+FPix3_neg',
      'BPix1+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_pos+FPix3_pos' ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    MTID = cms.PSet(  ),
    MTOB = cms.PSet(  ),
    MTEC = cms.PSet(  )
)
process.hltEgammaSuperClustersToPixelMatch = cms.EDProducer( "EgammaHLTFilteredSuperClusterProducer",
    cands = cms.InputTag( "hltEgammaCandidates" ),
    minEtCutEB = cms.double( 0.0 ),
    minEtCutEE = cms.double( 0.0 ),
    cuts = cms.VPSet( 
      cms.PSet(  endcapCut = cms.PSet( 
  useEt = cms.bool( False ),
  cutOverE = cms.double( 0.2 )
),
        var = cms.InputTag( "hltEgammaHoverE" ),
        barrelCut = cms.PSet( 
          useEt = cms.bool( False ),
          cutOverE = cms.double( 0.2 )
        )
      )
    )
)
process.hltEleSeedsTrackingRegions = cms.EDProducer( "TrackingRegionsFromSuperClustersEDProducer",
    RegionPSet = cms.PSet( 
      minBSDeltaZ = cms.double( 0.0 ),
      useZInVertex = cms.bool( False ),
      vertices = cms.InputTag( "" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useZInBeamspot = cms.bool( False ),
      ptMin = cms.double( 1.5 ),
      deltaEtaRegion = cms.double( 0.1 ),
      nrSigmaForBSDeltaZ = cms.double( 4.0 ),
      originHalfLength = cms.double( 12.5 ),
      measurementTrackerEvent = cms.InputTag( "" ),
      originRadius = cms.double( 0.2 ),
      precise = cms.bool( True ),
      superClusters = cms.VInputTag( 'hltEgammaSuperClustersToPixelMatch' ),
      whereToUseMeasTracker = cms.string( "kNever" ),
      deltaPhiRegion = cms.double( 0.4 ),
      defaultZ = cms.double( 0.0 )
    )
)
process.hltElePixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    seedingLayers = cms.InputTag( "hltPixelLayerPairs" ),
    trackingRegions = cms.InputTag( "hltEleSeedsTrackingRegions" ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    maxElement = cms.uint32( 0 ),
    maxElementTotal = cms.uint32( 50000000 ),
    layerPairs = cms.vuint32( 0 )
)
process.hltElePixelHitDoubletsForTriplets = cms.EDProducer( "HitPairEDProducer",
    seedingLayers = cms.InputTag( "hltPixelLayerTriplets" ),
    trackingRegions = cms.InputTag( "hltEleSeedsTrackingRegions" ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    maxElement = cms.uint32( 0 ),
    maxElementTotal = cms.uint32( 50000000 ),
    layerPairs = cms.vuint32( 0, 1 )
)
process.hltElePixelHitTriplets = cms.EDProducer( "CAHitTripletEDProducer",
    doublets = cms.InputTag( "hltElePixelHitDoubletsForTriplets" ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    useBendingCorrection = cms.bool( True ),
    CAThetaCut = cms.double( 0.004 ),
    CAPhiCut = cms.double( 0.1 ),
    CAThetaCut_byTriplets = cms.VPSet( 
      cms.PSet(  seedingLayers = cms.string( "" ),
        cut = cms.double( -1.0 )
      )
    ),
    CAPhiCut_byTriplets = cms.VPSet( 
      cms.PSet(  seedingLayers = cms.string( "" ),
        cut = cms.double( -1.0 )
      )
    ),
    CAHardPtCut = cms.double( 0.3 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 6.0 ),
      value1 = cms.double( 100.0 ),
      pt1 = cms.double( 0.8 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 8.0 )
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
)
process.hltElePixelSeedsDoublets = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    seedingHitSets = cms.InputTag( "hltElePixelHitDoublets" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    MinOneOverPtError = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    magneticField = cms.string( "ParabolicMf" ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
)
process.hltElePixelSeedsTriplets = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    seedingHitSets = cms.InputTag( "hltElePixelHitTriplets" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    MinOneOverPtError = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    magneticField = cms.string( "ParabolicMf" ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
)
process.hltElePixelSeedsCombined = cms.EDProducer( "SeedCombiner",
    seedCollections = cms.VInputTag( 'hltElePixelSeedsDoublets','hltElePixelSeedsTriplets' )
)
process.hltEgammaElectronPixelSeeds = cms.EDProducer( "ElectronNHitSeedProducer",
    initialSeeds = cms.InputTag( "hltElePixelSeedsCombined" ),
    vertices = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    measTkEvt = cms.InputTag( "hltSiStripClusters" ),
    superClusters = cms.VInputTag( 'hltEgammaSuperClustersToPixelMatch' ),
    matcherConfig = cms.PSet( 
      useRecoVertex = cms.bool( False ),
      minNrHits = cms.vuint32( 2, 3 ),
      matchingCuts = cms.VPSet( 
        cms.PSet(  dPhiMaxHighEt = cms.vdouble( 0.05 ),
          version = cms.int32( 2 ),
          dRZMaxHighEt = cms.vdouble( 9999.0 ),
          dRZMaxLowEtGrad = cms.vdouble( 0.0 ),
          dPhiMaxLowEtGrad = cms.vdouble( -0.002 ),
          dPhiMaxHighEtThres = cms.vdouble( 20.0 ),
          dRZMaxHighEtThres = cms.vdouble( 0.0 )
        ),
        cms.PSet(  etaBins = cms.vdouble(  ),
          dPhiMaxHighEt = cms.vdouble( 0.003 ),
          version = cms.int32( 2 ),
          dRZMaxHighEt = cms.vdouble( 0.05 ),
          dRZMaxLowEtGrad = cms.vdouble( -0.002 ),
          dPhiMaxLowEtGrad = cms.vdouble( 0.0 ),
          dPhiMaxHighEtThres = cms.vdouble( 0.0 ),
          dRZMaxHighEtThres = cms.vdouble( 30.0 )
        ),
        cms.PSet(  etaBins = cms.vdouble(  ),
          dPhiMaxHighEt = cms.vdouble( 0.003 ),
          version = cms.int32( 2 ),
          dRZMaxHighEt = cms.vdouble( 0.05 ),
          dRZMaxLowEtGrad = cms.vdouble( -0.002 ),
          dPhiMaxLowEtGrad = cms.vdouble( 0.0 ),
          dPhiMaxHighEtThres = cms.vdouble( 0.0 ),
          dRZMaxHighEtThres = cms.vdouble( 30.0 )
        )
      ),
      minNrHitsValidLayerBins = cms.vint32( 4 ),
      detLayerGeom = cms.ESInputTag( "","hltESPGlobalDetLayerGeometry" ),
      navSchool = cms.ESInputTag( "","SimpleNavigationSchool" ),
      paramMagField = cms.ESInputTag( "","ParabolicMf" )
    )
)
process.hltEgammaPixelMatchVars = cms.EDProducer( "EgammaHLTPixelMatchVarProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    pixelSeedsProducer = cms.InputTag( "hltEgammaElectronPixelSeeds" ),
    dPhi1SParams = cms.PSet(  bins = cms.VPSet( 
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.00112, 7.52E-4, -0.00122, 0.00109 ),
    xMin = cms.double( 0.0 ),
    yMax = cms.int32( 1 ),
    xMax = cms.double( 1.5 ),
    funcType = cms.string( "TF1:=pol3" )
  ),
  cms.PSet(  yMin = cms.int32( 2 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.00222, 1.96E-4, -2.03E-4, 4.47E-4 ),
    xMin = cms.double( 0.0 ),
    yMax = cms.int32( 2 ),
    xMax = cms.double( 1.5 ),
    funcType = cms.string( "TF1:=pol3" )
  ),
  cms.PSet(  yMin = cms.int32( 3 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.00236, 6.91E-4, 1.99E-4, 4.16E-4 ),
    xMin = cms.double( 0.0 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 1.5 ),
    funcType = cms.string( "TF1:=pol3" )
  ),
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.00823, -0.0029 ),
    xMin = cms.double( 1.5 ),
    yMax = cms.int32( 1 ),
    xMax = cms.double( 2.0 ),
    funcType = cms.string( "TF1:=pol1" )
  ),
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.00282 ),
    xMin = cms.double( 2.0 ),
    yMax = cms.int32( 1 ),
    xMax = cms.double( 3.0 ),
    funcType = cms.string( "TF1:=pol0" )
  ),
  cms.PSet(  yMin = cms.int32( 2 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.010838, -0.00345 ),
    xMin = cms.double( 1.5 ),
    yMax = cms.int32( 2 ),
    xMax = cms.double( 2.0 ),
    funcType = cms.string( "TF1:=pol1" )
  ),
  cms.PSet(  yMin = cms.int32( 2 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.0043 ),
    xMin = cms.double( 2.0 ),
    yMax = cms.int32( 2 ),
    xMax = cms.double( 3.0 ),
    funcType = cms.string( "TF1:=pol0" )
  ),
  cms.PSet(  yMin = cms.int32( 3 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.0208, -0.0125, 0.00231 ),
    xMin = cms.double( 1.5 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 3.0 ),
    funcType = cms.string( "TF1:=pol2" )
  )
) ),
    dPhi2SParams = cms.PSet(  bins = cms.VPSet( 
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 1.3E-4 ),
    xMin = cms.double( 0.0 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 1.6 ),
    funcType = cms.string( "TF1:=pol0" )
  ),
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 4.5E-4, -1.99E-4 ),
    xMin = cms.double( 1.5 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 1.9 ),
    funcType = cms.string( "TF1:=pol1" )
  ),
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 7.94E-5 ),
    xMin = cms.double( 1.9 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 3.0 ),
    funcType = cms.string( "TF1:=pol0" )
  )
) ),
    dRZ2SParams = cms.PSet(  bins = cms.VPSet( 
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.00299, 2.99E-4, -4.13E-6, 0.00191 ),
    xMin = cms.double( 0.0 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 1.5 ),
    funcType = cms.string( "TF1:=pol3" )
  ),
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.248, -0.329, 0.148, -0.0222 ),
    xMin = cms.double( 1.5 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 3.0 ),
    funcType = cms.string( "TF1:=pol3" )
  )
) ),
    productsToWrite = cms.int32( 0 )
)
process.hltEle5WPTightPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( True ),
    candTag = cms.InputTag( "hltEle5WPTightHcalIsoFilter" ),
    l1PixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeeds" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    s_a_phi1B = cms.double( 0.0069 ),
    s_a_phi1I = cms.double( 0.0088 ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    s_a_phi2I = cms.double( 7.0E-4 ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_zB = cms.double( 0.012 ),
    s_a_rI = cms.double( 0.027 ),
    s_a_rF = cms.double( 0.04 ),
    s2_threshold = cms.double( 0.4 ),
    tanhSO10BarrelThres = cms.double( 0.35 ),
    tanhSO10InterThres = cms.double( 1.0 ),
    tanhSO10ForwardThres = cms.double( 1.0 ),
    useS = cms.bool( False ),
    pixelVeto = cms.bool( False )
)
process.hltEle5WPTightPMS2Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    saveTags = cms.bool( True ),
    candTag = cms.InputTag( "hltEle5WPTightPixelMatchFilter" ),
    varTag = cms.InputTag( 'hltEgammaPixelMatchVars','s2' ),
    rhoTag = cms.InputTag( "" ),
    energyLowEdges = cms.vdouble( 0.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.vdouble( 70.0 ),
    thrRegularEE = cms.vdouble( 45.0 ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrOverE2EE = cms.vdouble( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doRhoCorrection = cms.bool( False ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" )
)
process.hltEgammaCkfTrackCandidatesForGSF = cms.EDProducer( "CkfTrackCandidateMaker",
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    reverseTrajectories = cms.bool( False ),
    useHitsSplitting = cms.bool( True ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 1000000 ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    src = cms.InputTag( "hltEgammaElectronPixelSeeds" ),
    SimpleMagneticField = cms.string( "" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryBuilderForGsfElectrons" ) ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" )
)
process.hltEgammaGsfTracks = cms.EDProducer( "GsfTrackProducer",
    src = cms.InputTag( "hltEgammaCkfTrackCandidatesForGSF" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    producer = cms.string( "" ),
    Fitter = cms.string( "hltESPGsfElectronFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    Propagator = cms.string( "hltESPFwdElectronPropagator" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    MeasurementTracker = cms.string( "hltESPMeasurementTracker" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    GeometricInnerState = cms.bool( True ),
    AlgorithmName = cms.string( "gsf" )
)
process.hltEgammaGsfElectrons = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    TrackProducer = cms.InputTag( "" ),
    GsfTrackProducer = cms.InputTag( "hltEgammaGsfTracks" ),
    UseGsfTracks = cms.bool( True ),
    BSProducer = cms.InputTag( "hltOnlineBeamSpot" )
)
process.hltEgammaGsfTrackVars = cms.EDProducer( "EgammaHLTGsfTrackVarProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    inputCollection = cms.InputTag( "hltEgammaGsfTracks" ),
    beamSpotProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    upperTrackNrToRemoveCut = cms.int32( 9999 ),
    lowerTrackNrToRemoveCut = cms.int32( -1 ),
    useDefaultValuesForBarrel = cms.bool( False ),
    useDefaultValuesForEndcap = cms.bool( False )
)
process.hltEle5WPTightGsfOneOEMinusOneOPFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    saveTags = cms.bool( True ),
    candTag = cms.InputTag( "hltEle5WPTightPMS2Filter" ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVars','OneOESuperMinusOneOP' ),
    rhoTag = cms.InputTag( "" ),
    energyLowEdges = cms.vdouble( 0.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.vdouble( 0.012 ),
    thrRegularEE = cms.vdouble( 0.011 ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrOverE2EE = cms.vdouble( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doRhoCorrection = cms.bool( False ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" )
)
process.hltEle5WPTightGsfMissingHitsFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    saveTags = cms.bool( True ),
    candTag = cms.InputTag( "hltEle5WPTightGsfOneOEMinusOneOPFilter" ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVars','MissingHits' ),
    rhoTag = cms.InputTag( "" ),
    energyLowEdges = cms.vdouble( 0.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.vdouble( 999.0 ),
    thrRegularEE = cms.vdouble( 1.0 ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrOverE2EE = cms.vdouble( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doRhoCorrection = cms.bool( False ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" )
)
process.hltEle5WPTightGsfDetaFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    saveTags = cms.bool( True ),
    candTag = cms.InputTag( "hltEle5WPTightGsfMissingHitsFilter" ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVars','DetaSeed' ),
    rhoTag = cms.InputTag( "" ),
    energyLowEdges = cms.vdouble( 0.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.vdouble( 0.004 ),
    thrRegularEE = cms.vdouble( 0.005 ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrOverE2EE = cms.vdouble( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doRhoCorrection = cms.bool( False ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" )
)
process.hltEle5WPTightGsfDphiFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    saveTags = cms.bool( True ),
    candTag = cms.InputTag( "hltEle5WPTightGsfDetaFilter" ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVars','Dphi' ),
    rhoTag = cms.InputTag( "" ),
    energyLowEdges = cms.vdouble( 0.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.vdouble( 0.02 ),
    thrRegularEE = cms.vdouble( 0.023 ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrOverE2EE = cms.vdouble( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doRhoCorrection = cms.bool( False ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" )
)
process.hltEle5DphiFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    saveTags = cms.bool( True ),
    candTag = cms.InputTag( "hltEgammaTriggerFilterObjectWrapper" ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVars','Dphi' ),
    rhoTag = cms.InputTag( "" ),
    energyLowEdges = cms.vdouble( 0.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.vdouble( 10.0 ),
    thrRegularEE = cms.vdouble( 10.0 ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrOverE2EE = cms.vdouble( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doRhoCorrection = cms.bool( False ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" )
)
process.hltAK4CaloJetsPF = cms.EDProducer( "FastjetJetProducer",
    useMassDropTagger = cms.bool( False ),
    useFiltering = cms.bool( False ),
    useDynamicFiltering = cms.bool( False ),
    useTrimming = cms.bool( False ),
    usePruning = cms.bool( False ),
    useCMSBoostedTauSeedingAlgorithm = cms.bool( False ),
    useKtPruning = cms.bool( False ),
    useConstituentSubtraction = cms.bool( False ),
    useSoftDrop = cms.bool( False ),
    correctShape = cms.bool( False ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    muCut = cms.double( -1.0 ),
    yCut = cms.double( -1.0 ),
    rFilt = cms.double( -1.0 ),
    rFiltFactor = cms.double( -1.0 ),
    trimPtFracMin = cms.double( -1.0 ),
    zcut = cms.double( -1.0 ),
    rcut_factor = cms.double( -1.0 ),
    csRho_EtaMax = cms.double( -1.0 ),
    csRParam = cms.double( -1.0 ),
    beta = cms.double( -1.0 ),
    R0 = cms.double( -1.0 ),
    gridMaxRapidity = cms.double( -1.0 ),
    gridSpacing = cms.double( -1.0 ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MaxVtxZ = cms.double( 15.0 ),
    subjetPtMin = cms.double( -1.0 ),
    muMin = cms.double( -1.0 ),
    muMax = cms.double( -1.0 ),
    yMin = cms.double( -1.0 ),
    yMax = cms.double( -1.0 ),
    dRMin = cms.double( -1.0 ),
    dRMax = cms.double( -1.0 ),
    maxDepth = cms.int32( -1 ),
    nFilt = cms.int32( -1 ),
    MinVtxNdof = cms.int32( 5 ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    srcPVs = cms.InputTag( "NotUsed" ),
    jetType = cms.string( "CaloJet" ),
    jetAlgorithm = cms.string( "AntiKt" ),
    rParam = cms.double( 0.4 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    jetPtMin = cms.double( 1.0 ),
    doPVCorrection = cms.bool( False ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    puPtMin = cms.double( 10.0 ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    subtractorName = cms.string( "" ),
    useExplicitGhosts = cms.bool( False ),
    doAreaDiskApprox = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    Rho_EtaMax = cms.double( 4.4 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    restrictInputs = cms.bool( False ),
    maxInputs = cms.uint32( 1 ),
    writeCompound = cms.bool( False ),
    writeJetsWithConst = cms.bool( False ),
    doFastJetNonUniform = cms.bool( False ),
    useDeterministicSeed = cms.bool( True ),
    minSeed = cms.uint32( 0 ),
    verbosity = cms.int32( 0 ),
    puWidth = cms.double( 0.0 ),
    nExclude = cms.uint32( 0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    puCenters = cms.vdouble(  ),
    applyWeight = cms.bool( False ),
    srcWeights = cms.InputTag( "" ),
    minimumTowersFraction = cms.double( 0.0 ),
    jetCollInstanceName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltAK4CaloJetsPFEt5 = cms.EDFilter( "EtMinCaloJetSelector",
    src = cms.InputTag( "hltAK4CaloJetsPF" ),
    filter = cms.bool( False ),
    etMin = cms.double( 5.0 )
)
process.hltPixelTracksFilter = cms.EDProducer( "PixelTrackFilterByKinematicsProducer",
    ptMin = cms.double( 0.1 ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    tipMax = cms.double( 1.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    chi2 = cms.double( 1000.0 )
)
process.hltPixelTracksFitter = cms.EDProducer( "PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool( False ),
    scaleFactor = cms.double( 0.65 )
)
process.hltPixelTracksTrackingRegions = cms.EDProducer( "GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet( 
      nSigmaZ = cms.double( 4.0 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      ptMin = cms.double( 0.8 ),
      originRadius = cms.double( 0.02 ),
      precise = cms.bool( True )
    )
)
process.hltPixelLayerQuadruplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3+BPix4',
      'BPix1+BPix2+BPix3+FPix1_pos',
      'BPix1+BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos+FPix2_pos',
      'BPix1+BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_neg+FPix2_neg+FPix3_neg' ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    MTID = cms.PSet(  ),
    MTOB = cms.PSet(  ),
    MTEC = cms.PSet(  )
)
process.hltPixelTracksHitDoublets = cms.EDProducer( "HitPairEDProducer",
    seedingLayers = cms.InputTag( "hltPixelLayerQuadruplets" ),
    trackingRegions = cms.InputTag( "hltPixelTracksTrackingRegions" ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    maxElement = cms.uint32( 0 ),
    maxElementTotal = cms.uint32( 50000000 ),
    layerPairs = cms.vuint32( 0, 1, 2 )
)
process.hltPixelTracksHitQuadruplets = cms.EDProducer( "CAHitQuadrupletEDProducer",
    doublets = cms.InputTag( "hltPixelTracksHitDoublets" ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    fitFastCircle = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True ),
    useBendingCorrection = cms.bool( True ),
    CAThetaCut = cms.double( 0.002 ),
    CAPhiCut = cms.double( 0.2 ),
    CAThetaCut_byTriplets = cms.VPSet( 
      cms.PSet(  seedingLayers = cms.string( "" ),
        cut = cms.double( -1.0 )
      )
    ),
    CAPhiCut_byTriplets = cms.VPSet( 
      cms.PSet(  seedingLayers = cms.string( "" ),
        cut = cms.double( -1.0 )
      )
    ),
    CAHardPtCut = cms.double( 0.0 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 50.0 ),
      value1 = cms.double( 200.0 ),
      pt1 = cms.double( 0.7 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
    )
)
process.hltPixelTracks = cms.EDProducer( "PixelTrackProducer",
    passLabel = cms.string( "" ),
    SeedingHitSets = cms.InputTag( "hltPixelTracksHitQuadruplets" ),
    Fitter = cms.InputTag( "hltPixelTracksFitter" ),
    Filter = cms.InputTag( "hltPixelTracksFilter" ),
    Cleaner = cms.string( "hltPixelTracksCleanerBySharedHits" )
)
process.hltPixelVertices = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    ZOffset = cms.double( 5.0 ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPixelTracks" ),
    ZSeparation = cms.double( 0.05 ),
    NTrkMin = cms.int32( 2 ),
    Method2 = cms.bool( True ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    PtMin = cms.double( 1.0 ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) )
)
process.hltTrimmedPixelVertices = cms.EDProducer( "PixelVertexCollectionTrimmer",
    src = cms.InputTag( "hltPixelVertices" ),
    maxVtx = cms.uint32( 100 ),
    fractionSumPt2 = cms.double( 0.3 ),
    minSumPt2 = cms.double( 0.0 ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) )
)
process.hltIter0PFLowPixelSeedsFromPixelTracks = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    InputCollection = cms.InputTag( "hltPixelTracks" ),
    InputVertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
    originHalfLength = cms.double( 0.3 ),
    originRadius = cms.double( 0.1 ),
    useProtoTrackKinematics = cms.bool( False ),
    useEventsWithNoVertex = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    usePV = cms.bool( False ),
    includeFourthHit = cms.bool( False ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) )
)
process.hltIter0PFlowCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    reverseTrajectories = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    src = cms.InputTag( "hltIter0PFLowPixelSeedsFromPixelTracks" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0GroupedCkfTrajectoryBuilderIT" ) ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" )
)
process.hltIter0PFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    useSimpleMF = cms.bool( True ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    src = cms.InputTag( "hltIter0PFlowCkfTrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "hltIter0" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    GeometricInnerState = cms.bool( True ),
    NavigationSchool = cms.string( "" ),
    MeasurementTracker = cms.string( "" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" )
)
process.hltIter0PFlowTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
    ignoreVertices = cms.bool( False ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 3, 4 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_par2 = cms.vdouble( 0.3, 0.3, 0.3 ),
        dr_par1 = cms.vdouble( 0.4, 0.4, 0.4 ),
        dr_exp = cms.vint32( 4, 4, 4 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 3, 4 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 0.4, 0.4, 0.4 ),
        dz_par2 = cms.vdouble( 0.35, 0.35, 0.35 ),
        dz_exp = cms.vint32( 4, 4, 4 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 4 )
    )
)
process.hltIter0PFlowTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    originalSource = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracks" ),
    originalMVAVals = cms.InputTag( 'hltIter0PFlowTrackCutClassifier','MVAValues' ),
    originalQualVals = cms.InputTag( 'hltIter0PFlowTrackCutClassifier','QualityMasks' ),
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False )
)
process.hltIter1ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trajectories = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurity" ),
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    TrackQuality = cms.string( "highPurity" ),
    maxChi2 = cms.double( 9.0 ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    overrideTrkQuals = cms.InputTag( "" )
)
process.hltIter1MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    src = cms.InputTag( "hltSiStripClusters" ),
    OnDemand = cms.bool( False ),
    clustersToSkip = cms.InputTag( "hltIter1ClustersRefRemoval" )
)
process.hltIter1PixelLayerQuadruplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3+BPix4',
      'BPix1+BPix2+BPix3+FPix1_pos',
      'BPix1+BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos+FPix2_pos',
      'BPix1+BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_neg+FPix2_neg+FPix3_neg' ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter1ClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter1ClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    MTID = cms.PSet(  ),
    MTOB = cms.PSet(  ),
    MTEC = cms.PSet(  )
)
process.hltIter1PFlowPixelTrackingRegions = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 0.2 ),
      sigmaZVertex = cms.double( 3.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.4 ),
      originRadius = cms.double( 0.05 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
)
process.hltIter1PFlowPixelClusterCheck = cms.EDProducer( "ClusterCheckerEDProducer",
    doClusterCheck = cms.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
    MaxNumberOfPixelClusters = cms.uint32( 40000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False )
)
process.hltIter1PFlowPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    seedingLayers = cms.InputTag( "hltIter1PixelLayerQuadruplets" ),
    trackingRegions = cms.InputTag( "hltIter1PFlowPixelTrackingRegions" ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    clusterCheck = cms.InputTag( "hltIter1PFlowPixelClusterCheck" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    maxElement = cms.uint32( 0 ),
    maxElementTotal = cms.uint32( 50000000 ),
    layerPairs = cms.vuint32( 0, 1, 2 )
)
process.hltIter1PFlowPixelHitQuadruplets = cms.EDProducer( "CAHitQuadrupletEDProducer",
    doublets = cms.InputTag( "hltIter1PFlowPixelHitDoublets" ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    fitFastCircle = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True ),
    useBendingCorrection = cms.bool( True ),
    CAThetaCut = cms.double( 0.004 ),
    CAPhiCut = cms.double( 0.3 ),
    CAThetaCut_byTriplets = cms.VPSet( 
      cms.PSet(  seedingLayers = cms.string( "" ),
        cut = cms.double( -1.0 )
      )
    ),
    CAPhiCut_byTriplets = cms.VPSet( 
      cms.PSet(  seedingLayers = cms.string( "" ),
        cut = cms.double( -1.0 )
      )
    ),
    CAHardPtCut = cms.double( 0.0 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 100.0 ),
      value1 = cms.double( 1000.0 ),
      pt1 = cms.double( 0.4 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "none" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
    )
)
process.hltIter1PixelTracks = cms.EDProducer( "PixelTrackProducer",
    passLabel = cms.string( "" ),
    SeedingHitSets = cms.InputTag( "hltIter1PFlowPixelHitQuadruplets" ),
    Fitter = cms.InputTag( "hltPixelTracksFitter" ),
    Filter = cms.InputTag( "hltPixelTracksFilter" ),
    Cleaner = cms.string( "hltPixelTracksCleanerBySharedHits" )
)
process.hltIter1PFLowPixelSeedsFromPixelTracks = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    InputCollection = cms.InputTag( "hltIter1PixelTracks" ),
    InputVertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
    originHalfLength = cms.double( 0.3 ),
    originRadius = cms.double( 0.1 ),
    useProtoTrackKinematics = cms.bool( False ),
    useEventsWithNoVertex = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    usePV = cms.bool( False ),
    includeFourthHit = cms.bool( False ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) )
)
process.hltIter1PFlowCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    reverseTrajectories = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    src = cms.InputTag( "hltIter1PFLowPixelSeedsFromPixelTracks" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter1GroupedCkfTrajectoryBuilderIT" ) ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1MaskedMeasurementTrackerEvent" )
)
process.hltIter1PFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    useSimpleMF = cms.bool( True ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    src = cms.InputTag( "hltIter1PFlowCkfTrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "hltIter1" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    GeometricInnerState = cms.bool( True ),
    NavigationSchool = cms.string( "" ),
    MeasurementTracker = cms.string( "" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1MaskedMeasurementTrackerEvent" )
)
process.hltIter1PFlowTrackCutClassifierPrompt = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter1PFlowCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
    ignoreVertices = cms.bool( False ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 0, 2 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 1.0, 0.85 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 1.0, 0.9 ),
        dr_exp = cms.vint32( 3, 3, 3 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 3.40282346639E38, 1.0, 0.9 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 1.0, 0.8 ),
        dz_exp = cms.vint32( 3, 3, 3 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 3.40282346639E38, 1.0, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 3.40282346639E38, 1.0, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    )
)
process.hltIter1PFlowTrackCutClassifierDetached = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter1PFlowCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
    ignoreVertices = cms.bool( False ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 0, 1 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_par2 = cms.vdouble( 1.0, 1.0, 1.0 ),
        dr_par1 = cms.vdouble( 1.0, 1.0, 1.0 ),
        dr_exp = cms.vint32( 4, 4, 4 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
      ),
      maxLostLayers = cms.vint32( 99, 3, 3 ),
      min3DLayers = cms.vint32( 1, 2, 3 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 1.0, 1.0, 1.0 ),
        dz_par2 = cms.vdouble( 1.0, 1.0, 1.0 ),
        dz_exp = cms.vint32( 4, 4, 4 )
      ),
      minNVtxTrk = cms.int32( 2 ),
      maxDz = cms.vdouble( 3.40282346639E38, 1.0, 3.40282346639E38 ),
      minNdof = cms.vdouble( -1.0, -1.0, -1.0 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
      maxChi2n = cms.vdouble( 1.0, 0.7, 0.4 ),
      maxDr = cms.vdouble( 3.40282346639E38, 1.0, 3.40282346639E38 ),
      minLayers = cms.vint32( 5, 5, 5 )
    )
)
process.hltIter1PFlowTrackCutClassifierMerged = cms.EDProducer( "ClassifierMerger",
    inputClassifiers = cms.vstring( 'hltIter1PFlowTrackCutClassifierPrompt',
      'hltIter1PFlowTrackCutClassifierDetached' )
)
process.hltIter1PFlowTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    originalSource = cms.InputTag( "hltIter1PFlowCtfWithMaterialTracks" ),
    originalMVAVals = cms.InputTag( 'hltIter1PFlowTrackCutClassifierMerged','MVAValues' ),
    originalQualVals = cms.InputTag( 'hltIter1PFlowTrackCutClassifierMerged','QualityMasks' ),
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False )
)
process.hltIter1Merged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    MinPT = cms.double( 0.05 ),
    Epsilon = cms.double( -0.001 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    MinFound = cms.int32( 3 ),
    TrackProducers = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPurity','hltIter1PFlowTrackSelectionHighPurity' ),
    hasSelector = cms.vint32( 0, 0 ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPurity','hltIter1PFlowTrackSelectionHighPurity' ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    copyExtras = cms.untracked.bool( True ),
    writeOnlyTrkQuals = cms.bool( False ),
    copyMVA = cms.bool( False )
)
process.hltIter1TrackRefsForJets4Iter2 = cms.EDProducer( "ChargedRefCandidateProducer",
    src = cms.InputTag( "hltIter1Merged" ),
    particleType = cms.string( "pi+" )
)
process.hltAK4Iter1TrackJets4Iter2 = cms.EDProducer( "FastjetJetProducer",
    useMassDropTagger = cms.bool( False ),
    useFiltering = cms.bool( False ),
    useDynamicFiltering = cms.bool( False ),
    useTrimming = cms.bool( False ),
    usePruning = cms.bool( False ),
    useCMSBoostedTauSeedingAlgorithm = cms.bool( False ),
    useKtPruning = cms.bool( False ),
    useConstituentSubtraction = cms.bool( False ),
    useSoftDrop = cms.bool( False ),
    correctShape = cms.bool( False ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( True ),
    muCut = cms.double( -1.0 ),
    yCut = cms.double( -1.0 ),
    rFilt = cms.double( -1.0 ),
    rFiltFactor = cms.double( -1.0 ),
    trimPtFracMin = cms.double( -1.0 ),
    zcut = cms.double( -1.0 ),
    rcut_factor = cms.double( -1.0 ),
    csRho_EtaMax = cms.double( -1.0 ),
    csRParam = cms.double( -1.0 ),
    beta = cms.double( -1.0 ),
    R0 = cms.double( -1.0 ),
    gridMaxRapidity = cms.double( -1.0 ),
    gridSpacing = cms.double( -1.0 ),
    DzTrVtxMax = cms.double( 0.5 ),
    DxyTrVtxMax = cms.double( 0.2 ),
    MaxVtxZ = cms.double( 30.0 ),
    subjetPtMin = cms.double( -1.0 ),
    muMin = cms.double( -1.0 ),
    muMax = cms.double( -1.0 ),
    yMin = cms.double( -1.0 ),
    yMax = cms.double( -1.0 ),
    dRMin = cms.double( -1.0 ),
    dRMax = cms.double( -1.0 ),
    maxDepth = cms.int32( -1 ),
    nFilt = cms.int32( -1 ),
    MinVtxNdof = cms.int32( 0 ),
    src = cms.InputTag( "hltIter1TrackRefsForJets4Iter2" ),
    srcPVs = cms.InputTag( "hltTrimmedPixelVertices" ),
    jetType = cms.string( "TrackJet" ),
    jetAlgorithm = cms.string( "AntiKt" ),
    rParam = cms.double( 0.4 ),
    inputEtMin = cms.double( 0.1 ),
    inputEMin = cms.double( 0.0 ),
    jetPtMin = cms.double( 7.5 ),
    doPVCorrection = cms.bool( False ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    puPtMin = cms.double( 0.0 ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    subtractorName = cms.string( "" ),
    useExplicitGhosts = cms.bool( False ),
    doAreaDiskApprox = cms.bool( False ),
    voronoiRfact = cms.double( 0.9 ),
    Rho_EtaMax = cms.double( 4.4 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    restrictInputs = cms.bool( False ),
    maxInputs = cms.uint32( 1 ),
    writeCompound = cms.bool( False ),
    writeJetsWithConst = cms.bool( False ),
    doFastJetNonUniform = cms.bool( False ),
    useDeterministicSeed = cms.bool( True ),
    minSeed = cms.uint32( 14327 ),
    verbosity = cms.int32( 0 ),
    puWidth = cms.double( 0.0 ),
    nExclude = cms.uint32( 0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    puCenters = cms.vdouble(  ),
    applyWeight = cms.bool( False ),
    srcWeights = cms.InputTag( "" ),
    minimumTowersFraction = cms.double( 0.0 ),
    jetCollInstanceName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltIter1TrackAndTauJets4Iter2 = cms.EDProducer( "TauJetSelectorForHLTTrackSeeding",
    inputTrackJetTag = cms.InputTag( "hltAK4Iter1TrackJets4Iter2" ),
    inputCaloJetTag = cms.InputTag( "hltAK4CaloJetsPFEt5" ),
    inputTrackTag = cms.InputTag( "hltIter1Merged" ),
    ptMinCaloJet = cms.double( 10.0 ),
    etaMinCaloJet = cms.double( -2.7 ),
    etaMaxCaloJet = cms.double( 2.7 ),
    tauConeSize = cms.double( 0.2 ),
    isolationConeSize = cms.double( 0.5 ),
    fractionMinCaloInTauCone = cms.double( 0.7 ),
    fractionMaxChargedPUInCaloCone = cms.double( 0.3 ),
    ptTrkMaxInCaloCone = cms.double( 1.4 ),
    nTrkMaxInCaloCone = cms.int32( 0 )
)
process.hltIter2ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trajectories = cms.InputTag( "hltIter1PFlowTrackSelectionHighPurity" ),
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter1ClustersRefRemoval" ),
    TrackQuality = cms.string( "highPurity" ),
    maxChi2 = cms.double( 16.0 ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    overrideTrkQuals = cms.InputTag( "" )
)
process.hltIter2MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    src = cms.InputTag( "hltSiStripClusters" ),
    OnDemand = cms.bool( False ),
    clustersToSkip = cms.InputTag( "hltIter2ClustersRefRemoval" )
)
process.hltIter2PixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix1+BPix3+BPix4',
      'BPix1+BPix2+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg',
      'BPix1+BPix3+FPix1_pos',
      'BPix1+BPix2+FPix2_pos',
      'BPix1+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix2_neg',
      'BPix1+FPix2_neg+FPix3_neg',
      'BPix1+FPix1_neg+FPix3_neg',
      'BPix1+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_pos+FPix3_pos' ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2ClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2ClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    MTID = cms.PSet(  ),
    MTOB = cms.PSet(  ),
    MTEC = cms.PSet(  )
)
process.hltIter2PFlowPixelTrackingRegions = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet( 
      vertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
      zErrorVetex = cms.double( 0.05 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 15.0 ),
      maxNVertices = cms.int32( 10 ),
      maxNRegions = cms.int32( 100 ),
      nSigmaZVertex = cms.double( 4.0 ),
      nSigmaZBeamSpot = cms.double( 3.0 ),
      ptMin = cms.double( 0.4 ),
      mode = cms.string( "VerticesFixed" ),
      input = cms.InputTag( "hltIter1TrackAndTauJets4Iter2" ),
      searchOpt = cms.bool( True ),
      whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
      originRadius = cms.double( 0.025 ),
      measurementTrackerName = cms.InputTag( "hltIter2MaskedMeasurementTrackerEvent" ),
      precise = cms.bool( True ),
      deltaEta = cms.double( 0.8 ),
      deltaPhi = cms.double( 0.8 )
    )
)
process.hltIter2PFlowPixelClusterCheck = cms.EDProducer( "ClusterCheckerEDProducer",
    doClusterCheck = cms.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
    MaxNumberOfPixelClusters = cms.uint32( 40000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False )
)
process.hltIter2PFlowPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    seedingLayers = cms.InputTag( "hltIter2PixelLayerTriplets" ),
    trackingRegions = cms.InputTag( "hltIter2PFlowPixelTrackingRegions" ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    clusterCheck = cms.InputTag( "hltIter2PFlowPixelClusterCheck" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    maxElement = cms.uint32( 0 ),
    maxElementTotal = cms.uint32( 50000000 ),
    layerPairs = cms.vuint32( 0, 1 )
)
process.hltIter2PFlowPixelHitTriplets = cms.EDProducer( "CAHitTripletEDProducer",
    doublets = cms.InputTag( "hltIter2PFlowPixelHitDoublets" ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    useBendingCorrection = cms.bool( True ),
    CAThetaCut = cms.double( 0.004 ),
    CAPhiCut = cms.double( 0.1 ),
    CAThetaCut_byTriplets = cms.VPSet( 
      cms.PSet(  seedingLayers = cms.string( "" ),
        cut = cms.double( -1.0 )
      )
    ),
    CAPhiCut_byTriplets = cms.VPSet( 
      cms.PSet(  seedingLayers = cms.string( "" ),
        cut = cms.double( -1.0 )
      )
    ),
    CAHardPtCut = cms.double( 0.3 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 6.0 ),
      value1 = cms.double( 100.0 ),
      pt1 = cms.double( 0.4 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 8.0 )
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
)
process.hltIter2PFlowPixelSeeds = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    seedingHitSets = cms.InputTag( "hltIter2PFlowPixelHitTriplets" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    MinOneOverPtError = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    magneticField = cms.string( "ParabolicMf" ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
)
process.hltIter2PFlowCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    reverseTrajectories = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    src = cms.InputTag( "hltIter2PFlowPixelSeeds" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2GroupedCkfTrajectoryBuilderIT" ) ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2MaskedMeasurementTrackerEvent" )
)
process.hltIter2PFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    useSimpleMF = cms.bool( True ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    src = cms.InputTag( "hltIter2PFlowCkfTrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "hltIter2" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    GeometricInnerState = cms.bool( True ),
    NavigationSchool = cms.string( "" ),
    MeasurementTracker = cms.string( "" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2MaskedMeasurementTrackerEvent" )
)
process.hltIter2PFlowTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter2PFlowCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
    ignoreVertices = cms.bool( False ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 0.3 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 0.4 ),
        dr_exp = cms.vint32( 4, 4, 4 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 0.4 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 0.35 ),
        dz_exp = cms.vint32( 4, 4, 4 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    )
)
process.hltIter2PFlowTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    originalSource = cms.InputTag( "hltIter2PFlowCtfWithMaterialTracks" ),
    originalMVAVals = cms.InputTag( 'hltIter2PFlowTrackCutClassifier','MVAValues' ),
    originalQualVals = cms.InputTag( 'hltIter2PFlowTrackCutClassifier','QualityMasks' ),
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False )
)
process.hltIter2Merged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    MinPT = cms.double( 0.05 ),
    Epsilon = cms.double( -0.001 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    MinFound = cms.int32( 3 ),
    TrackProducers = cms.VInputTag( 'hltIter1Merged','hltIter2PFlowTrackSelectionHighPurity' ),
    hasSelector = cms.vint32( 0, 0 ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter1Merged','hltIter2PFlowTrackSelectionHighPurity' ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    copyExtras = cms.untracked.bool( True ),
    writeOnlyTrkQuals = cms.bool( False ),
    copyMVA = cms.bool( False )
)
process.hltDoubletRecoveryClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trajectories = cms.InputTag( "hltIter2PFlowTrackSelectionHighPurity" ),
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter2ClustersRefRemoval" ),
    TrackQuality = cms.string( "highPurity" ),
    maxChi2 = cms.double( 16.0 ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    overrideTrkQuals = cms.InputTag( "" )
)
process.hltDoubletRecoveryMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    src = cms.InputTag( "hltSiStripClusters" ),
    OnDemand = cms.bool( False ),
    clustersToSkip = cms.InputTag( "hltDoubletRecoveryClustersRefRemoval" )
)
process.hltDoubletRecoveryPixelLayersAndRegions = cms.EDProducer( "PixelInactiveAreaTrackingRegionsSeedingLayersProducer",
    RegionPSet = cms.PSet( 
      precise = cms.bool( True ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 15.0 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      measurementTrackerName = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEvent" ),
      extraEta = cms.double( 0.0 ),
      vertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
      ptMin = cms.double( 1.2 ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
      maxNVertices = cms.int32( 3 ),
      extraPhi = cms.double( 0.0 ),
      originRadius = cms.double( 0.015 ),
      zErrorVertex = cms.double( 0.03 ),
      operationMode = cms.string( "VerticesFixed" )
    ),
    inactivePixelDetectorLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    ignoreSingleFPixPanelModules = cms.bool( True ),
    debug = cms.untracked.bool( False ),
    createPlottingFiles = cms.untracked.bool( False ),
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix1+BPix4',
      'BPix2+BPix3',
      'BPix2+BPix4',
      'BPix3+BPix4',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix1+FPix3_pos',
      'BPix1+FPix3_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'BPix3+FPix1_pos',
      'BPix3+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix3_pos',
      'FPix1_neg+FPix3_neg',
      'FPix2_pos+FPix3_pos',
      'FPix2_neg+FPix3_neg' ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltDoubletRecoveryClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltDoubletRecoveryClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    MTID = cms.PSet(  ),
    MTOB = cms.PSet(  ),
    MTEC = cms.PSet(  )
)
process.hltDoubletRecoveryPFlowPixelClusterCheck = cms.EDProducer( "ClusterCheckerEDProducer",
    doClusterCheck = cms.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
    MaxNumberOfPixelClusters = cms.uint32( 40000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False )
)
process.hltDoubletRecoveryPFlowPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    seedingLayers = cms.InputTag( "" ),
    trackingRegions = cms.InputTag( "" ),
    trackingRegionsSeedingLayers = cms.InputTag( "hltDoubletRecoveryPixelLayersAndRegions" ),
    clusterCheck = cms.InputTag( "hltDoubletRecoveryPFlowPixelClusterCheck" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( False ),
    maxElement = cms.uint32( 0 ),
    maxElementTotal = cms.uint32( 50000000 ),
    layerPairs = cms.vuint32( 0 )
)
process.hltDoubletRecoveryPFlowPixelSeeds = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    seedingHitSets = cms.InputTag( "hltDoubletRecoveryPFlowPixelHitDoublets" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    MinOneOverPtError = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    magneticField = cms.string( "ParabolicMf" ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
)
process.hltDoubletRecoveryPFlowCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    reverseTrajectories = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    src = cms.InputTag( "hltDoubletRecoveryPFlowPixelSeeds" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2GroupedCkfTrajectoryBuilderIT" ) ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEvent" )
)
process.hltDoubletRecoveryPFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    useSimpleMF = cms.bool( True ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    src = cms.InputTag( "hltDoubletRecoveryPFlowCkfTrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "hltDoubletRecovery" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    GeometricInnerState = cms.bool( True ),
    NavigationSchool = cms.string( "" ),
    MeasurementTracker = cms.string( "" ),
    MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEvent" )
)
process.hltDoubletRecoveryPFlowTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltDoubletRecoveryPFlowCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
    ignoreVertices = cms.bool( False ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 0.3 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 0.4 ),
        dr_exp = cms.vint32( 4, 4, 4 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 0.4 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 0.35 ),
        dz_exp = cms.vint32( 4, 4, 4 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    )
)
process.hltDoubletRecoveryPFlowTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    originalSource = cms.InputTag( "hltDoubletRecoveryPFlowCtfWithMaterialTracks" ),
    originalMVAVals = cms.InputTag( 'hltDoubletRecoveryPFlowTrackCutClassifier','MVAValues' ),
    originalQualVals = cms.InputTag( 'hltDoubletRecoveryPFlowTrackCutClassifier','QualityMasks' ),
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False )
)
process.hltMergedTracks = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    MinPT = cms.double( 0.05 ),
    Epsilon = cms.double( -0.001 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    MinFound = cms.int32( 3 ),
    TrackProducers = cms.VInputTag( 'hltIter2Merged','hltDoubletRecoveryPFlowTrackSelectionHighPurity' ),
    hasSelector = cms.vint32( 0, 0 ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter2Merged','hltDoubletRecoveryPFlowTrackSelectionHighPurity' ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    copyExtras = cms.untracked.bool( True ),
    writeOnlyTrkQuals = cms.bool( False ),
    copyMVA = cms.bool( False )
)
process.hltEgammaEleGsfTrackIso = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    electronProducer = cms.InputTag( "hltEgammaGsfElectrons" ),
    trackProducer = cms.InputTag( "hltMergedTracks" ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    beamSpotProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoConeSize = cms.double( 0.2 ),
    egTrkIsoZSpan = cms.double( 0.15 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSizeBarrel = cms.double( 0.03 ),
    egTrkIsoVetoConeSizeEndcap = cms.double( 0.03 ),
    egTrkIsoStripBarrel = cms.double( 0.01 ),
    egTrkIsoStripEndcap = cms.double( 0.01 ),
    useGsfTrack = cms.bool( True ),
    useSCRefs = cms.bool( True )
)
process.hltEle5WPTightGsfTrackIsoFilter = cms.EDFilter( "HLTEgammaGenericQuadraticEtaFilter",
    saveTags = cms.bool( True ),
    candTag = cms.InputTag( "hltEle5DphiFilter" ),
    varTag = cms.InputTag( "hltEgammaEleGsfTrackIso" ),
    rhoTag = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    energyLowEdges = cms.vdouble( 0.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    etaBoundaryEB12 = cms.double( 1.0 ),
    etaBoundaryEE12 = cms.double( 2.1 ),
    thrRegularEB1 = cms.vdouble( 0.838 ),
    thrRegularEE1 = cms.vdouble( -0.363 ),
    thrOverEEB1 = cms.vdouble( 0.03 ),
    thrOverEEE1 = cms.vdouble( 0.025 ),
    thrOverE2EB1 = cms.vdouble( 0.0 ),
    thrOverE2EE1 = cms.vdouble( 0.0 ),
    thrRegularEB2 = cms.vdouble( -0.385 ),
    thrRegularEE2 = cms.vdouble( 0.702 ),
    thrOverEEB2 = cms.vdouble( 0.03 ),
    thrOverEEE2 = cms.vdouble( 0.025 ),
    thrOverE2EB2 = cms.vdouble( 0.0 ),
    thrOverE2EE2 = cms.vdouble( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doRhoCorrection = cms.bool( True ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreas = cms.vdouble( 0.029, 0.111, 0.114, 0.032 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.0, 1.479, 2.1 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023, 1024 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    throw = cms.bool( False ),
    processName = cms.string( "@" ),
    moduleLabelPatternsToMatch = cms.vstring( 'hlt*' ),
    moduleLabelPatternsToSkip = cms.vstring(  )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtStage2Digis + process.hltGtStage2ObjectMap )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTDoFullUnpackingEgammaEcalSequence = cms.Sequence( process.hltEcalDigis + process.hltEcalPreshowerDigis + process.hltEcalUncalibRecHit + process.hltEcalDetIdToBeRecovered + process.hltEcalRecHit + process.hltEcalPreshowerRecHit )
process.HLTPFClusteringForEgamma = cms.Sequence( process.hltRechitInRegionsECAL + process.hltRechitInRegionsES + process.hltParticleFlowRecHitECALL1Seeded + process.hltParticleFlowRecHitPSL1Seeded + process.hltParticleFlowClusterPSL1Seeded + process.hltParticleFlowClusterECALUncorrectedL1Seeded + process.hltParticleFlowClusterECALL1Seeded + process.hltParticleFlowSuperClusterECALL1Seeded )
process.HLTDoLocalHcalSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfprereco + process.hltHfreco + process.hltHoreco )
process.HLTFastJetForEgamma = cms.Sequence( process.hltTowerMakerForAll + process.hltFixedGridRhoFastjetAllCaloForMuons )
process.HLTPFHcalClustering = cms.Sequence( process.hltParticleFlowRecHitHBHE + process.hltParticleFlowClusterHBHE + process.hltParticleFlowClusterHCAL )
process.HLTDoLocalPixelSequence = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClusters + process.hltSiPixelClustersCache + process.hltSiPixelRecHits )
process.HLTDoLocalStripSequence = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.hltSiStripRawToClustersFacility + process.hltSiStripClusters )
process.HLTElePixelMatchSequence = cms.Sequence( process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltPixelLayerPairs + process.hltPixelLayerTriplets + process.hltEgammaHoverE + process.hltEgammaSuperClustersToPixelMatch + process.hltEleSeedsTrackingRegions + process.hltElePixelHitDoublets + process.hltElePixelHitDoubletsForTriplets + process.hltElePixelHitTriplets + process.hltElePixelSeedsDoublets + process.hltElePixelSeedsTriplets + process.hltElePixelSeedsCombined + process.hltEgammaElectronPixelSeeds + process.hltEgammaPixelMatchVars )
process.HLTGsfElectronSequence = cms.Sequence( process.hltEgammaCkfTrackCandidatesForGSF + process.hltEgammaGsfTracks + process.hltEgammaGsfElectrons + process.hltEgammaGsfTrackVars )
process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence( process.hltEcalDigis + process.hltEcalUncalibRecHit + process.hltEcalDetIdToBeRecovered + process.hltEcalRecHit )
process.HLTDoCaloSequencePF = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence + process.HLTDoLocalHcalSequence + process.hltTowerMakerForAll )
process.HLTAK4CaloJetsPrePFRecoSequence = cms.Sequence( process.HLTDoCaloSequencePF + process.hltAK4CaloJetsPF )
process.HLTPreAK4PFJetsRecoSequence = cms.Sequence( process.HLTAK4CaloJetsPrePFRecoSequence + process.hltAK4CaloJetsPFEt5 )
process.HLTRecoPixelTracksSequence = cms.Sequence( process.hltPixelTracksFilter + process.hltPixelTracksFitter + process.hltPixelTracksTrackingRegions + process.hltPixelLayerQuadruplets + process.hltPixelTracksHitDoublets + process.hltPixelTracksHitQuadruplets + process.hltPixelTracks )
process.HLTRecopixelvertexingSequence = cms.Sequence( process.HLTRecoPixelTracksSequence + process.hltPixelVertices + process.hltTrimmedPixelVertices )
process.HLTIterativeTrackingIteration0 = cms.Sequence( process.hltIter0PFLowPixelSeedsFromPixelTracks + process.hltIter0PFlowCkfTrackCandidates + process.hltIter0PFlowCtfWithMaterialTracks + process.hltIter0PFlowTrackCutClassifier + process.hltIter0PFlowTrackSelectionHighPurity )
process.HLTIterativeTrackingIteration1 = cms.Sequence( process.hltIter1ClustersRefRemoval + process.hltIter1MaskedMeasurementTrackerEvent + process.hltIter1PixelLayerQuadruplets + process.hltIter1PFlowPixelTrackingRegions + process.hltIter1PFlowPixelClusterCheck + process.hltIter1PFlowPixelHitDoublets + process.hltIter1PFlowPixelHitQuadruplets + process.hltIter1PixelTracks + process.hltIter1PFLowPixelSeedsFromPixelTracks + process.hltIter1PFlowCkfTrackCandidates + process.hltIter1PFlowCtfWithMaterialTracks + process.hltIter1PFlowTrackCutClassifierPrompt + process.hltIter1PFlowTrackCutClassifierDetached + process.hltIter1PFlowTrackCutClassifierMerged + process.hltIter1PFlowTrackSelectionHighPurity )
process.HLTIter1TrackAndTauJets4Iter2Sequence = cms.Sequence( process.hltIter1TrackRefsForJets4Iter2 + process.hltAK4Iter1TrackJets4Iter2 + process.hltIter1TrackAndTauJets4Iter2 )
process.HLTIterativeTrackingIteration2 = cms.Sequence( process.hltIter2ClustersRefRemoval + process.hltIter2MaskedMeasurementTrackerEvent + process.hltIter2PixelLayerTriplets + process.hltIter2PFlowPixelTrackingRegions + process.hltIter2PFlowPixelClusterCheck + process.hltIter2PFlowPixelHitDoublets + process.hltIter2PFlowPixelHitTriplets + process.hltIter2PFlowPixelSeeds + process.hltIter2PFlowCkfTrackCandidates + process.hltIter2PFlowCtfWithMaterialTracks + process.hltIter2PFlowTrackCutClassifier + process.hltIter2PFlowTrackSelectionHighPurity )
process.HLTIterativeTrackingDoubletRecovery = cms.Sequence( process.hltDoubletRecoveryClustersRefRemoval + process.hltDoubletRecoveryMaskedMeasurementTrackerEvent + process.hltDoubletRecoveryPixelLayersAndRegions + process.hltDoubletRecoveryPFlowPixelClusterCheck + process.hltDoubletRecoveryPFlowPixelHitDoublets + process.hltDoubletRecoveryPFlowPixelSeeds + process.hltDoubletRecoveryPFlowCkfTrackCandidates + process.hltDoubletRecoveryPFlowCtfWithMaterialTracks + process.hltDoubletRecoveryPFlowTrackCutClassifier + process.hltDoubletRecoveryPFlowTrackSelectionHighPurity )
process.HLTIterativeTrackingIter02 = cms.Sequence( process.HLTIterativeTrackingIteration0 + process.HLTIterativeTrackingIteration1 + process.hltIter1Merged + process.HLTIter1TrackAndTauJets4Iter2Sequence + process.HLTIterativeTrackingIteration2 + process.hltIter2Merged + process.HLTIterativeTrackingDoubletRecovery + process.hltMergedTracks )
process.HLTTrackReconstructionForPFNoMu = cms.Sequence( process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequence + process.HLTDoLocalStripSequence + process.HLTIterativeTrackingIter02 )
process.HLTTrackReconstructionForIsoElectronIter02 = cms.Sequence( process.HLTPreAK4PFJetsRecoSequence + process.HLTTrackReconstructionForPFNoMu )
process.HLTEle5WPTightGsfSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEgammaTriggerFilterObjectWrapper + cms.ignore(process.hltEGL1SingleEGOrFilter) + cms.ignore(process.hltEG5L1SingleEGOrEtFilter) + process.hltEgammaClusterShape + cms.ignore(process.hltEle5WPTightClusterShapeFilter) + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + cms.ignore(process.hltEle5WPTightHEFilter) + process.hltEgammaEcalPFClusterIso + cms.ignore(process.hltEle5WPTightEcalIsoFilter) + process.HLTPFHcalClustering + process.hltEgammaHcalPFClusterIso + cms.ignore(process.hltEle5WPTightHcalIsoFilter) + process.HLTElePixelMatchSequence + cms.ignore(process.hltEle5WPTightPixelMatchFilter) + cms.ignore(process.hltEle5WPTightPMS2Filter) + process.HLTGsfElectronSequence + cms.ignore(process.hltEle5WPTightGsfOneOEMinusOneOPFilter) + cms.ignore(process.hltEle5WPTightGsfMissingHitsFilter) + cms.ignore(process.hltEle5WPTightGsfDetaFilter) + cms.ignore(process.hltEle5WPTightGsfDphiFilter) + process.hltEle5DphiFilter + process.HLTTrackReconstructionForIsoElectronIter02 + process.hltEgammaEleGsfTrackIso + cms.ignore(process.hltEle5WPTightGsfTrackIsoFilter) )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )

process.HLTriggerFirstPath = cms.Path( process.hltGetConditions + process.hltGetRaw + process.hltPSetMap + process.hltBoolFalse )
process.HLT_Ele32_WPTight_Gsf_v15 = cms.Path( process.HLTBeginSequence + cms.ignore(process.hltL1sSingleEGor) + process.hltPreEle32WPTightGsf + process.HLTEle5WPTightGsfSequence + process.HLTEndSequence )
process.HLTriggerFinalPath = cms.Path( process.hltGtStage2Digis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolFalse )


process.HLTSchedule = cms.Schedule( *(process.HLTriggerFirstPath, process.HLT_Ele32_WPTight_Gsf_v15, process.HLTriggerFinalPath, ))


process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/497/00000/00C024D9-C893-E811-BE8B-FA163E085754.root',
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

# avoid PrescaleService error due to missing HLT paths
if 'PrescaleService' in process.__dict__:
    for pset in reversed(process.PrescaleService.prescaleTable):
        if not hasattr(process,pset.pathName.value()):
            process.PrescaleService.prescaleTable.remove(pset)

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 100 )
)

# enable TrigReport, TimeReport and MultiThreading
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    numberOfThreads = cms.untracked.uint32( 4 ),
    numberOfStreams = cms.untracked.uint32( 0 ),
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'auto:run3_hlt')

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.TriggerSummaryProducerAOD = cms.untracked.PSet()
    process.MessageLogger.L1GtTrigReport = cms.untracked.PSet()
    process.MessageLogger.L1TGlobalSummary = cms.untracked.PSet()
    process.MessageLogger.HLTrigReport = cms.untracked.PSet()
    process.MessageLogger.FastReport = cms.untracked.PSet()
    process.MessageLogger.ThroughputService = cms.untracked.PSet()

# load the DQMStore and DQMRootOutputModule
process.load( "DQMServices.Core.DQMStore_cfi" )

process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("DQMIO.root")
)

process.DQMOutput = cms.EndPath( process.dqmOutput )

# add specific customizations
_customInfo = {}
_customInfo['menuType'  ]= "GRun"
_customInfo['globalTags']= {}
_customInfo['globalTags'][True ] = "auto:run3_hlt_GRun"
_customInfo['globalTags'][False] = "auto:run3_mc_GRun"
_customInfo['inputFiles']={}
_customInfo['inputFiles'][True]  = "file:RelVal_Raw_GRun_DATA.root"
_customInfo['inputFiles'][False] = "file:RelVal_Raw_GRun_MC.root"
_customInfo['maxEvents' ]=  20
_customInfo['globalTag' ]= "auto:run3_hlt"
_customInfo['inputFile' ]=  ['/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/497/00000/00C024D9-C893-E811-BE8B-FA163E085754.root']
_customInfo['realData'  ]=  True
from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
process = customizeHLTforAll(process,"GRun",_customInfo)

from HLTrigger.Configuration.customizeHLTforCMSSW import customizeHLTforCMSSW
process = customizeHLTforCMSSW(process,"GRun")

# Eras-based customisations
from HLTrigger.Configuration.Eras import modifyHLTforEras
modifyHLTforEras(process)

#User-defined customization functions
from HLTrigger.Configuration.customizeHLTforCMSSW import customiseFor2018Input
process = customiseFor2018Input(process)
from HLTrigger.Configuration.customizeHLTforEGamma import customiseEGammaMenuDev
process = customiseEGammaMenuDev(process)

process.egOutMod.fileName = cms.untracked.string(options.outputFile)

process.egOutMod.outputCommands.append('keep *_slimmedElectrons_*_*') 
process.egOutMod.outputCommands.append('keep *_offlineSlimmedPrimaryVertices_*_*') 
process.egOutMod.outputCommands.append('keep *_packedPFCandidates_*_*') 
process.egOutMod.outputCommands.append('keep *_isolatedTracks_*_*') 

process.egOutMod.outputCommands.append('keep *_reducedEgamma_*_*') 
process.egOutMod.outputCommands.append('keep *_TriggerResults_*_*')
process.egOutMod.outputCommands.append('keep *_slimmedMuons_*_*')

#process.egOutMod.outputCommands.append('keep *_displacedStandAloneMuons_*_*') 
#process.egOutMod.outputCommands.append('keep *_*_*_*') 



process.source.fileNames = cms.untracked.vstring(       
# This is ok!
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/BAC58767-E593-E811-BD20-FA163EC5D27D.root'

#    '/store/data/Run2018D/EphemeralZeroBias8/MINIAOD/PromptReco-v2/000/320/500/00000/042EC2A9-F595-E811-8000-FA163E93F5A3.root'
'/store/data/Run2018D/EphemeralZeroBias8/MINIAOD/PromptReco-v2/000/320/500/00000/0ED01D6C-FE95-E811-8FA9-FA163E536B65.root'
#        '/store/data/Run2018D/EphemeralZeroBias8/MINIAOD/PromptReco-v2/000/320/497/00000/C8FEA71E-6695-E811-8D4D-02163E015309.root'
)

process.source.secondaryFileNames=cms.untracked.vstring(
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/F87CC759-D793-E811-8606-FA163E91624B.root',
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/0AD1DC91-D893-E811-B09E-FA163EF17A8E.root',
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/BAC58767-E593-E811-BD20-FA163EC5D27D.root',
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/8E82948A-D993-E811-9029-FA163ED2983B.root',
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/DAA1583F-D793-E811-8BD2-FA163EA4DD67.root',
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/BA68D7D6-DD93-E811-B0E8-FA163E4D3DAC.root',
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/DAD7B4AF-D993-E811-AE0C-02163E00CD90.root',
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/B63A4B96-E193-E811-BFA7-FA163EFD28DB.root',
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/1A998A1B-DD93-E811-8B34-FA163EBBF819.root',
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/02FE5D95-D993-E811-A437-02163E016161.root',
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/865908EB-E593-E811-B188-02163E012CFA.root',
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/824022BF-D893-E811-BF28-FA163ED3127A.root',
#    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/6613D742-E993-E811-AA29-02163E013066.root'
    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/90D00266-E593-E811-B22C-FA163E2C0EB5.root',
    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/72AD64FF-DA93-E811-9EFB-02163E01767C.root',
    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/A2E01D6A-E593-E811-A44D-02163E015C09.root',
    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/D05057CD-E693-E811-83F4-FA163EB656C6.root',
    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/8AE52E67-E593-E811-B025-FA163EEE65D6.root',
    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/B65DBEDC-E693-E811-B63B-FA163EE96112.root',
    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/54A80CB1-E093-E811-BBEB-FA163E07DD78.root',
    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/66C6AD51-E293-E811-826D-FA163ED85F64.root',
    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/1485D3A0-D893-E811-93F9-FA163E9666C9.root',
    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/9A94309A-E793-E811-8A35-02163E00ACDD.root',
    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/46AC0CB1-E093-E811-BA3D-FA163E07DD78.root',
    '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/500/00000/16A189D2-E693-E811-8769-FA163EB1CCFA.root'
)

process.source.inputCommands = cms.untracked.vstring(
    'keep *'
)


#process.source = cms.Source( "PoolSource",
#    fileNames = cms.untracked.vstring(       
#        '/store/data/Run2018D/EphemeralZeroBias8/MINIAOD/PromptReco-v2/000/320/497/00000/C8FEA71E-6695-E811-8D4D-02163E015309.root'
#    ),
#
#    secondaryFileNames=cms.untracked.vstring(
#        '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/497/00000/04E0297E-C893-E811-B0AA-FA163EADBE2E.root',
#        '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/497/00000/0E8ECE80-C893-E811-8745-FA163EADFE85.root',
#        '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/497/00000/24F83A7B-C893-E811-9B05-FA163EEECA4B.root',
#        '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/497/00000/7498FCE5-C993-E811-9334-FA163EE0A861.root',
#        '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/497/00000/92AF2DF3-C993-E811-B2F3-FA163E1972DF.root',
#        '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/497/00000/92D52E78-C893-E811-9941-FA163EF326A4.root',
#        '/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/320/497/00000/9A87F260-CB93-E811-875D-FA163EA379FB.root',
#        '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/497/00000/00C024D9-C893-E811-BE8B-FA163E085754.root',
#    ),
#
#    inputCommands = cms.untracked.vstring(
#        'keep *'
#    )
#)

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

