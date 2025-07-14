import os
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

class SelectFieldWindow(QtWidgets.QDialog):
    field_selected = pyqtSignal(str)  # Only one definition

    def __init__(self, parent=None):
        super().__init__(parent)
        self.field_mappings = {}  # Store mappings here
        self.setupUi()
        self.loadFields()

    def setupUi(self):
        self.setObjectName("SelectFieldWindow")
        self.resize(419, 305)
        self.setMinimumSize(QtCore.QSize(400, 300))
        self.setStyleSheet("""
            QWidget { background-color: #333333; color: yellow; font-family: Arial; font-size: 14px; }
            QLabel { color: yellow; font-size: 16px; font-weight: bold; }
            QPushButton { background-color: yellow; color: black; border-radius: 5px; padding: 10px; font-size: 14px; font-weight: bold; }
            QPushButton:hover { background-color: #cccc00; }
            QPushButton:pressed { background-color: #999900; }
        """)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        
        self.title_label = QtWidgets.QLabel("Select an Existing Field", self)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.title_label)

        self.field_list = QtWidgets.QListWidget(self)
        self.verticalLayout.addWidget(self.field_list)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        
        self.open_field_button = QtWidgets.QPushButton("Open Selected", self)
        self.open_field_button.clicked.connect(self.openSelectedField)
        self.horizontalLayout.addWidget(self.open_field_button)

        self.cancel_button = QtWidgets.QPushButton("Cancel", self)
        self.cancel_button.clicked.connect(self.close)
        self.horizontalLayout.addWidget(self.cancel_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

    def loadFields(self):
        """Loads field mappings and displays both the user-defined field name and file name."""
        mapping_file = r"C:\Users\Stelios\desktop\diplomatikh\drone-disease-monitor\field_mappings.json"

        self.field_list.clear()

        try:
            if os.path.exists(mapping_file):
                with open(mapping_file, "r") as file:
                    self.field_mappings = json.load(file)  # Store mappings
                print("Loaded field mappings:", self.field_mappings)
            else:
                self.field_mappings = {}
                print("No field mappings file found.")

            for field_name, file_path in self.field_mappings.items():
                file_name = os.path.basename(file_path)
                self.field_list.addItem(f"{field_name} - {file_name}")

            print(f"List count: {self.field_list.count()}")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Failed to load field mappings: {e}")

    def openSelectedField(self):
        """Handles opening the selected field file."""
        selected_item = self.field_list.currentItem()
        if selected_item:
            selected_text = selected_item.text()
            field_name = selected_text.split(" - ")[0]

            file_path = self.field_mappings.get(field_name)
            if file_path and os.path.exists(file_path):
                print(f"Opened field: {field_name}")
                self.field_selected.emit(file_path)
                self.accept()
            else:
                QtWidgets.QMessageBox.warning(self, "Warning", "Field path is invalid or doesn't exist.")
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a field first.")
