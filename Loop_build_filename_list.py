#15/12/2023
#This will run perfectly and output filenames
#Interpreter is 'Loop_build_filename_list'

#LOOPING THROUGH FOLDERS IN DIRECTORY
#OUTPUTTING CAL files, dynamic trial files, vsk files and all other files

import os
import logging

# Configure the logging settings
logging.basicConfig(filename='logfile.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def loop_build_filename_list(parent_folder_path, search_string_cal="Cal", search_string_c3d = ".c3d", search_string_vsk=".vsk"):
    calfile_list = []  # Start a list that adds Cal .c3d files to
    dynamicfile_list = [] #Start a list that adds dynamic trial .c3d files to
    vskfile_list = [] # Start a list that adds VSK files to
    otherfile_list = [] # Start a list for files that don't have "Cal"

    for folder_name in os.listdir(parent_folder_path):
        folder_path = os.path.join(parent_folder_path, folder_name)
        if os.path.isdir(folder_path):  # Only consider folders (not files)
            print(f'Files in {folder_name}:')
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

    print("Calibration files:")
    for file_name in calfile_list:
        print(file_name)

    print("Dynamic trial files:")
    for file_name in dynamicfile_list:
        print(file_name)

    print("vsk files:")
    for file_name in vskfile_list:
        print(file_name)

    print("All other files:")
    for file_name in otherfile_list:
        print(file_name)

    return calfile_list, dynamicfile_list, vskfile_list, otherfile_list

# Usage example:
parent_folder_path = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Data\\'
#cal_files, non_calfiles = loop_build_filename_list(parent_folder_path)
calfile_list, dynamicfile_list, vskfile_list, otherfile_list = loop_build_filename_list(parent_folder_path)
