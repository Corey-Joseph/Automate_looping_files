#31/08/2023
#This will run perfectly and output filenames
#Interpreter is 'Loop_build_filename_list'

import os

#LOOPING THROUGH FOLDERS IN DIRECTORY

parent_folder_path = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Data\\'

for folder_name in os.listdir(parent_folder_path):
    folder_path = os.path.join(parent_folder_path, folder_name)
    if os.path.isdir(folder_path):  # Only consider folders (not files)
        print(f'Files in {folder_name}:')
        for file_name in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file_name)):  # Only consider files (not directories)
                print(f'\t{file_name}')