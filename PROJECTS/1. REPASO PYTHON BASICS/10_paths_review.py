#REVIEW OF PATHS IN PYTHON TO ACCESS OTHER DIRECTORIES
#Santiago Garcia Arango, June 2020

import os
print( os.getcwd() ) #Current work directory (can change based on the directory from where this is run)
print( __file__ ) #Current path for this specific python file (always the same)
print( os.path.dirname( __file__) ) #Access the "parent directory" of the current python file executed
print( os.path.dirname( os.path.dirname( __file__ ) ) ) #Access upper folder two levels
