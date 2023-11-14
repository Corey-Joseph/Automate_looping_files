#works 14_09_23
import os
import pyCGM2
from pyCGM2.Utils import files
from pyCGM2.Tools import btkTools
from pyCGM2.Lib.CGM import cgm1  # Assuming you want to use cgm1
from pyCGM2 import enums


def calibrate_cgm1(data_path, static_file):
    # Load settings
    pyCGM2_path = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Automate_looping_files\\pyCGM2-Master\\pyCGM2'
    settings = files.loadModelSettings(pyCGM2_path + "\\Settings", "CGM1-pyCGM2.settings")

    # Load static acquisition
    acqStatic = btkTools.smartReader(os.path.join(data_path, static_file))

    #If we want to load the mp data we will need to use ViconNexus.py either to
    #access the function "NEXUS.GetSubjectParamDetails" or create our own based on the file detected in the  folder
    #we are looping through
    #if we use ViconNexus.py to get the function "NEXUS.GetSubjectParamDetails" then we need to make sure
    #the way we create the names of the subject when reading .mp file
    #for example, we need to create something line this:
    """def GetSubjectParamDetails(self, subject, param):
        Retrieve detailed information about a subject parameter

        Input
          subject = string, name of an existing subject
          param  = string, name an existing subject parameter
        Returns
          value  = floating point number, current value of the subject parameter
          unit   = string, unit associated with the value
          default = floating point number, PRIOR value of the subject parameter
          required = logical, indication as to whether the subject parameter is a required parameter
          hasvalue = logical, indication as to whether the subject parameter has a value

        .. code-block::

            Usage Example: Display subject parameter details

              value, unit, default, required = vicon.GetSubjectParamDetails( 'Colin', 'MyParam' )
              isRequired = ' Not Required'
              if( required ):
                isRequired = ' Required'

              SubjectParamInfo = 'MyParam = {0} [{1}] Default={2}, {3}'.format( value, unit, default, isRequired )
              print SubjectParamInfo
        """


    # Define required and optional metadata parameters
    required_mp = {
        "Bodymass": 75.0,
        "Height": 1750,
        "LeftLegLength" : 800,
        "LeftKneeWidth" : 90,
        "RightLegLength" : 800,
        "RightKneeWidth" : 90,
        "LeftAnkleWidth" : 60,
        "RightAnkleWidth" : 60,
        "LeftSoleDelta" : 0,
        "RightSoleDelta" : 0,
        "LeftShoulderOffset" : 0,
        "LeftElbowWidth" : 0,
        "LeftWristWidth" : 0,
        "LeftHandThickness" : 0,
        "RightShoulderOffset" : 0,
        "RightElbowWidth" : 0,
        "RightWristWidth" : 0,
        "RightHandThickness" : 0,
    }

    optional_mp = {
        "InterAsisDistance": 0,
        "InterAsisDistance" : 0,
        "LeftAsisTrocanterDistance" : 0,
        "LeftTibialTorsion" : 0,
        "LeftThighRotation" : 0,
        "LeftShankRotation" : 0,
        "RightAsisTrocanterDistance" : 0,
        "RightTibialTorsion" : 0,
        "RightThighRotation" : 0,
        "RightShankRotation" : 0,
    }

    # Other settings
    translators = settings["Translators"]
    leftFlatFoot = settings["Calibration"]["Left flat foot"]
    rightFlatFoot = settings["Calibration"]["Right flat foot"]
    headFlat = settings["Calibration"]["Head flat"]
    markerDiameter = settings["Global"]["Marker diameter"]
    pointSuffix = settings["Global"]["Point suffix"]

    # Calibrate using cgm1
    model, finalAcqStatic, error = cgm1.calibrate(
        data_path,
        static_file,
        translators,
        required_mp,
        optional_mp,
        leftFlatFoot,
        rightFlatFoot,
        headFlat,
        markerDiameter,
        pointSuffix
    )

    return model, finalAcqStatic, error


# Example usage:
# if __name__ == "__main__": # Check if this script is being run as the main program
#     DATA_PATH = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Data\\MCLA\\' # Define the file path where the data is stored
#     staticFile = "CPD8743248 - MCLA Cal 02.c3d" # Define the name of the specific file to operate on
#
#     # Call a function called calibrate_cgm1 with the data path and file name as arguments
#     # This function likely performs some data calibration or processing and returns three values
#     model, finalAcqStatic, error = calibrate_cgm1(DATA_PATH, staticFile)
#
#     # You can use the variables model, finalAcqStatic, and error as needed
