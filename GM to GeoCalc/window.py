from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys


class Ui_gm_to_geocalc(object):
    def setupUi(self, gm_to_geocalc):
        gm_to_geocalc.setObjectName("gm_to_geocalc")
        gm_to_geocalc.resize(440, 200)
        gm_to_geocalc.setMinimumSize(QtCore.QSize(440, 200))
        gm_to_geocalc.setMaximumSize(QtCore.QSize(440, 200))
        self.pushButton = QtWidgets.QPushButton(gm_to_geocalc)
        self.pushButton.setGeometry(QtCore.QRect(30, 65, 158, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(gm_to_geocalc)
        self.label.setGeometry(QtCore.QRect(0, 10, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(gm_to_geocalc)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 158, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(gm_to_geocalc)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(250, 60, 160, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.setDisabled(True)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_4.setDisabled(True)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(gm_to_geocalc)
        QtCore.QMetaObject.connectSlotsByName(gm_to_geocalc)

    def retranslateUi(self, gm_to_geocalc):
        _translate = QtCore.QCoreApplication.translate
        gm_to_geocalc.setWindowTitle(_translate("gm_to_geocalc", "GM to GeoCalc"))
        self.pushButton.setText(_translate("gm_to_geocalc", "Select file"))
        self.label.setText(_translate("gm_to_geocalc", "Path"))
        self.label_2.setText(_translate("gm_to_geocalc", "GM to GeoCalc"))
        self.pushButton_2.setText(_translate("gm_to_geocalc", "Convert to DMS"))
        self.pushButton_4.setText(_translate("gm_to_geocalc", "Convert to XY"))
        self.pushButton_3.setText(_translate("gm_to_geocalc", "Instruction"))
