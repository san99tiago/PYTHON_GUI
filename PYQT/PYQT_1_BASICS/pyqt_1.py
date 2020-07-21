# BASICS OF PYQT5
# Santiago Garcia Arango, July 2020
# Tutorial based on <sentdex: PyQt Python GUI Application Development>

"""
Remark: these first scripts are over-commented, so that anyone can read them
and get the basic understanding of the PyQt library.
The are NOT intended to be totally efficient or following global standards.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Create main app, where the parameter is by convention the argv connection
app = QApplication(sys.argv)

# Creation of main window, its geometry and the title
window = QWidget()
window.setGeometry(100, 100, 2560, 1440)  # May change based on screen-size
window.setWindowTitle("San99tiago")

# Always include the creation of the actual window and the exit method
window.show()
sys.exit(app.exec_())
