import os
import logging

from pyCGM2.Utils import files
from pyCGM2.Tools import btkTools
from pyCGM2.ForcePlates import forceplates
from pyCGM2 import enums
from pyCGM2.Nexus import vskTools

#NEED TO SELECT WHICH MODEL RUNNING
#from pyCGM2.Lib.CGM import cgm2_1
from pyCGM2.Lib.CGM import cgm1


#DATA_PATH = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Data\\MCLA\\'
#I think the below path points to the CGM2 files pulled from the Beta arm of the Fabien's site
pyCGM2_path = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Automate_looping_files\\pyCGM2-Master\\pyCGM2'

#Modify to suit local disk files
parent_folder_path = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Data\\'

# Configure the logging settings
logging.basicConfig(filename='logfile.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def model_static_CGM2(parent_folder_path, folder_name, cal_filename, vsk_filename):
    DATA_PATH = parent_folder_path+folder_name
    staticFile = cal_filename
    vskfile = vsk_filename
    #NEED TO SELECT WHICH MODEL RUNNING
    #settings = files.loadModelSettings(pyCGM2_path,"CGM1-pyCGM2.settings")
    settings = files.loadModelSettings(pyCGM2_path + "\\Settings", "CGM1-pyCGM2.settings")
    print(settings)
    # CALIBRATION--------------------------------
    #staticFile ="CPD8743248 - MCLA Cal 02.c3d" <<<<NEED TO MAKE THIS THE STATIC FILE IT lOOPS
    #acqStatic = btkTools.smartReader(DATA_PATH+staticFile)

    acqStatic = btkTools.smartReader(folder_path+folder_name+file_name)

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
    #vsk = vskTools.Vsk(DATA_PATH + "New Subject.vsk")
    #required_mp,optional_mp = vskTools.getFromVskSubjectMp(vsk, resetFlag=True)
    required_mp,optional_mp = vskTools.getFromVskSubjectMp(vskfile, resetFlag=True)

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

#def model_dynamic_CGM2(parent_folder_path, folder_name, dynamic_filename)
    # trialName = dynamic_filename
    # DATA_PATH = parent_folder_path+folder_name
    # momentProjection = enums.enumFromtext(settings["Fitting"]["Moment Projection"],enums.MomentProjection)
    # pointSuffix = settings["Global"]["Point suffix"]
    #
    #
    # # force plate assignment to start from c3d
    # #acq = btkTools.smartReader(DATA_PATH+trialName)
    # acq = btkTools.smartReader(parent_folder_path + folder_name + trialName)
    # mfpa = forceplates.matchingFootSideOnForceplate(acq)
    #
    # acqGait,detectAnomaly = cgm1.fitting(model,DATA_PATH, trialName,
    #     translators,
    #     markerDiameter,
    #     pointSuffix,
    #     mfpa,
    #     momentProjection,
    #     frameInit= None, frameEnd= None )
    #
    # btkTools.smartWriter(acqGait, DATA_PATH+trialName[:-4]+"-modelled.c3d")
    # print("Model",model)

def loop_build_filename_list(parent_folder_path, search_string_cal="Cal", search_string_c3d = ".c3d", search_string_vsk=".vsk"):
    calfile_list = []  # Start a list that adds Cal .c3d files to
    dynamicfile_list = [] #Start a list that adds dynamic trial .c3d files to
    vskfile_list = [] # Start a list that adds VSK files to
    otherfile_list = [] # Start a list for files that don't have "Cal"

    for folder_name in os.listdir(parent_folder_path):
        folder_path = os.path.join(parent_folder_path, folder_name)
        if os.path.isdir(folder_path):  # Only consider folders (not files)
            print(f'Files in {folder_name}:')
            run_it_son()
            logging.info(f"File path: {parent_folder_path}")

            for file_name in os.listdir(folder_path):
                if os.path.isfile(os.path.join(folder_path, file_name)):  # Only consider files (not directories)
                    print(f'\t{file_name}')
                    logging.info(f"Folder name: {folder_name}")
                    if search_string_cal in file_name and search_string_c3d in file_name:  # Search for "Cal" AND ".c3d" in the filename
                        print(f"Found '{search_string_cal}' in file name: {file_name}")  # Return filename with "Cal"
                        calfile_list.append(file_name)
                        logging.info(f"Processing file: {file_name}")
                    elif search_string_c3d in file_name and search_string_cal not in file_name:  # Search for ".c3d" files and exclude "Cal" in the filename to filter for dynamic trials
                        print(f"Found 'dynamic trial' in file name: {file_name}")  # Return filename that meets above rule
                        dynamicfile_list.append(file_name)
                        logging.info(f"Processing file: {file_name}")
                    elif search_string_vsk in file_name:  # Search for ".vsk" in the filename
                        print(f"Found '{search_string_vsk}' in file name: {file_name}")  # Return filename with ".vsk"
                        vskfile_list.append(file_name)
                        logging.info(f"Processing file: {file_name}")
                    else:
                        otherfile_list.append(file_name)
                        logging.info(f"Processing file: {file_name}")

#NEED TO FIGURE OUT HOW TO RUN CODE THAT CALLS ALL FUNCTIONS
#FOR EXAMPLE, FINDS CAL AND VSK, RUNS STATIC CGM2
# THEN FINDS DYNAMIC AND RUNS DYNAMIC CGM2

