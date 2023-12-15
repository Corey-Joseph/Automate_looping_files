#this works and outputs modelled file 31/08/2023
import pyCGM2; LOGGER = pyCGM2.LOGGER
import os
import sys
import pyCGM2
from pyCGM2.Utils import files
from pyCGM2.Tools import btkTools
from pyCGM2.ForcePlates import forceplates
from pyCGM2 import enums
from pyCGM2.Nexus import vskTools

#NEED TO SELECT WHICH MODEL RUNNING
#from pyCGM2.Lib.CGM import cgm2_1
from pyCGM2.Lib.CGM import cgm1

DATA_PATH = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Data\\MCLA\\'
#pyCGM2_path = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\pyCGM2\\pyCGM2\\'
pyCGM2_path = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Automate_looping_files\\pyCGM2-Master\\pyCGM2'

# load the settings file. By default, it will look in pyCGM2/Settings
# you can copy and paste this settings and put it in your directory)
#NEED TO SELECT WHICH MODEL RUNNING
#settings = files.loadModelSettings(pyCGM2_path,"CGM1-pyCGM2.settings")
settings = files.loadModelSettings(pyCGM2_path + "\\Settings", "CGM1-pyCGM2.settings")
print(settings)
# CALIBRATION--------------------------------
staticFile ="CPD8743248 - MCLA Cal 02.c3d"
#staticFile = []
acqStatic = btkTools.smartReader(DATA_PATH+staticFile)

# choice of options
leftFlatFoot = settings["Calibration"]["Left flat foot"]
rightFlatFoot= settings["Calibration"]["Right flat foot"]
headFlat= settings["Calibration"]["Head flat"]
translators = settings["Translators"]
markerDiameter = settings["Global"]["Marker diameter"]
#HJC not applicable for 1.0 or 1.1
#HJC = settings["Calibration"]["HJC"]
pointSuffix = settings["Global"]["Point suffix"]


#Get MP data from vsk file
vsk = vskTools.Vsk(DATA_PATH + "New Subject.vsk")
required_mp,optional_mp = vskTools.getFromVskSubjectMp(vsk, resetFlag=True)


#model,finalAcqStatic,error = cgm2_1.calibrate(DATA_PATH,
    #staticFile,
    #translators,
    #required_mp,
    #optional_mp,
    #leftFlatFoot,
    #rightFlatFoot,
    #headFlat,
    #markerDiameter,
    #HJC,
    #pointSuffix)

#NEED TO SELECT WHICH MODEL RUNNING
#Because CGM1 doesnt have hara model, need to take out HJC from avove
model,finalAcqStatic,error = cgm1.calibrate(DATA_PATH,
    staticFile,
    translators,
    required_mp,
    optional_mp,
    leftFlatFoot,
    rightFlatFoot,
    headFlat,
    markerDiameter,
    pointSuffix)

#FITTING ----------------------------------------------------------
trialName = "MCLA Initial Ax  CGM2 BF02.c3d"

momentProjection = enums.enumFromtext(settings["Fitting"]["Moment Projection"],enums.MomentProjection)
pointSuffix = settings["Global"]["Point suffix"]


# force plate assignment to start from c3d
acq = btkTools.smartReader(DATA_PATH+trialName)
mfpa = forceplates.matchingFootSideOnForceplate(acq)

acqGait,detectAnomaly = cgm1.fitting(model,DATA_PATH, trialName,
    translators,
    markerDiameter,
    pointSuffix,
    mfpa,
    momentProjection,
    frameInit= None, frameEnd= None )

btkTools.smartWriter(acqGait, DATA_PATH+trialName[:-4]+"-modelled.c3d")
print("Model",model)