# -*- coding: utf-8 -*-
 
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc

 
class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(507, 224)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.horizontalLayout_username = QtWidgets.QHBoxLayout()
        self.horizontalLayout_username.setObjectName("horizontalLayout_username")
        self.lbl_username = QtWidgets.QLabel(Form)
        self.lbl_username.setObjectName("lbl_username")
        self.horizontalLayout_username.addWidget(self.lbl_username)
        self.lineEditUsername = QtWidgets.QLineEdit(Form)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.horizontalLayout_username.addWidget(self.lineEditUsername)
        self.verticalLayout.addLayout(self.horizontalLayout_username)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditEmail = QtWidgets.QLineEdit(Form)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.horizontalLayout.addWidget(self.lineEditEmail)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditPassword = QtWidgets.QLineEdit(Form)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.horizontalLayout_2.addWidget(self.lineEditPassword)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40,
        QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.insert_data)
        self.verticalLayout.addWidget(self.pushButton)
        self.labelResult = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.verticalLayout.addWidget(self.labelResult)
 
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
  
    def insert_data(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="pyqt5"
            )
 
            mycursor = mydb.cursor()
            
            username = self.lineEditUsername.text()
            email = self.lineEditEmail.text()
            password = self.lineEditPassword.text()
 
            query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            value = (username, email, password)
 
            mycursor.execute(query, value)
 
            mydb.commit()
            self.labelResult.setText("Registro Guardado con Exito!")
 
        except mc.Error as e:
            self.labelResult.setText("Error al insertar la informacion")
 
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_username.setText(_translate("Form", "Username:"))
        self.label.setText(_translate("Form", "Email:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.pushButton.setText(_translate("Form", "Guardar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
