import Model_cgm2_static as cgm2s
import Loop_build_filename_list as fnl

#THINGS TO MAKE SURE OF
#1 NEED TO CHECK THE BELOW TO MAKE SURE IT READS THE ACUTAL MP
#FILE FOR THE SUBJECT OR WHETHER IT JUST USES THE MANUALLY
#ENTERED DATA HERE

#2 CREATE A LOG FILE SO IT CAN BE CHECKED WHICH DATA IS RUN

#3 CREATE A WAY TO LOOK FOR 'cal' IN FILENAME AND RUN STATIC ON THAT FILE
# THIS NEEDS MY SCRIPT TO BE SPLIT INTO STATIC AND DYNAMIC I THINK

DATA_PATH = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Data\\MCLA\\'
#I think the below path points to the CGM2 files pulled from the Beta arm of the Fabien's site
pyCGM2_path = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Automate_looping_files\\pyCGM2-Master\\pyCGM2'

parent_folder_path = 'C:\\Users\\Helen laptop\\Documents\\CGM2project\\Data\\'

filenames = []  #ASSUMING I NEED THIS TO READ FILENAME AND RUN CGM2 ON THAT FILE

staticfile = []

cal_files = loop_build_filename_list(parent_folder_path)

for file_name in calfile_list:
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'r') as file:
        file_contents = file.read()
        # Perform operations on file_contents or run code on the file as needed
        script_to_run = cgm2s  # Replace with the name of your Python script
        # Execute the Python script with the file name as an argument
        subprocess.run(['python', script_to_run, file_path, calfile_list])
        print(f"Processing file '{file_name}':\n{file_contents}")
