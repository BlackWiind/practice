# -*- coding: utf-8 -*-
#Шестиричный калькулятор


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.second_number: str = None
        self.first_number: str = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(328, 493)
        MainWindow.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(0, 10, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.result_label.setFont(font)
        self.result_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.result_label.setText("")
        self.result_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.result_label.setObjectName("result_label")
        self.calc_label = QtWidgets.QLabel(self.centralwidget)
        self.calc_label.setGeometry(QtCore.QRect(0, 90, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.calc_label.setFont(font)
        self.calc_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.calc_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.calc_label.setObjectName("calc_label")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 210, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(229, 201, 62);")
        self.btn_1.setObjectName("btn_1")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(250, 280, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(229, 201, 62);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(90, 280, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(229, 201, 62);")
        self.btn_5.setObjectName("btn_5")
        self.btn_sum = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sum.setGeometry(QtCore.QRect(250, 210, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sum.setFont(font)
        self.btn_sum.setStyleSheet("background-color: rgb(229, 201, 62);")
        self.btn_sum.setObjectName("btn_sum")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(10, 280, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(229, 201, 62);")
        self.btn_4.setObjectName("btn_4")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(170, 210, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(229, 201, 62);")
        self.btn_3.setObjectName("btn_3")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(90, 210, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(229, 201, 62);")
        self.btn_2.setObjectName("btn_2")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(170, 280, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(229, 201, 62);")
        self.btn_0.setObjectName("btn_0")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(250, 420, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(229, 201, 62);")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_eqv = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eqv.setGeometry(QtCore.QRect(10, 400, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_eqv.setFont(font)
        self.btn_eqv.setStyleSheet("background-color: rgb(255, 55, 37);")
        self.btn_eqv.setObjectName("btn_eqv")
        self.btn_to_ten = QtWidgets.QPushButton(self.centralwidget)
        self.btn_to_ten.setGeometry(QtCore.QRect(250, 350, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_to_ten.setFont(font)
        self.btn_to_ten.setStyleSheet("background-color: rgb(229, 201, 62);")
        self.btn_to_ten.setObjectName("btn_to_ten")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_press()

    def calculation(self, firs_number: str
                    , second_number: str
                    , operation) -> str:

        if operation == '+':
            num = int(firs_number, 6) + int(second_number, 6)
        else:
            num = int(firs_number, 6) - int(second_number, 6)
        return self.to_six(num)

    def button_press(self):
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_sum.clicked.connect(lambda: self.plus_minus(self.btn_sum.text()))
        self.btn_minus.clicked.connect(lambda: self.plus_minus(self.btn_minus.text()))

        self.btn_eqv.clicked.connect(self.equal)
        self.btn_to_ten.clicked.connect(lambda:
                                        self.result_label.setText(self.to_decimal(self.calc_label.text())),
                                        )
        self.btn_clear.clicked.connect(lambda: self.calc_label.setText('0'))

    def write_number(self, number):
        if self.calc_label.text() == '0':
            self.calc_label.setText(number)
        else:
            self.calc_label.setText(self.calc_label.text() + number)

    def plus_minus(self, d):
        if self.result_label.text() != '':
            self.first_number = self.result_label.text()
        elif self.calc_label.text() != '0':
            self.first_number = self.calc_label.text()
            self.result_label.setText(self.calc_label.text())
        self.calc_label.setText(d)

    def to_six(self, numder: int) -> str:
        answer = ''
        if numder == 0:
            return '0'
        if numder > 0:
            while numder > 0:
                answer = str(numder % 6) + answer
                numder //= 6
            return answer
        else:
            numder = abs(numder)
            while numder > 0:
                answer = str(numder % 6) + answer
                numder //= 6
            return '-' + answer

    def equal(self):
        if self.calc_label.text() != "0":
            self.second_number = self.calc_label.text()[1:]
            operation = self.calc_label.text()[0]
            try:
                self.result_label.setText(self.calculation(self.first_number,
                                                           self.second_number,
                                                           operation))
            except:
                self.calc_label.setText('0')
            self.calc_label.setText('0')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calc_label.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_sum.setText(_translate("MainWindow", "+"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_eqv.setText(_translate("MainWindow", "="))
        self.btn_to_ten.setText(_translate("MainWindow", "в х10"))

    def to_decimal(self, number: str) -> str:
        self.calc_label.setText('0')
        try:
            return str(int(number, 6))
        except:
            return '0'


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
