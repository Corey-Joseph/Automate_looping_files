from pyCGM2 import btk
import pyCGM2.Lib.CGM.cgm1  # Import the cgm1 module from the pyCGM2 package
from pyCGM2.Utils import files
from pyCGM2.ForcePlates import forceplates
from pyCGM2.Tools import btkTools
from pyCGM2 import enums


# Define your input data and arguments
model = "CGM1.0"  # Replace with actual model data
DATA_PATH = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Data\\MCLA\\'
pyCGM2_path = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Automate_looping_files\\pyCGM2-Master\\pyCGM2'
reconstructFilenameLabelled = "MCLA Initial Ax  CGM2 BF02.c3d"
trialName = "MCLA Initial Ax  CGM2 BF02.c3d"
translators = {'translate_x': 0, 'translate_y': 0, 'translate_z': 0}
markerDiameter = 14.0
settings = files.loadModelSettings(pyCGM2_path + "\\Settings", "CGM1-pyCGM2.settings")
pointSuffix = settings["Global"]["Point suffix"]
acq = btkTools.smartReader(DATA_PATH+trialName)
mfpa = mfpa = forceplates.matchingFootSideOnForceplate(acq)
momentProjection = enums.enumFromtext(settings["Fitting"]["Moment Projection"],enums.MomentProjection)


# Call the fitting function with the provided arguments
result = pyCGM2.Lib.CGM.cgm1.fitting(
    model,
    DATA_PATH,
    reconstructFilenameLabelled,
    translators,
    markerDiameter,
    pointSuffix,
    mfpa,
    momentProjection
)

# Process the result or use it as needed
print("Fitting result:", result)
