#SIMPLE CLASS TO PLAY AROUND WITH RANDOM NAMES FROM 3 TXT FILES
#Santiago Garcia Arango
#One of the modules to show how to create a simple package in python.

import random
import os

#Get the path to the directory of this specific python script
CURRENT_PATH = os.path.abspath( os.path.dirname( __file__ ) )

#Get the path to the files that contain the "MINI-DATABASE" for the names generation
PATH_TO_MALE_NAMES = CURRENT_PATH + "\\male_first_names.txt"
PATH_TO_FEMALE_NAMES = CURRENT_PATH + "\\female_first_names.txt"
PATH_TO_LAST_NAMES = CURRENT_PATH + "\\last_names.txt"


class name_generator:
    def __init__(self):
        pass

    def return_first_name(self):
        #We choose randomly between males and females
        self.is_male = random.randint(0,1)

        #We validate if the name is male or female
        if self.is_male:
            txt = open( PATH_TO_MALE_NAMES, "r")
            lines_info = txt.readlines()
            self.name = random.choice( lines_info ).strip()
            txt.close()
        else:
            txt = open( PATH_TO_FEMALE_NAMES, "r")
            lines_info = txt.readlines()
            self.name = random.choice( lines_info ).strip()
            txt.close()
        
        return self.name
    
    def return_last_name(self):
        txt = open( PATH_TO_LAST_NAMES, "r")
        lines_info = txt.readlines()
        self.last_name = random.choice( lines_info ).strip()
        txt.close()

        return self.last_name

#------------------------------------------------------------------------
#TEST THE SCRIPT TO GENERATE SOME RANDOM NAMES AND LAST_NAMES
names = name_generator()
print( "RANDOM FIRST NAME = ", names.return_first_name() )
print( "RANDOM LAST NAME = ", names.return_last_name() )
