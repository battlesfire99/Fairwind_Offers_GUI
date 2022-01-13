import sys
from PyQt5 import QtWidgets, uic
import resources

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("gui.ui")
window.show()
app.exec_()

