#this works and outputs modelled file 31/08/2023
import pyCGM2; LOGGER = pyCGM2.LOGGER
import os
import sys

import pyCGM2
from pyCGM2.Utils import files
from pyCGM2.Tools import btkTools
from pyCGM2.ForcePlates import forceplates
from pyCGM2 import enums

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

#NEED TO CHECK THE BELOW TO MAKE SURE IT READS THE ACUTAL MP
#FILE FOR THE SUBJECT OR WHETHER IT JUST USES THE MANUALLY
#ENTERED DATA HERE

# definitions from mp from metadata
required_mp = dict()
required_mp["Bodymass"] = 75.0
required_mp["Height"]= 1750
required_mp["LeftLegLength"] = 800
required_mp["LeftKneeWidth"] = 90
required_mp["RightLegLength"] = 800
required_mp["RightKneeWidth"] = 90
required_mp["LeftAnkleWidth"] = 60
required_mp["RightAnkleWidth"] = 60
required_mp["LeftSoleDelta"] = 0
required_mp["RightSoleDelta"] = 0
required_mp["LeftShoulderOffset"] = 0
required_mp["LeftElbowWidth"] = 0
required_mp["LeftWristWidth"] = 0
required_mp["LeftHandThickness"] = 0
required_mp["RightShoulderOffset"] = 0
required_mp["RightElbowWidth"] = 0
required_mp["RightWristWidth"] = 0
required_mp["RightHandThickness"]= 0

optional_mp = dict()
optional_mp["InterAsisDistance"]= 0
optional_mp["LeftAsisTrocanterDistance"]= 0
optional_mp["LeftTibialTorsion"]= 0
optional_mp["LeftThighRotation"]= 0
optional_mp["LeftShankRotation"]= 0
optional_mp["RightAsisTrocanterDistance"]= 0
optional_mp["RightTibialTorsion"]= 0
optional_mp["RightThighRotation"]= 0
optional_mp["RightShankRotation"]= 0


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

# FITTING ----------------------------------------------------------
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