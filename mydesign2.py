# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'disigned2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
import numpy as np
import neurallink


class Ui_Neiralink(object):
    def setupUi(self, Neiralink):
        Neiralink.setObjectName("Neiralink")
        Neiralink.resize(464, 346)
        Neiralink.setWindowOpacity(4.0)
        Neiralink.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button = QtWidgets.QPushButton(Neiralink)
        self.button.setGeometry(QtCore.QRect(300, 240, 141, 41))
        self.button.setDefault(True)
        self.button.setObjectName("button")
        self.button.clicked.connect(self.buttonClickedgo)
        self.rost = QtWidgets.QTextEdit(Neiralink)
        self.rost.setGeometry(QtCore.QRect(10, 130, 221, 31))
        self.rost.setObjectName("rost")
        self.ves = QtWidgets.QTextEdit(Neiralink)
        self.ves.setGeometry(QtCore.QRect(10, 200, 221, 31))
        self.ves.setObjectName("ves")
        self.label = QtWidgets.QLabel(Neiralink)
        self.label.setGeometry(QtCore.QRect(10, 100, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Neiralink)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Neiralink)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Neiralink)
        self.label_4.setGeometry(QtCore.QRect(120, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.labell = QtWidgets.QLabel(Neiralink)
        self.labell.setGeometry(QtCore.QRect(20, 270, 241, 41))
        self.labell.setText("")
        self.labell.setObjectName("labell")
        self.labell.setFont(font)
        self.labell.setText("Подождите. Сеть тренируется")
        self.brefresh = QtWidgets.QPushButton(Neiralink)
        self.brefresh.setGeometry(QtCore.QRect(300, 290, 141, 41))
        self.brefresh.setObjectName("brefresh")
        self.brefresh.clicked.connect(self.buttonClickedrefresh)

        self.retranslateUi(Neiralink)
        QtCore.QMetaObject.connectSlotsByName(Neiralink)

        data = np.array([
            [17, -1],    # Alice
            [5, -10],     # Bob
            [2, 5],     # Charlie
            [6, 3], # Diana
            [0, -2],
            [18, 11],
            [13, 7],
            [-13, -8],
        ])
 
        all_y_trues = np.array([
            0, # Alice
            0, # Bob
            1, # Charlie
            0,
            1,
            0,
            0,
            1# Diana
        ])

        self.network = neurallink.OurNeuralNetwork()
        self.network.train(data, all_y_trues)
        self.labell.setText("Сеть натренирована")
        

    def retranslateUi(self, Neiralink):
        _translate = QtCore.QCoreApplication.translate
        Neiralink.setWindowTitle(_translate("Neiralink", "NEIRALINK"))
        self.button.setText(_translate("Neiralink", "Узнать"))
        self.label.setText(_translate("Neiralink", "Введите рост ниже (см)"))
        self.label_2.setText(_translate("Neiralink", "Теперь введите вес (кг)"))
        self.label_3.setText(_translate("Neiralink", "Теперь можно узнать пол человека"))
        self.label_4.setText(_translate("Neiralink", "по его росту и весу:"))
        self.brefresh.setText(_translate("Neiralink", "Очистить вывод"))

    def buttonClickedgo(self):
        trost = self.rost.toPlainText()
        tves = self.ves.toPlainText()

        if trost.isdigit() and tves.isdigit():

            rost = float(trost)
            ves = float(tves)

            rost -= 165
            ves -= 62

            rez = self.network.feedforward(np.array([rost,ves]))
            ch = 0.5-rez

            self.labell.setText("")
            if ch<0:
                self.labell.setText("Женский пол")
            elif ch>0:
                self.labell.setText("Мужской пол")
            else:
                self.labell.setText("Нельзя определить")
        else:
            self.labell.setText("Данные некорректны")

    def buttonClickedrefresh(self):
        self.labell.setText("")
