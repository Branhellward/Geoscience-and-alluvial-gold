import sys
import pandas as pd
import xlsxwriter
import regex
from window import *

global reg_ex, file_name_2, output_2, open_first_2


def make_xlsx():
    global reg_ex, open_first_2
    open_first_2 = open(file_name_2).read()

    fin_fi_2 = regex.sub(r'(\d\d)+[.,]+(\d)+(\d)+(\d)+(\d)', reg_ex, open_first_2) \
        .replace('N', '') \
        .replace('E', '') \
        .replace('°', '') \
        .replace('\'', '') \
        .replace('\"', '') \

    f = open('encoding.txt', 'w')
    f.write(fin_fi_2)
    f.close()
    data = pd.read_csv('encoding.txt', encoding='cp1251', header=None, sep=r"\s+", names=None, )
    workbook = xlsxwriter.Workbook(output_2)
    worksheet = workbook.add_worksheet('Coordinates')

    merge_format = workbook.add_format({
        'bold': 0,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    write_format = workbook.add_format({
        'bold': 0,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    write_format1 = workbook.add_format({
        'num_format': '00',
        'bold': 0,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    worksheet.merge_range('A1:A2', '№№', merge_format)
    worksheet.merge_range('B1:D1', 'Северная широта', merge_format)
    worksheet.merge_range('E1:G1', 'Восточная долгота', merge_format)
    worksheet.write('B2', 'Градусы', write_format)
    worksheet.write('C2', 'Минуты', write_format)
    worksheet.write('D2', 'Секунды', write_format)
    worksheet.write('E2', 'Градусы', write_format)
    worksheet.write('F2', 'Минуты', write_format)
    worksheet.write('G2', 'Секунды', write_format)
    worksheet.write('A1', '№№', write_format1)

    a = 0
    z = data.shape[0]
    bcolmn = 'B'
    b = 0
    ccolmn = 'C'
    c = 0
    dcolmn = 'D'
    d = 0
    ecolmn = 'E'
    e = 0
    fcolmn = 'F'
    f = 0
    gcolmn = 'G'
    g = 0
    yy = -1

    while a < z:
        a += 1
        b += 1
        c += 1
        d += 1
        e += 1
        f += 1
        g += 1
        yy += 1
        vertical_2 = ('A' + str(a + 2))
        bb = (ecolmn + str(b + 2))
        cc = (fcolmn + str(c + 2))
        dd = (gcolmn + str(d + 2))
        ee = (bcolmn + str(e + 2))
        ff = (ccolmn + str(f + 2))
        gg = (dcolmn + str(g + 2))

        worksheet.write(vertical_2, a, write_format)
        worksheet.write(bb, data.iat[yy, 0], write_format)
        worksheet.write(cc, data.iat[yy, 1], write_format1)
        worksheet.write(dd, data.iat[yy, 2], write_format1)
        worksheet.write(ee, data.iat[yy, 3], write_format)
        worksheet.write(ff, data.iat[yy, 4], write_format1)
        worksheet.write(gg, data.iat[yy, 5], write_format1)

    workbook.close()


class Txt_to_xlsx(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Txt_to_xlsx()
        self.ui.setupUi(self)

        self.ui.pushButton_8.clicked.connect(self.notification)
        self.ui.pushButton_6.clicked.connect(self.open_file_txt)
        self.ui.pushButton_7.clicked.connect(self.button_handler)
        self.ui.pushButton_7.setDisabled(True)

    def button_handler(self):

        global output_2
        output_2 = False
        output_2 = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "Your file", "*.xlsx")[0]
        if not output_2:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select the name and path of the file!')
        else:
            self.inside_engine()
            self.finish_label()
            self.ui.pushButton_7.setDisabled(True)

    def open_file_txt(self):
        global file_name_2
        file_name_2 = QFileDialog.getOpenFileName(self, "File selection", "Your file", "text (*.txt)")[0]
        if not file_name_2:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select a .txt file!')
        else:
            self.label_path_2()
            self.ui.pushButton_7.setDisabled(False)
        return file_name_2

    def inside_engine(self):
        global reg_ex

        if self.ui.radioButton.isChecked():
            reg_ex = r'\1'
            make_xlsx()
        elif self.ui.radioButton_2.isChecked():
            reg_ex = r'\1,\2'
            make_xlsx()
        elif self.ui.radioButton_3.isChecked():
            reg_ex = r'\1,\2\3'
            make_xlsx()
        elif self.ui.radioButton_4.isChecked():
            reg_ex = r'\1,\2\3\4'
            make_xlsx()
        elif self.ui.radioButton_5.isChecked():
            reg_ex = r'\1,\2\3\4\5'
            make_xlsx()

    def label_path_2(self):
        self.ui.label_7.setText(file_name_2)

    def finish_label(self):
        finish_name = 'Finish'
        self.ui.label_7.setText(finish_name)

    def notification(self):

        QtWidgets.QMessageBox.about(self, 'Instruction', '''
Txt Xlsx

1. The necessary lines, areas and points - must be
            Projection:
            Geographic (Latitude/Longitude)
            Zone:
            Which you need
            Datum:
            Which you need, for ex. (S-42 (PULKOVO 1942))
            Planar Units:
            ARC DEGREES
2. Export the object we need:
    File - Export - Export Vector/Lidar Format..
3. Select Export Format = Text File
4. Apply the settings:
    Coordinate Separator: (TAB)
    Feature Separator: (NONE)
    Coordinate Order/Format: X
    Coordinate Precision: Use Default Precision Based on Units
    Others don't need to select
5. OK
6. Select a text file with coordinates
7. Click the button "Convert"
8. Select the name and path of the file (.xlsx)
9. Click "Save file"
''')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Txt_to_xlsx()
    myapp.show()
    sys.exit(app.exec_())
