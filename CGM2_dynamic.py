#FITTING ----------------------------------------------------------
import pyCGM2
from pyCGM2 import enums
from pyCGM2.Utils import files
from pyCGM2.Tools import btkTools
from pyCGM2.Lib.CGM import cgm1  # Assuming you want to use cgm1
from pyCGM2.ForcePlates import forceplates

pyCGM2_path = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Automate_looping_files\\pyCGM2-Master\\pyCGM2'
DATA_PATH = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Data\\MCLA\\'
settings = files.loadModelSettings(pyCGM2_path + "\\Settings", "CGM1-pyCGM2.settings")
trialName = "MCLA Initial Ax  CGM2 BF02.c3d"
model = "CGM1.0"
translators = settings["Translators"]
markerDiameter = settings["Global"]["Marker diameter"]

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