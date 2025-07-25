# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/create_field_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateFieldDialog(object):
    def setupUi(self, CreateFieldDialog):
        CreateFieldDialog.setObjectName("CreateFieldDialog")
        CreateFieldDialog.resize(794, 732)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateFieldDialog.sizePolicy().hasHeightForWidth())
        CreateFieldDialog.setSizePolicy(sizePolicy)
        CreateFieldDialog.setStyleSheet("/* Main Window Background */\n"
        "QWidget {\n"
        "    background-color: #333333; /* Dark grey background */\n"
        "    color: yellow; /* Yellow text */\n"
        "    font-family: Arial, sans-serif; /* Font style */\n"
        "    font-size: 14px; /* Font size */\n"
        "}\n"
        "\n"
        "/* Labels */\n"
        "QLabel {\n"
        "    color: yellow; /* Yellow text */\n"
        "    font-size: 16px; /* Larger font size for labels */\n"
        "    font-weight: bold; /* Bold text */\n"
        "}\n"
        "\n"
        "/* Buttons */\n"
        "QPushButton {\n"
        "    background-color: yellow; /* Yellow background */\n"
        "    color: black; /* Black text */\n"
        "    border: 1px solid yellow; /* Yellow border */\n"
        "    border-radius: 5px; /* Rounded corners */\n"
        "    padding: 10px; /* Padding inside the button */\n"
        "    font-size: 14px; /* Font size */\n"
        "    font-weight: bold; /* Bold text */\n"
        "}\n"
        "\n"
        "/* Button Hover Effect */\n"
        "QPushButton:hover {\n"
        "    background-color: #cccc00; /* Darker yellow on hover */\n"
        "    border: 1px solid #cccc00; /* Darker yellow border on hover */\n"
        "}\n"
        "\n"
        "/* Button Pressed Effect */\n"
        "QPushButton:pressed {\n"
        "    background-color: #999900; /* Even darker yellow when pressed */\n"
        "    border: 1px solid #999900; /* Even darker yellow border when pressed */\n"
        "}")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(CreateFieldDialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(CreateFieldDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.upload_button = QtWidgets.QPushButton(CreateFieldDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_button.sizePolicy().hasHeightForWidth())
        self.upload_button.setSizePolicy(sizePolicy)
        self.upload_button.setMinimumSize(QtCore.QSize(200, 0))
        self.upload_button.setObjectName("upload_button")
        self.verticalLayout.addWidget(self.upload_button)
        self.file_path_label = QtWidgets.QLabel(CreateFieldDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_path_label.sizePolicy().hasHeightForWidth())
        self.file_path_label.setSizePolicy(sizePolicy)
        self.file_path_label.setObjectName("file_path_label")
        self.verticalLayout.addWidget(self.file_path_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scan_button = QtWidgets.QPushButton(CreateFieldDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_button.sizePolicy().hasHeightForWidth())
        self.scan_button.setSizePolicy(sizePolicy)
        self.scan_button.setObjectName("scan_button")
        self.verticalLayout.addWidget(self.scan_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.return_button = QtWidgets.QPushButton(CreateFieldDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_button.sizePolicy().hasHeightForWidth())
        self.return_button.setSizePolicy(sizePolicy)
        self.return_button.setObjectName("return_button")
        self.verticalLayout.addWidget(self.return_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        
        # Fixing size and aspect ratio of the images
        self.label_3 = QtWidgets.QLabel(CreateFieldDialog)
        self.label_3.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.label_3.setMaximumWidth(600)  # Constrain max width
        self.label_3.setMaximumHeight(400)  # Constrain max height
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setPixmap(QtGui.QPixmap("gui\\../resources/Screenshot (168).png"))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)

        self.label_2 = QtWidgets.QLabel(CreateFieldDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        
        # Fixing size and aspect ratio for the second image
        self.label_4 = QtWidgets.QLabel(CreateFieldDialog)
        self.label_4.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.label_4.setMaximumWidth(600)  # Constrain max width
        self.label_4.setMaximumHeight(400)  # Constrain max height
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setPixmap(QtGui.QPixmap("gui\\../resources/Screenshot (169).png"))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QtWidgets.QLabel(CreateFieldDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(CreateFieldDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateFieldDialog)

        # Connect the return_button to close the dialog
        self.return_button.clicked.connect(CreateFieldDialog.close)



    def retranslateUi(self, CreateFieldDialog):
        _translate = QtCore.QCoreApplication.translate
        CreateFieldDialog.setWindowTitle(_translate("CreateFieldDialog", "Create Field Dialog"))
        self.label.setText(_translate("CreateFieldDialog", "Create a New Field"))
        self.upload_button.setText(_translate("CreateFieldDialog", "Upload JSON File"))
        self.file_path_label.setText(_translate("CreateFieldDialog", "No file selected"))
        self.scan_button.setText(_translate("CreateFieldDialog", "Initial Field Scan"))
        self.return_button.setText(_translate("CreateFieldDialog", "Return"))

    def upload_file(self):
        # Open file dialog to upload the file
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_path:
            self.file_path_label.setText(file_path)  # Set the file path to the label

    def on_scan_clicked(self):
        # Get the file path from the label
        file_path = self.file_path_label.text()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateFieldDialog = QtWidgets.QDialog()
    ui = Ui_CreateFieldDialog()
    ui.setupUi(CreateFieldDialog)
    CreateFieldDialog.show()
    sys.exit(app.exec_())