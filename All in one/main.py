import sys
from main_window import *
from PyQt5 import QtWidgets
from empty_table import empty_table
from txt_to_xlsx import Txt_to_xlsx
from txt_to_xlsx_xy import txt_to_xlxs_xy
from area_calculate import area_calculate
from reverse_export import reverse_export
from reverse_export_xy import reverse_export_xy
from geocalc_ext import gce


class all_in_one(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_all_in_one()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.e_t_window)
        self.ui.pushButton_2.clicked.connect(self.t_t_x_window)
        self.ui.pushButton_3.clicked.connect(self.t_t_x_xy_window)
        self.ui.pushButton_4.clicked.connect(self.a_c_window)
        self.ui.pushButton_9.clicked.connect(self.r_e_window)
        self.ui.pushButton_10.clicked.connect(self.r_e_xy_window)
        self.ui.pushButton_11.clicked.connect(self.g_c_e_window)

    def e_t_window(self):
        self.w2 = empty_table()
        self.w2.show()
    
    def t_t_x_window(self):
        self.w3 = Txt_to_xlsx()
        self.w3.show()

    def t_t_x_xy_window(self):
        self.w4 = txt_to_xlxs_xy()
        self.w4.show()
    
    def a_c_window(self):
        self.w5 = area_calculate()
        self.w5.show()

    def r_e_window(self):
        self.w6 = reverse_export()
        self.w6.show()
        
    def r_e_xy_window(self):
        self.w7 = reverse_export_xy()
        self.w7.show()

    def g_c_e_window(self):
        self.w8 = gce()
        self.w8.show()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = all_in_one()
    myapp.show()
    sys.exit(app.exec_())