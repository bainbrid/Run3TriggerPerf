from CRABClient.UserUtilities import config #, getUsernameFromSiteDB
config = config()

config.General.requestName = 'JpsiK_20211212_HLTRAW'
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'EGM-Run3Winter21DRMiniAOD-00021_1_cfg.py'
config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 4

config.Data.inputDataset = '/BuToKJpsi_Toee_2021206/ytakahas-winter21-d68537ecb0111c6d02d9d0fcc3a0a6d8/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
#config.Data.totalUnits=30

config.Data.outLFNDirBase = '/store/user/ytakahas/' + config.General.requestName #% (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'Winter21_HLTRAW'
#config.Site.storageSite = 'T3_CH_PSI'
config.Site.storageSite = 'T2_CH_CSCS'
#config.Site.ignoreGlobalBlacklist = True
#config.Data.ignoreLocality = True
#config.Site.whitelist = ['T2_CH_*']
#config.Site.blacklist = ['T2_US_Purdue']


config.General.workArea = 'crab_HLTRAW'

#name = 'EphemeralZeroBias8'
#name = 'ZeroBias10'

#config.General.requestName = name
#config.Data.inputDataset = '/' + name + '/Run2018D-PromptReco-v2/MINIAOD'
#config.Data.secondaryInputDataset = '/' + name + '/Run2018D-v1/RAW'


#for a in [1,2,3,4,5,6,7]:
    
#
#'/EphemeralZeroBias1/Run2018D-PromptReco-v2/MINIAOD'
#'/EphemeralZeroBias2/Run2018D-PromptReco-v2/MINIAOD'
#'/EphemeralZeroBias3/Run2018D-PromptReco-v2/MINIAOD'
#'/EphemeralZeroBias4/Run2018D-PromptReco-v2/MINIAOD'
#'/EphemeralZeroBias5/Run2018D-PromptReco-v2/MINIAOD'
#'/EphemeralZeroBias6/Run2018D-PromptReco-v2/MINIAOD'
#'/EphemeralZeroBias7/Run2018D-PromptReco-v2/MINIAOD'
#'/EphemeralZeroBias8/Run2018D-PromptReco-v2/MINIAOD'
#
#'/EphemeralZeroBias1/Run2018D-v1/RAW'
#'/EphemeralZeroBias2/Run2018D-v1/RAW'
#'/EphemeralZeroBias3/Run2018D-v1/RAW'
#'/EphemeralZeroBias4/Run2018D-v1/RAW'
#'/EphemeralZeroBias5/Run2018D-v1/RAW'
#'/EphemeralZeroBias6/Run2018D-v1/RAW'
#'/EphemeralZeroBias7/Run2018D-v1/RAW'
#'/EphemeralZeroBias8/Run2018D-v1/RAW'




#config.General.requestName = 'EphemeralZeroBias3'
#config.Data.inputDataset = '/EphemeralZeroBias3/Run2018D-PromptReco-v2/MINIAOD'
#config.Data.secondaryInputDataset = '/EphemeralZeroBias3/Run2018D-v1/RAW'



