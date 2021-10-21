import xlsxwriter
import sys
import pandas as pd
import regex

from area_calculate_windoow import *

global cleaner                                                  # Variable for regular expression
global dd, ee                                                   # Internal calculations for sum
global file_name, output_file_2


def make_xlsx_square():
    open_first = open(file_name).read()                         # Prepare file for further work
    global cleaner                                              # Use some regular expression
    cleaner = r'\1.\2'                                          #
    fine_txt = regex.sub(r'(\d{0})+[.,]+(\d)', cleaner, open_first)
    f = open(file_name, 'w')
    f.write(fine_txt)                                           # Write our file
    f.close()
    data = pd.read_csv(file_name, encoding='cp1251', header=None, sep=r"\s+", names=None)

    workbook = xlsxwriter.Workbook(output_file_2)               # Name of our .xlsx file
    worksheet = workbook.add_worksheet('Area calculate')

    worksheet.set_column('B:C', 16.22)                          # Set the cell width
    worksheet.set_column('D:E', 24.33)                          # Set the cell width

    write_format_hat = workbook.add_format({                    # Make style for table header
        'font': 'Times New Roman',
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    write_format_sum = workbook.add_format({                    # Make style for sum cells
        'bold': 1,
        'border': 1,
        'num_format': "0",
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    write_format_for_formula = workbook.add_format({            # Make style for formula cells
        'bold': 0,
        'border': 1,
        'num_format': "0",
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    write_format_square = workbook.add_format({                 # Make style for square digit cells
        'bold': 1,
        'border': 1,
        'num_format': '0.00000',
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    write_format = workbook.add_format({                        # Make style for other information
        'bold': 0,
        'border': 1,
        'num_format': "0.000",
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    worksheet.write('A1', '№№', write_format_hat)               #
    worksheet.write('B1', 'X', write_format_hat)                #
    worksheet.write('C1', 'Y', write_format_hat)                # Make the header of the table
    worksheet.write('D1', 'Xn*Yn+1', write_format_hat)          #
    worksheet.write('E1', 'Yn*Xn+1', write_format_hat)          #

    a = 0                                                       #
    data_shape = data.shape[0]                                  #
    data_shape_2 = data.shape[0] - 1                            #
    bcolmn = 'B'                                                #
    b = 0                                                       # Letter
    ccolmn = 'C'                                                # Variables
    c = 0                                                       #
    dcolmn = 'D'                                                #
    d = 0                                                       #
    ecolmn = 'E'                                                #
    e = 0                                                       #
    x = data_shape_2 + 1                                        #
    form_a = 1                                                  #
    form_b = 1                                                  #

    global dd, ee                                               # Internal calculations for sum

    while a < data_shape_2:
        vertical = ('A' + str(a + 2))
        bb = (bcolmn + str(b + 2))
        cc = (ccolmn + str(c + 2))
        dd = (dcolmn + str(d + 2))
        ee = (ecolmn + str(e + 2))

        worksheet.write(bb, data.iat[a, 0], write_format)       #
        worksheet.write(cc, data.iat[a, 1], write_format)       #
        form_c = float((data.iat[a, 0]) * (data.iat[form_a, 1]))    # Fill cells with
        form_d = float((data.iat[form_b, 0]) * (data.iat[a, 1]))    # .txt digital value
        worksheet.write(dd, form_c, write_format_for_formula)   #
        worksheet.write(ee, form_d, write_format_for_formula)   #

        a += 1                                                  #
        b += 1                                                  #
        d += 1                                                  #
        c += 1                                                  # Cells
        x -= 1                                                  # Counter
        e += 1                                                  #
        form_a += 1                                             #
        form_b += 1                                             #

        worksheet.write(vertical, a, write_format_hat)          # Number of row

    worksheet.write('A' + str(data_shape + 1), 'Amount', write_format_square)                      # Amount value
    worksheet.write('D' + str(data_shape + 1), ('=SUM(D2:' + str(dd) + ')'), write_format_sum)     # Formula value
    worksheet.write('E' + str(data_shape + 1), ('=SUM(E2:' + str(ee) + ')'), write_format_sum)     # Formula value
    worksheet.write('A' + str(data_shape + 2), 'S (Ha)', write_format_square)                      # Hectare label
    worksheet.write('B' + str(data_shape + 2), '=' + 'ABS' + '(' + '(' +
                    ((dcolmn + str(data_shape + 1) + '-' + ecolmn + str(data_shape + 1)) +       # Square formula value
                     ')' + '*0.5/10000' + ')'), write_format_square)
    workbook.close()


class area_calculate(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_area_calculate()
        self.ui.setupUi(self)

        self.ui.pushButton_3.clicked.connect(self.instruction_2)
        self.ui.pushButton_5.clicked.connect(self.file_selection)
        self.ui.pushButton_4.clicked.connect(self.save_file_area)

    def file_selection(self):
        global file_name
        self.label_status_calm()
        file_name = QFileDialog.getOpenFileName(self, "File selection", "Your file", "text (*.txt)")[0]
        if not file_name:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select a .txt file!')
        else:
            self.path_label()
            self.ui.pushButton_4.setDisabled(False)
        return file_name

    def save_file_area(self):
        global output_file_2
        output_file_2 = False
        output_file_2 = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "Your file", "*.xlsx")[0]
        if not output_file_2:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select the name and path of the file!')
        else:
            make_xlsx_square()
            self.finish_label()
            self.ui.pushButton_4.setDisabled(True)

    def instruction_2(self):
        QtWidgets.QMessageBox.about(self, 'Instruction', ''' 
    Area calculate
 
1. The necessary lines, areas and points - must be
            Projection:
            Gauss Krueger (6 degree zones)
            Zone:
            Which you need
            Datum:
            Which you need, for ex. (S-42 (PULKOVO 1942))
            Planar Units:
            METERS
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
7. Click the button "Calculate area"
8. Select the name and path of the file (.xlsx)
9. Click "Save file"
    ''')

    def path_label(self):
        self.ui.label_4.setText(file_name)

    def label_status_calm(self):
        self.ui.label_4.setText('Status')

    def finish_label(self):
        self.ui.label_4.setText('Finish')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = area_calculate()
    myapp.show()
    sys.exit(app.exec_())
