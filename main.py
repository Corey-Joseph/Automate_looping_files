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
