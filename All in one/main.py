import sys
from main_window import *
from PyQt5 import QtWidgets


class all_in_one(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_all_in_one()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = all_in_one()
    myapp.show()
    sys.exit(app.exec_())