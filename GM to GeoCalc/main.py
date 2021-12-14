import pandas as pd
from window import *


def for_dms():
    counter = 1
    replacements = {'°':'', ' N':';', ' E':';', '\'':'', '\"':''}

    with open('1.txt') as input_file, open('3.txt', 'w') as output_file:
        for line in input_file:
            for src, target in replacements.items():
                line = line.replace(src, target)
            output_file.write( '{}{} {}'.format(counter,';', line))
            counter += 1 
    
    data = pd.read_csv('3.txt', encoding='cp1251', header=None, sep=r"\s+", names=None)
    data = data[[0,4,5,6,1,2,3]]

    data.to_csv('3.txt', header=None, index=None, sep=' ', mode='w')

def for_xy():
    counter = 1
    replacements = {'\n':';\n','\t':';\t'}

    with open('4.txt') as input_file, open('5.txt', 'w') as output_file:
        for line in input_file:
            for src, target in replacements.items():
                line = line.replace(src, target)
            output_file.write( '{}{} {}'.format(counter,';', line))
            counter += 1
            
    data = pd.read_csv('5.txt', encoding='cp1251', header=None, sep=r"\s+", names=None)
    data = data[[0,2,1]]
    data.to_csv('3.txt', header=None, index=None, sep=' ', mode='w')


class gm_to_geocalc(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_gm_to_geocalc()
        self.ui.setupUi(self)

        self.ui.pushButton_3.clicked.connect(self.instruction)
        
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = gm_to_geocalc()
    myapp.show()
    sys.exit(app.exec_())