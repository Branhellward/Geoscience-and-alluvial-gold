import sys
import openpyxl
import regex
import pandas as pd
from window import *


global select_file, output_txt

def geo_xlsx_to_txt():
    global select_file, output_txt  
    book = openpyxl.open(select_file, read_only=True)
    sheet = book.active

    output_file = open(output_txt,'w')

    for row in range (3,sheet.max_row+1):
        coord_line = str(
            sheet[row][0].value)+'; '+str(
                sheet[row][1].value)+' '+str(
                    sheet[row][2].value)+' '+str(
                        sheet[row][3].value)+'; '+str(
                            sheet[row][4].value)+' '+str(
                                sheet[row][5].value)+' '+str(
                                    sheet[row][6].value)+';\n'

        output_file.write(coord_line)
    output_file.close()

    open_file = open(output_txt).read()
    regular_ka = r'\1.\2'
    fine_text = regex.sub(r'(\d{0})+[.,]+(\d{0})',regular_ka ,open_file)

    wr = open(output_txt,'w')
    wr.write(fine_text)
    wr.close()

def xy_xlsx_to_txt():
    global select_file, output_txt
    book = openpyxl.open(select_file, read_only=True)
    sheet = book.active

    output_file = open(output_txt,'w')

    for row in range (2,sheet.max_row+1):
        coord_line = str(
            sheet[row][0].value)+'; '+str(
                sheet[row][1].value)+'; '+str(
                    sheet[row][2].value)+';\n'

        output_file.write(coord_line)
    output_file.close()

    open_file = open(output_txt).read()
    regular_ka = r'\1.\2'
    fine_text = regex.sub(r'(\d{0})+[.,]+(\d{0})',regular_ka ,open_file)

    wr = open(output_txt,'w')
    wr.write(fine_text)
    wr.close()


class gce(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_gce()
        self.ui.setupUi(self)
        
        self.ui.pushButton_3.clicked.connect(self.file_selection)
        self.ui.pushButton.clicked.connect(self.save_file_geo)
        self.ui.pushButton_2.clicked.connect(self.save_file_xy)
    
    def file_selection(self):
        global select_file
        self.label_status_calm()
        select_file = QFileDialog.getOpenFileName(self, "File selection", "Your file", "text (*.xlsx)")[0]
        if not select_file:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select a .xlsx file!')
        else:
            self.path_label()
            self.ui.pushButton.setDisabled(False)
            self.ui.pushButton_2.setDisabled(False)
        return select_file
    
    def save_file_geo(self):
        global output_txt
        output_txt = False
        output_txt = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "Your file", "*.txt")[0]
        if not output_txt:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select the name and path of the file!')
        else:
            geo_xlsx_to_txt()
            self.finish_label()
            self.ui.pushButton.setDisabled(True)
            self.ui.pushButton_2.setDisabled(True)

    def save_file_xy(self):
        global output_txt
        output_txt = False
        output_txt = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "Your file", "*.txt")[0]
        if not output_txt:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select the name and path of the file!')
        else:
            xy_xlsx_to_txt()
            self.finish_label()
            self.ui.pushButton.setDisabled(True)
            self.ui.pushButton_2.setDisabled(True)

    def path_label(self):
        self.ui.label_2.setText(select_file)
    
    def finish_label(self):
        self.ui.label_2.setText('Finish')

    def label_status_calm(self):
        self.ui.label_2.setText('Status')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = gce()
    myapp.show()
    sys.exit(app.exec_())