import openpyxl
import sys
from window import*


class reverse_export_xy(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_reverse_export_xy()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = reverse_export_xy()
    myapp.show()
    sys.exit(app.exec_())