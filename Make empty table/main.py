# If you need - you can replace English to Russian use comments in source
# При необходимости вы можете заменить английский язык на русский в соответствии с комментариями

import sys
import xlsxwriter
from window import *

global number_of_cells, output_file


def empty_xlsx():

    global number_of_cells

    def number_of_rows():
        return let + str(dig)

    height = 1
    dig = 3  # Digit
    let = 'A'  # Letter
    z = 1  # Counter

    workbook = xlsxwriter.Workbook(output_file)  # Name of xlsx file/ Название файла
    worksheet = workbook.add_worksheet('Сoordinates')  # Name of xlsx worksheet/ Название листа

    merge_format = workbook.add_format({
        'bold': 0,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    worksheet.merge_range('A1:A2', '№№', merge_format)
    worksheet.merge_range('B1:D1', 'North Latitude', merge_format)  # 'Северная Широта'
    worksheet.merge_range('E1:G1', 'East Longitude', merge_format)  # 'Восточная Долгота'

    write_format = workbook.add_format({
        'bold': 0,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    worksheet.write('B2', 'Degrees', write_format)  # 'Градусы'
    worksheet.write('C2', 'Minutes', write_format)  # 'Минуты'
    worksheet.write('D2', 'Seconds', write_format)  # 'Секунды'
    worksheet.write('E2', 'Degrees', write_format)  # 'Градусы'
    worksheet.write('F2', 'Minutes', write_format)  # 'Минуты'
    worksheet.write('G2', 'Seconds', write_format)  # 'Секунды'

    while height <= number_of_cells:
        table = number_of_rows()
        worksheet.write(table, int(z), write_format)
        worksheet.write('B' + str(dig), None, write_format)
        worksheet.write('C' + str(dig), None, write_format)
        worksheet.write('D' + str(dig), None, write_format)
        worksheet.write('E' + str(dig), None, write_format)
        worksheet.write('F' + str(dig), None, write_format)
        worksheet.write('G' + str(dig), None, write_format)
        height += 1
        dig += 1
        z += 1

    workbook.close()


class empty_table(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Empty_table()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.instruction)
        self.ui.pushButton.clicked.connect(self.cells_creator)

    def label_status_calm(self):
        self.ui.label_3.setText('Status')

    def label_status_finish(self):
        self.ui.label_3.setText('Success')

    def cells_creator(self):
        global number_of_cells, output_file
        number_of_cells = self.ui.spinBox.value()
        output_file = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "Your file", "*.xlsx")[0]
        if not output_file:
            self.label_status_calm()
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select the name and path of the file!')
        else:
            empty_xlsx()
            self.label_status_finish()

    def instruction(self):
        QtWidgets.QMessageBox.about(self, 'Instruction', ''' 
    Create empty table
    
    1. Input number of rows
    2. Click on the button "Create empty table"
    3. Select the name and path of the file (.xlsx)
    4. Click on the button "Save"
    ''')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = empty_table()
    myapp.show()
    sys.exit(app.exec_())







