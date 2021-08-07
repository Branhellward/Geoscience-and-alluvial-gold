import sys
from window import *


class gce(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_gce()
        self.ui.setupUi(self)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = gce()
    myapp.show()
    sys.exit(app.exec_())