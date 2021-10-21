from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_reverse_export_xy(object):
    def setupUi(self, reverse_export_xy):
        reverse_export_xy.setObjectName("Form")
        reverse_export_xy.resize(400, 140)
        reverse_export_xy.setMinimumSize(QtCore.QSize(400, 140))
        reverse_export_xy.setMaximumSize(QtCore.QSize(400, 140))
        self.label_9 = QtWidgets.QLabel(reverse_export_xy)
        self.label_9.setGeometry(QtCore.QRect(10, 100, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.pushButton_9 = QtWidgets.QPushButton(reverse_export_xy)
        self.pushButton_9.setGeometry(QtCore.QRect(204, 90, 181, 25))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_10 = QtWidgets.QLabel(reverse_export_xy)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayoutWidget = QtWidgets.QWidget(reverse_export_xy)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 39, 381, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.pushButton_10.setDisabled(True)

        self.retranslateUi(reverse_export_xy)
        QtCore.QMetaObject.connectSlotsByName(reverse_export_xy)

    def retranslateUi(self, reverse_export_xy):
        _translate = QtCore.QCoreApplication.translate
        reverse_export_xy.setWindowTitle(_translate("Form", "Reverse Export XY"))
        self.label_9.setText(_translate("Form", "Reverse Export XY"))
        self.pushButton_9.setText(_translate("Form", "Instruction"))
        self.label_10.setText(_translate("Form", "Status"))
        self.pushButton_11.setText(_translate("Form", "Select file"))
        self.pushButton_10.setText(_translate("Form", "Export"))
