# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/EGM-Run3Winter21GS-00003-fragment.py --python_filename EGM-Run3Winter21GS-00003_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:EGM-Run3Winter21GS-00003.root --conditions 112X_mcRun3_2021_realistic_v15 --beamspot Run3RoundOptics25ns13TeVLowSigmaZ --step GEN,SIM --geometry DB:Extended --era Run3 --no_exec --mc -n 7156
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

#import sys
#args = sys.argv
#
#print '.............. enter GS_step1_template.py ............'
#
#lhe = 'None'
#nmax = 1
#
#if len(args)!=7:
#    print 'Provide [sample][index][lhe file][nmax][seed]', len(args)
#    sys.exit(0)
#else:
#    sample = args[2]
#    index = args[3]
#    nmax = int(args[4])
#    seed = int(args[5])
#    cdir = args[6]
#
#
#print 'sample name = ', sample
#print 'index = ', index
#print 'nmax = ', nmax
#print 'seed = ', seed
#print 'current_dir = ', cdir



process = cms.Process('SIM',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRun3RoundOptics25ns13TeVLowSigmaZ_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
#        input = cms.untracked.int32(nmax),
        input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
#    FailPath = cms.untracked.vstring(),
#    IgnoreCompletely = cms.untracked.vstring(),
#    Rethrow = cms.untracked.vstring(),
#    SkipEvent = cms.untracked.vstring(),
#    allowUnscheduled = cms.obsolete.untracked.bool,
#    canDeleteEarly = cms.untracked.vstring(),
#    emptyRunLumiMode = cms.obsolete.untracked.string,
#    eventSetup = cms.untracked.PSet(
#        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
#            allowAnyLabel_=cms.required.untracked.uint32
#        ),
#        numberOfConcurrentIOVs = cms.untracked.uint32(1)
#    ),
#    fileMode = cms.untracked.string('FULLMERGE'),
#    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
#    makeTriggerResults = cms.obsolete.untracked.bool,
#    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
#    numberOfConcurrentRuns = cms.untracked.uint32(1),
#    numberOfStreams = cms.untracked.uint32(0),
#    numberOfThreads = cms.untracked.uint32(1),
#    printDependencies = cms.untracked.bool(False),
#    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
#    throwIfIllegalParameter = cms.untracked.bool(True),
#    wantSummary = cms.untracked.bool(False)
)

#process.RandomNumberGeneratorService.generator.initialSeed = seed


# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/BPH-RunIISummer20UL18GEN-00073-fragment.py nevts:14400'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)


# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:BPH-RunIIFall18GS-00180.root'),
#    fileName = cms.untracked.string("file:" + cdir + "/GS_" + sample + "_" + index + ".root"),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '112X_mcRun3_2021_realistic_v15', '')

process.bctoefilter = cms.EDFilter("BCToEFilter",
    filterAlgoPSet = cms.PSet(
        eTThreshold = cms.double(10),
        genParSource = cms.InputTag("genParticlesForFilter")
    )
)


process.emenrichingfilter = cms.EDFilter("EMEnrichingFilter",
    filterAlgoPSet = cms.PSet(
        caloIsoMax = cms.double(10.0),
        clusterThreshold = cms.double(20.0),
        genParSource = cms.InputTag("genParticlesForFilter"),
        hOverEMax = cms.double(0.5),
        isoConeSize = cms.double(0.2),
        isoGenParConeSize = cms.double(0.1),
        isoGenParETMin = cms.double(20.0),
        requireTrackMatch = cms.bool(False),
        tkIsoMax = cms.double(5.0)
    )
)


process.decayfilter = cms.EDFilter("PythiaDauVFilter",
    DaughterIDs = cms.untracked.vint32(321, 11, -11),
    MaxEta = cms.untracked.vdouble(9999.0, 9999.0, 9999.0),
    MinEta = cms.untracked.vdouble(-9999.0, -9999.0, -9999.0),
    MinPt = cms.untracked.vdouble(-1.0, -1.0, -1.0),
    NumberDaughters = cms.untracked.int32(3),
    ParticleID = cms.untracked.int32(521),
    verbose = cms.untracked.int32(1)
)





process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            list_forced_decays = cms.vstring('MyB+','MyB-'),        
            operates_on_particles = cms.vint32(),    # we care just about our signal particles
            convertPythiaCodes = cms.untracked.bool(False),
            #user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Bu_KJpsi_ee.dec')
                user_decay_embedded= cms.vstring(
"""
#
# This is the decay file for the decay B+ -> J/Psi K + -> E+ E- K+
#
Alias      MyB+        B+
Alias      MyB-        B-
ChargeConj MyB-        MyB+
Alias      MyJpsi      J/psi
ChargeConj MyJpsi      MyJpsi
#
Decay MyB+
  1.000    MyJpsi      K+             SVS;
Enddecay
CDecay MyB-
#
Decay MyJpsi
  1.000         e+       e-         PHOTOS VLL;
Enddecay
#
End
"""
                        ),
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),

    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'processParameters'
        ),
        processParameters = cms.vstring(
            'SoftQCD:nonDiffractive = on', 
            'PTFilter:filter = on', 
            'PTFilter:quarkToFilter = 5', 
            'PTFilter:scaleToFilter = 1.0', 
#            '300553:new = 300553 -300553 1 0 0 1.0579400e+01 2.0500001e-02 10.5584 10.6819 0.0000000e+00', 
#            '100313:new = 100313 -100313 1 0 0 1.4140000e+00 2.3199996e-01 0.254 2.574 0.0000000e+00', 
#            '100323:new = 100323 -100323 1 1 0 1.4140000e+00 2.3199996e-01 0.254 2.574 0.0000000e+00', 
#            '30343:new = 30343 -30343 1 0 0 1.6000000e+00 0.0000000e+00 1.6 1.6 0.0000000e+00', 
#            '30353:new = 30353 -30353 1 1 0 1.6000000e+00 0.0000000e+00 1.6 1.6 0.0000000e+00', 
#            '30363:new = 30363 -30363 1 0 0 1.8000000e+00 0.0000000e+00 1.8 1.8 0.0000000e+00', 
#            '9020221:new = 9020221 -9020221 0 0 0 1.4089000e+00 5.1100000e-02 1.1534 1.6644 3.8616000e-12', 
#            '9000443:new = 9000443 -9000443 1 0 0 4.0390000e+00 8.0000005e-02 3.639 4.439 0.0000000e+00', 
#            '9010443:new = 9010443 -9010443 1 0 0 4.1530000e+00 7.8000000e-02 3.763 4.543 0.0000000e+00', 
#            '9020443:new = 9020443 -9020443 1 0 0 4.4210000e+00 6.1999976e-02 4.111 4.731 0.0000000e+00', 
#            '110551:new = 110551 -110551 0 0 0 1.0232500e+01 0.0000000e+00 10.2325 10.2325 0.0000000e+00', 
#            '120553:new = 120553 -120553 1 0 0 1.0255500e+01 0.0000000e+00 10.2555 10.2555 0.0000000e+00', 
#            '100555:new = 100555 -100555 2 0 0 1.0268600e+01 0.0000000e+00 10.2686 10.2686 0.0000000e+00', 
#            '210551:new = 210551 -210551 0 0 0 1.0500700e+01 0.0000000e+00 10.5007 10.5007 0.0000000e+00', 
#            '220553:new = 220553 -220553 1 0 0 1.0516000e+01 0.0000000e+00 10.516 10.516 0.0000000e+00', 
#            '200555:new = 200555 -200555 2 0 0 1.0526400e+01 0.0000000e+00 10.5264 10.5264 0.0000000e+00', 
#            '130553:new = 130553 -130553 1 0 0 1.0434900e+01 0.0000000e+00 10.4349 10.4349 0.0000000e+00', 
#            '30553:new = 30553 -30553 1 0 0 1.0150100e+01 0.0000000e+00 10.1501 10.1501 0.0000000e+00', 
#            '20555:new = 20555 -20555 2 0 0 1.0156200e+01 0.0000000e+00 10.1562 10.1562 0.0000000e+00', 
#            '120555:new = 120555 -120555 2 0 0 1.0440600e+01 0.0000000e+00 10.4406 10.4406 0.0000000e+00', 
#            '557:new = 557 -557 3 0 0 1.0159900e+01 0.0000000e+00 10.1599 10.1599 0.0000000e+00', 
#            '100557:new = 100557 -100557 3 0 0 1.0444300e+01 0.0000000e+00 10.4443 10.4443 0.0000000e+00', 
#            '110553:new = 110553 -110553 1 0 0 1.0255000e+01 0.0000000e+00 10.255 10.255 0.0000000e+00', 
#            '210553:new = 210553 -210553 1 0 0 1.0516000e+01 0.0000000e+00 10.516 10.516 0.0000000e+00', 
#            '110555:new = 110555 -110555 2 0 0 1.0441000e+01 0.0000000e+00 10.441 10.441 0.0000000e+00', 
#            '10555:new = 10555 -10555 2 0 0 1.0157000e+01 0.0000000e+00 10.157 10.157 0.0000000e+00', 
#            '13124:new = 13124 -13124 1.5 0 0 1.6900000e+00 6.0000018e-02 1.39 1.99 0.0000000e+00', 
#            '43122:new = 43122 -43122 0.5 0 0 1.8000000e+00 2.9999996e-01 0.3 3.3 0.0000000e+00', 
#            '53122:new = 53122 -53122 0.5 0 0 1.8100000e+00 1.5000001e-01 1.06 2.56 0.0000000e+00', 
#            '13126:new = 13126 -13126 2.5 0 0 1.8300000e+00 9.5000007e-02 1.355 2.305 0.0000000e+00', 
#            '13212:new = 13212 -13212 0.5 0 0 1.6600000e+00 1.0000000e-01 1.16 2.16 0.0000000e+00', 
#            '3126:new = 3126 -3126 2.5 0 0 1.8200000e+00 7.9999995e-02 1.42 2.22 0.0000000e+00', 
#            '3216:new = 3216 -3216 2.5 0 0 1.7750000e+00 1.1999999e-01 1.175 2.375 0.0000000e+00', 
#            '14124:new = 14124 -14124 2.5 1 0 2.626600 0 2.626600 2.626600 0.0000000e+00'
        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118', 
            'SigmaTotal:mode = 0', 
            'SigmaTotal:sigmaEl = 21.89', 
            'SigmaTotal:sigmaTot = 100.309', 
            'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
#            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'
        )
    ),
    comEnergy = cms.double(14000.0),
    convertPythiaCodes = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)


process.bufilter = cms.EDFilter("PythiaFilter",
    MaxEta = cms.untracked.double(9999.0),
    MinEta = cms.untracked.double(-9999.0),
    ParticleID = cms.untracked.int32(521)
)


process.decayfilterpositiveleg = cms.EDFilter(
    "PythiaDauVFilter",
    verbose         = cms.untracked.int32(1),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID      = cms.untracked.int32(521),  ## Bu
    DaughterIDs     = cms.untracked.vint32(443, 321), ## J/psi and K+
    MinPt           = cms.untracked.vdouble(-1., -1.),
    MinEta          = cms.untracked.vdouble(-9999., -9999.),
    MaxEta          = cms.untracked.vdouble( 9999.,  9999.)
    )

process.jpsifilter = cms.EDFilter(
    "PythiaDauVFilter",
    verbose         = cms.untracked.int32(1), 
    NumberDaughters = cms.untracked.int32(2), 
    MotherID        = cms.untracked.int32(521),  
    ParticleID      = cms.untracked.int32(443),  
    DaughterIDs     = cms.untracked.vint32(11, -11),
    MinPt           = cms.untracked.vdouble(-1., -1.), 
    MinEta          = cms.untracked.vdouble(-9999., -9999.), 
    MaxEta          = cms.untracked.vdouble(9999., 9999.)
    )



process.ProductionFilterSequence = cms.Sequence(process.generator+process.bufilter+process.decayfilterpositiveleg + process.jpsifilter)


#process.ProductionFilterSequence = cms.Sequence(process.generator+process.genParticlesForFilter+~process.bctoefilter+process.emenrichingfilter)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.ProductionFilterSequence)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
