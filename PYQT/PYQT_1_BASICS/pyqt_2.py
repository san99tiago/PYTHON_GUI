# BASICS OF PYQT5
# Santiago Garcia Arango, July 2020
# Tutorial based on <sentdex: PyQt Python GUI Application Development>

"""
Remark: these first scripts are over-commented, so that anyone can read them
and get the basic understanding of the PyQt library.
"""

import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

# Get the path for the assets folder
CURRENT_FOLDER = os.path.dirname( __file__ )
PATH_TO_ASSETS = os.path.join(CURRENT_FOLDER, "assets")

# Now we will work with an "Object Oriented Programming" approach with PyQt5
# We must inherit from the QMainWindow class, so we can use its own methods
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 2560, 1440)
        self.setWindowTitle(" SAN99TIAGO")

        path_to_icon = os.path.join(PATH_TO_ASSETS, "python_ico.ico")
        self.setWindowIcon(QIcon(path_to_icon))

        self.show()

# Create and run main app using the already created Window class
app = QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
