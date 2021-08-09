import xlsxwriter
import sys
import regex
import pandas as pd
from window import *


def xy_txt_to_xlsx():
    global select_file, output_xlsx
    open_file = open(select_file).read()
    cleaner = r'\1.\2'
    fine_text = regex.sub(r'(\d{0})+[.,]+(\d{0})',cleaner ,open_file)

    wr = open(select_file,'w')
    wr.write(fine_text)
    wr.close()

    data = pd.read_csv(select_file, encoding='cp1251', header=None, sep=r"\s+", names=None, )

    workbook = xlsxwriter.Workbook(output_xlsx)
    worksheet = workbook.add_worksheet('Coordinates')

    worksheet.set_column('B:C', 16.22)
    worksheet.set_column('D:E', 24.33)

    write_format_hat = workbook.add_format({
            'font': 'Times New Roman',
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'white'})

    write_format = workbook.add_format({
            'bold': 0,
            'border': 1,
            'num_format': "0.000",
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'white'})

    worksheet.write('A1', '№№', write_format_hat)
    worksheet.write('B1', 'X', write_format_hat)
    worksheet.write('C1', 'Y', write_format_hat)

    a = 0
    data_shape_2 = data.shape[0] - 1
    bcolmn = 'B'
    b = 0
    ccolmn = 'C'
    c = 0

    while a < data_shape_2:
        vertical = ('A' + str(a + 2))
        bb = (bcolmn + str(b + 2))
        cc = (ccolmn + str(c + 2))

        iat_data_2 = float(data.iat[a, 0])
        iat_data_1 = float(data.iat[a, 1])

        worksheet.write(bb, iat_data_2, write_format)
        worksheet.write(cc, iat_data_1, write_format) 

        a += 1
        b += 1 
        c += 1

        worksheet.write(vertical, a, write_format_hat)

    workbook.close()


class txt_to_xlxs_xy(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_5.clicked.connect(self.open_file_txt)
        self.ui.pushButton_4.clicked.connect(self.save_file_xlsx_xy)
        
    def open_file_txt(self):
        global select_file
        select_file = QFileDialog.getOpenFileName(self, "File selection", "Your file", "text (*.txt)")[0]
        if not select_file:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select a .txt file!')
        else:
            self.path_label()
            self.ui.pushButton_4.setDisabled(False)
        return select_file

    def save_file_xlsx_xy(self):
        global output_xlsx
        output_xlsx = False
        output_xlsx = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "Your file", "*.xlsx")[0]
        if not output_xlsx:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select the name and path of the file!')
        else:
            xy_txt_to_xlsx()
            self.finish_label()
            self.ui.pushButton_4.setDisabled(True)

    def path_label(self):
        self.ui.label_4.setText(select_file)

    def finish_label(self):
        self.ui.label_4.setText('Finish')

    def label_status_calm(self):
        self.ui.label_4.setText('Status')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = txt_to_xlxs_xy()
    myapp.show()
    sys.exit(app.exec_())