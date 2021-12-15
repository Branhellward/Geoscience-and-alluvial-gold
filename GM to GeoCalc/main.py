import pandas as pd
from window import *


global file_name, output_file


def for_dms():
    global file_name, output_file
    counter = 1
    replacements = {'°':'', ' N':';', ' E':';', '\'':'', '\"':''}

    with open(file_name) as input_file, open(output_file, 'w') as output:
        for line in input_file:
            for src, target in replacements.items():
                line = line.replace(src, target)
            output.write( '{}{} {}'.format(counter,';', line))
            counter += 1 
    
    data = pd.read_csv(output_file, encoding='cp1251', header=None, sep=r"\s+", names=None)
    data = data[[0,4,5,6,1,2,3]]

    data.to_csv(output_file, header=None, index=None, sep=' ', mode='w')

def for_xy():
    global file_name, output_file
    counter = 1
    replacements = {'\n':';\n','\t':';\t'}

    with open(file_name) as input_file, open(output_file, 'w') as output:
        for line in input_file:
            for src, target in replacements.items():
                line = line.replace(src, target)
            output.write( '{}{} {}'.format(counter,';', line))
            counter += 1
            
    data = pd.read_csv(output_file, encoding='cp1251', header=None, sep=r"\s+", names=None)
    data = data[[0,2,1]]
    data.to_csv(output_file, header=None, index=None, sep=' ', mode='w')


class gm_to_geocalc(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_gm_to_geocalc()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.file_selection)
        self.ui.pushButton_2.clicked.connect(self.save_file_dms)
        self.ui.pushButton_3.clicked.connect(self.instruction)
        self.ui.pushButton_4.clicked.connect(self.save_file_xy)
        
    def file_selection(self):
        global file_name
        self.label_status_calm()
        file_name = QFileDialog.getOpenFileName(self, "File selection", "Your file", "text (*.txt)")[0]
        if not file_name:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select a .txt file!')
        else:
            self.path_label()
            self.ui.pushButton_4.setDisabled(False)
            self.ui.pushButton_2.setDisabled(False)
        return file_name
    
    def save_file_dms(self):
        global output_file
        output_file = False
        output_file = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "Your file", "*.txt")[0]
        if not output_file:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select the name and path of the file!')
        else:
            for_dms()
            self.finish_label()
            self.ui.pushButton_4.setDisabled(True)
            self.ui.pushButton_2.setDisabled(True)
            
    def save_file_xy(self):
        global output_file
        output_file = False
        output_file = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "Your file", "*.txt")[0]
        if not output_file:
            QtWidgets.QMessageBox.about(self, 'Warning', 'Need to select the name and path of the file!')
        else:
            for_xy()
            self.finish_label()
            self.ui.pushButton_4.setDisabled(True)
            self.ui.pushButton_2.setDisabled(True)
        
    def instruction(self):
            QtWidgets.QMessageBox.about(self, 'Instruction', ''' 
        Gm to GeoCalc
    
    1. Select the area you need
    2. Export object:
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
    7. Click the button "Convert to DME or XY"
    8. Select the name and path of the file (.txt)
    9. Click "Save file"
        ''')

    def path_label(self):
        self.ui.label.setText(file_name)

    def label_status_calm(self):
        self.ui.label.setText('Path')

    def finish_label(self):
        self.ui.label.setText('Finish')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = gm_to_geocalc()
    myapp.show()
    sys.exit(app.exec_())