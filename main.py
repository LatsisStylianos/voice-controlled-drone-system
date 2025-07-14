import sys
import os
import json
import shutil
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from gui.login_window import Ui_LoginWindow
from gui.main_window import Ui_MainWindow
from gui.create_field_dialog import Ui_CreateFieldDialog
from gui.select_field_window import SelectFieldWindow  # Importing only the SelectFieldWindow class
from gui.drone_control_window import DroneControlWindow  # Import the new DroneControlWindow
from database import create_database, register_user, login_user


# Login Window (as QDialog)
class LoginWindow(QtWidgets.QDialog, Ui_LoginWindow):  
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.connect_signals()  
        create_database()

        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

        # Load and set logo image
        self.load_login_image()

    def load_login_image(self):
        """Loads and sets the login window logo."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        resources_dir = os.path.join(base_dir, "resources")
        image_path = os.path.join(resources_dir, "tello.png")

        # Debugging output
        print("Login image path:", image_path)

        if os.path.exists(image_path):
            pixmap = QtGui.QPixmap(image_path)
            if pixmap.isNull():
                print("Failed to load the image.")
            else:
                print("Image loaded successfully!")
                self.logo_label.setPixmap(pixmap)
                self.logo_label.setScaledContents(True)  # Scale the image
        else:
            print("Image does not exist!")

    def connect_signals(self):
        self.login_button.clicked.connect(self.on_login_clicked)
        self.register_button.clicked.connect(self.on_register_clicked)

    def on_login_clicked(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if login_user(username, password):
            self.close()
            self.main_window = MainWindow()
            self.main_window.show()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def on_register_clicked(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if register_user(username, password):
            QtWidgets.QMessageBox.information(self, "Registration Successful", "You have successfully registered!")
        else:
            QtWidgets.QMessageBox.warning(self, "Registration Failed", "Username already exists.")


# Main Window
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.connect_signals()  
        self.configure_image_label()  

    def connect_signals(self):
        self.create_field_button.clicked.connect(self.on_create_field_clicked)
        self.select_field_button.clicked.connect(self.on_select_field_clicked)

    def configure_image_label(self):
        """Configures the image label."""
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setScaledContents(True)
        self.image_label.setMinimumSize(300, 300)

    def on_create_field_clicked(self):
        self.create_field_dialog = CreateFieldDialog()
        self.create_field_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.create_field_dialog.exec_()

    def on_select_field_clicked(self):
        """Opens the Select Field Window."""
        self.select_field_window = SelectFieldWindow()
        self.select_field_window.field_selected.connect(self.on_field_selected)  # Connect the signal
        self.select_field_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.select_field_window.exec_()

    def on_field_selected(self, field_path):
        """Opens the Drone Control Window when a field is selected."""
        # Here you pass the full field path, not just the field name
        self.drone_control_window = DroneControlWindow(field_path)  # Pass the full path
        self.drone_control_window.show()


# Create Field Dialog (as QDialog)
class CreateFieldDialog(QtWidgets.QDialog, Ui_CreateFieldDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  

        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowMaximizeButtonHint)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.field_data = None  

        self.connect_signals()
        self.load_images()

    def connect_signals(self):
        self.upload_button.clicked.connect(self.on_upload_clicked)
        self.scan_button.clicked.connect(self.on_scan_clicked)

    def load_images(self):
        """Loads and sets images in the create field dialog."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        resources_dir = os.path.join(base_dir, "resources")

        image_paths = [
            ("Screenshot (168).png", self.label_3),
            ("Screenshot (169).png", self.label_4),
        ]

        for image_name, label in image_paths:
            image_path = os.path.join(resources_dir, image_name)
            print(f"Loading image: {image_path}")

            if os.path.exists(image_path):
                pixmap = QtGui.QPixmap(image_path)
                if pixmap.isNull():
                    print(f"Error: Failed to load {image_name}")
                else:
                    print(f"Loaded {image_name} successfully!")
                    label.setPixmap(pixmap)
                    label.setScaledContents(True)
            else:
                print(f"Error: Image not found - {image_path}")

    def on_upload_clicked(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Upload JSON/GeoJSON File", "", "JSON Files (*.json *.geojson)")

        if file_path:
            field_name, ok = QtWidgets.QInputDialog.getText(self, "Field Name", "Enter a name for this field:")
            if not ok or not field_name.strip():
                QtWidgets.QMessageBox.warning(self, "Error", "You must enter a valid field name.")
                return

            field_name = field_name.strip()
            
            # Define the destination folder where files will be saved
            base_dir = os.path.dirname(os.path.abspath(__file__))
            fields_dir = os.path.join(base_dir, "fields")
            
            if not os.path.exists(fields_dir):
                os.makedirs(fields_dir)
            
            new_file_path = os.path.join(fields_dir, os.path.basename(file_path))
            
            try:
                if os.path.exists(new_file_path):
                    QtWidgets.QMessageBox.warning(self, "Warning", "This file already exists in the fields folder.")
                else:
                    shutil.copy(file_path, new_file_path)
                    self.save_field_mapping(field_name, new_file_path)  # Save the field name mapping
                    self.load_json(new_file_path)  # Load the file
                    self.file_path_label.setText(f"{new_file_path}")  # Display file path under button
                    QtWidgets.QMessageBox.information(self, "Success", "File uploaded and linked successfully!")
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Error", f"Failed to upload file: {e}")

    def save_field_mapping(self, field_name, file_path):
        """Save the mapping of field names to file paths."""
        mapping_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "field_mappings.json")

        try:
            # Check if the file exists and read or initialize an empty dictionary
            if os.path.exists(mapping_file) and os.path.getsize(mapping_file) > 0:
                with open(mapping_file, "r") as file:
                    field_mappings = json.load(file)
            else:
                field_mappings = {}

            # Add new field mapping
            field_mappings[field_name] = file_path

            # Write the updated mappings to the file
            with open(mapping_file, "w") as file:
                json.dump(field_mappings, file, indent=4)

            print(f"Field mapping for '{field_name}' saved successfully!")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Failed to save field mapping: {e}")


    def load_json(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.field_data = json.load(file)

            if "starting_positions" in self.field_data:
                self.start_position_combo.clear()
                self.start_position_combo.addItems(self.field_data["starting_positions"])
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Failed to load file: {e}")

    def on_scan_clicked(self):
        file_path = self.file_path_label.text()

        if file_path == "No file selected" or not file_path:
            QtWidgets.QMessageBox.warning(self, "Error", "Please upload a valid JSON file first.")
            return

        if not self.field_data:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to load the field data.")
            return

        # Create and show the scanning dialog
        self.scan_dialog = QtWidgets.QMessageBox(self)  # Store as instance variable
        self.scan_dialog.setWindowTitle("Scanning")
        self.scan_dialog.setText("Scanning...")
        self.scan_dialog.setStandardButtons(QtWidgets.QMessageBox.NoButton)
        self.scan_dialog.setModal(True)
        
        # Create and configure the timer (store as instance variable)
        self.scan_timer = QtCore.QTimer()
        self.scan_timer.setSingleShot(True)
        self.scan_timer.timeout.connect(self.scan_dialog.accept)  # Use accept() to properly close
        
        # Start the timer before showing the dialog
        self.scan_timer.start(5000)  # 5 seconds
        
        # Show the dialog - this will block until closed
        self.scan_dialog.exec_()
        
        # After dialog closes, clean up
        self.scan_timer.stop()
        del self.scan_timer
        del self.scan_dialog
        
        # Proceed with the scanning logic
        field_name = os.path.basename(file_path)
        print(f"Field Name: {field_name}")
        print("Initiating initial field scan...")
        
        # Your scanning logic goes here


# Run the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())