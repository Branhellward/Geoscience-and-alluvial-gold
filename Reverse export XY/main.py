import openpyxl
import sys
from window import*

global file_name_4, reverse_export_file_xy

def export_ingine():
    global file_name_4
    book = openpyxl.open(file_name_4, read_only=True)   # Xlsx file
    sheet = book.active
    reverse_export_file = open(reverse_export_file_xy, 'w')    # Open xlsx for read

    for row in range(2,sheet.max_row+1):    # Read all rows and add char to txt
        coord_line=str(sheet[row][1].value)+'\t'+str(
            sheet[row][2].value)+'\n'

        reverse_export_file.write(coord_line)   
    reverse_export_file.close()

class reverse_export_xy(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_reverse_export_xy()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.open_file_xlsx)
        self.ui.pushButton_10.clicked.connect(self.save_file_area)
        self.ui.pushButton_9.clicked.connect(self.instruction_4)


    def open_file_xlsx(self):
            global file_name_4
            self.label_status_calm()
            file_name_4 = QFileDialog.getOpenFileName(self, "File selection", "Your file", "table (*.xlsx);;table (*.xls)")[0]    # Выбор файла с таблицей
            if not file_name_4:
                QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select a table file!')    # Предупреждение, отсутствие выбранного файла
            else:
                self.label_path_4()
                self.ui.pushButton_10.setDisabled(False)
            return file_name_4

    def save_file_area(self):
        global reverse_export_file_xy
        reverse_export_file_xy = False
        reverse_export_file_xy = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "Your file", "*.txt")[0]    # Сохранение файла
        if not reverse_export_file_xy:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select the name and path of the file!')   # Предупреждение, отсутствие пути сохранения
        else:
            export_ingine()
            self.finish_label()
            self.ui.pushButton_10.setDisabled(True)

    def instruction_4(self):
        QtWidgets.QMessageBox.about(self, 'Instruction', '''
    Reverse Export
 
1. Select a .xlsx/.xls file with coordinates
2. Click the button "Export"
3. Select the name and path of the file (.txt)
4. Open it use GM program
5. Select projection You need

    ''')

    def label_path_4(self):
            self.ui.label_10.setText(file_name_4)

    def label_status_calm(self):
        self.ui.label_10.setText('Status')

    def finish_label(self):
        self.ui.label_10.setText('Finish')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = reverse_export_xy()
    myapp.show()
    sys.exit(app.exec_())