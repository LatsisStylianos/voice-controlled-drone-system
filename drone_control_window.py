from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import difflib
from PyQt5.QtGui import QPixmap, QImage
import socket
import urllib.request
import random
import threading
import time
import cv2
from djitellopy import Tello
import atexit
from PyQt5.QtCore import QThread, pyqtSignal
from math import cos, radians
import json
from .select_field_window import SelectFieldWindow
from PyQt5.QtCore import QTimer
import os
from gui.video_recorder import VideoRecorderWorker



# Auto-generated UI class (do not edit this manually)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 600)
        MainWindow.setStyleSheet("/* Main Window or Dialog Background */\n"
"QWidget {\n"
"    background-color: #333333; /* Dark grey background */\n"
"    color: yellow; /* Yellow text */\n"
"    font-family: Arial, sans-serif; /* Font style */\n"
"    font-size: 14px; /* Font size */\n"
"}\n"
"\n"
"/* Labels (Username, Password) */\n"
"QLabel {\n"
"    color: yellow; /* Yellow text */\n"
"    font-size: 16px; /* Larger font size for labels */\n"
"    font-weight: bold; /* Bold text */\n"
"}\n"
"\n"
"/* Specific Label (label_4) */\n"
"QLabel#label_4 {\n"
"    color: #555555; /* Yellow text */\n"
"    padding: 5px; /* Padding inside the label */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Line Edits (Input Fields) */\n"
"QLineEdit {\n"
"    background-color: #444444; /* Darker grey background */\n"
"    color: yellow; /* Yellow text */\n"
"    border: 1px solid yellow; /* Yellow border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px; /* Padding inside the input field */\n"
"    font-size: 14px; /* Font size */\n"
"}\n"
"\n"
"/* Push Buttons (Login, Register) */\n"
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
"/* Push Button Hover Effect */\n"
"QPushButton:hover {\n"
"    background-color: #cccc00; /* Darker yellow on hover */\n"
"    border: 1px solid #cccc00; /* Darker yellow border on hover */\n"
"}\n"
"\n"
"/* Push Button Pressed Effect */\n"
"QPushButton:pressed {\n"
"    background-color: #999900; /* Even darker yellow when pressed */\n"
"    border: 1px solid #999900; /* Even darker yellow border when pressed */\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wifi_label = QtWidgets.QLabel(self.centralwidget)
        self.wifi_label.setObjectName("wifi_label")
        self.horizontalLayout.addWidget(self.wifi_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        
        # Add connection status label
        self.connection_label = QtWidgets.QLabel(self.centralwidget)
        self.connection_label.setObjectName("connection_label")
        self.horizontalLayout.addWidget(self.connection_label)
        
        self.battery_label = QtWidgets.QLabel(self.centralwidget)
        self.battery_label.setObjectName("battery_label")
        self.horizontalLayout.addWidget(self.battery_label)
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setObjectName("settings_button")
        self.horizontalLayout.addWidget(self.settings_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        # Replace static image with video label
        self.video_label = QtWidgets.QLabel(self.centralwidget)
        self.video_label.setText("Waiting for drone video...")
        self.video_label.setAlignment(QtCore.Qt.AlignCenter)
        self.video_label.setStyleSheet("background-color: black; color: white;")
        self.video_label.setScaledContents(True)
        self.video_label.setObjectName("video_label")
        self.video_label.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addWidget(self.video_label)

        # Add status message label below video
        self.status_message_label = QtWidgets.QLabel(self.centralwidget)
        self.status_message_label.setText("Ready")
        self.status_message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_message_label.setStyleSheet("""
            color: yellow;
            font-size: 16px;
            padding: 2px;
            margin: 0;
            background-color: #222222;
            border-top: 1px solid #444444;
            qproperty-alignment: AlignCenter;
        """)
        self.status_message_label.setFixedHeight(28)
        self.status_message_label.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed
        )
        self.status_message_label.setObjectName("status_message_label")
        self.verticalLayout.addWidget(self.status_message_label)
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.land_takeoff_button = QtWidgets.QPushButton(self.centralwidget)
        self.land_takeoff_button.setObjectName("land_takeoff_button")
        self.horizontalLayout_3.addWidget(self.land_takeoff_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.flight_time_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.flight_time_label_2.setObjectName("flight_time_label_2")
        self.horizontalLayout_3.addWidget(self.flight_time_label_2)
        self.speed_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.speed_label_2.setObjectName("speed_label_2")
        self.horizontalLayout_3.addWidget(self.speed_label_2)
        self.height_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.height_label_2.setObjectName("height_label_2")
        self.horizontalLayout_3.addWidget(self.height_label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.microphone_button = QtWidgets.QPushButton(self.centralwidget)
        self.microphone_button.setObjectName("microphone_button")
        self.horizontalLayout_3.addWidget(self.microphone_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.wifi_label.setText(_translate("MainWindow", "Wi-Fi not connected"))
        self.connection_label.setText(_translate("MainWindow", "Drone: --"))  # Added
        self.battery_label.setText(_translate("MainWindow", "Battery: --"))  # Changed
        self.settings_button.setText(_translate("MainWindow", "Settings"))
        self.land_takeoff_button.setText(_translate("MainWindow", "Take Off"))
        self.flight_time_label_2.setText(_translate("MainWindow", "Flight Time: 00"))
        self.speed_label_2.setText(_translate("MainWindow", "Speed: 0"))
        self.height_label_2.setText(_translate("MainWindow", "Height: 0"))
        self.microphone_button.setText(_translate("MainWindow", "🎤"))

class SettingsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setFixedSize(300, 250)
        
        layout = QtWidgets.QVBoxLayout()
        
        # Information labels (read-only)
        info_style = "QLabel { color: yellow; font-size: 14px; }"
        
        # Height information
        self.height_label = QtWidgets.QLabel("Height: 0 meters")
        self.height_label.setStyleSheet(info_style)
        layout.addWidget(self.height_label)
        
        # Time information
        self.time_label = QtWidgets.QLabel("Time: 0 seconds")
        self.time_label.setStyleSheet(info_style)
        layout.addWidget(self.time_label)
        
        # Speed information
        self.speed_label = QtWidgets.QLabel("Speed: 0 m/s")
        self.speed_label.setStyleSheet(info_style)
        layout.addWidget(self.speed_label)
        
        # Language information
        self.language_label = QtWidgets.QLabel("Language: English")
        self.language_label.setStyleSheet(info_style)
        layout.addWidget(self.language_label)
        
        # Low battery warning combo box (changed from slider)
        battery_layout = QtWidgets.QHBoxLayout()
        battery_layout.addWidget(QtWidgets.QLabel("Low Battery Warning:"))
        self.battery_combo = QtWidgets.QComboBox()
        self.battery_combo.addItems(["5%", "10%", "15%", "20%"])
        self.battery_combo.setCurrentIndex(1)  # Default to 10%
        battery_layout.addWidget(self.battery_combo)
        layout.addLayout(battery_layout)
        
        # Photo quality option
        quality_layout = QtWidgets.QHBoxLayout()
        quality_layout.addWidget(QtWidgets.QLabel("Photo Quality:"))
        self.quality_combo = QtWidgets.QComboBox()
        self.quality_combo.addItems(["Normal", "High"])
        quality_layout.addWidget(self.quality_combo)
        layout.addLayout(quality_layout)
        
        # Close button
        self.close_button = QtWidgets.QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)
        
        self.setLayout(layout)
        atexit.register(self.cleanup_drone)

# Custom class that uses the generated UI
class DroneControlWindow(QtWidgets.QMainWindow):
    def __init__(self, file_path=None, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Drone Control")

        self.selected_field_path = file_path
        if file_path:
            self.load_field_data(file_path)  # Load field data if provided.
        else:
            print("No file path provided at initialization.")
        
        # Initialize drone connection
        self.drone = Tello()
        self.drone_connected = False
        self.is_flying = False
        self.flight_start_time = 0
        self.current_height = 0
        self.current_speed = 0
        self.wifi_connected = False
        self.video_thread = None
        self.video_running = False

        # Register cleanup function to ensure proper shutdown
        atexit.register(self.cleanup_drone)

        # Connect buttons to functions
        self.ui.land_takeoff_button.clicked.connect(self.toggle_land_takeoff)
        self.ui.microphone_button.clicked.connect(self.verbal_instructions)
        self.ui.settings_button.clicked.connect(self.show_settings)
        
        # Set up timers
        self.check_internet_connection()
        self.connection_timer = QtCore.QTimer(self)
        self.connection_timer.timeout.connect(self.check_internet_connection)
        self.connection_timer.start(5000)
        
        self.drone_connection_timer = QtCore.QTimer(self)
        self.drone_connection_timer.timeout.connect(self.check_drone_connection)
        self.drone_connection_timer.start(3000)

        # Timers for inactivity
        self.keep_alive_timer = QTimer(self)
        self.keep_alive_timer.timeout.connect(self.send_keep_alive)
        self.keep_alive_timer.start(5000)  # every 5 seconds
        
        # Timer to update drone metrics
        self.metrics_timer = QtCore.QTimer(self)
        self.metrics_timer.timeout.connect(self.update_drone_metrics)
        self.metrics_timer.start(1000)
        
        # Start video thread
        self.start_video_stream()

    
    def start_video_stream(self):
        """Start the video stream and update it using a QTimer"""
        if not self.video_running and self.drone_connected:
            try:
                self.video_running = True
                self.video_timer = QtCore.QTimer(self)
                self.video_timer.timeout.connect(self.update_video)
                self.video_timer.start(33)  # ~30 FPS (1000ms / 30)
            except Exception as e:
                print(f"Error starting video stream: {e}")
                self.video_running = False

    def update_video(self):
        """Update the video feed from the drone without freezing"""
        if self.drone_connected:
            try:
                frame = self.drone.get_frame_read().frame  # Get the frame **once**
                if frame is not None and frame.size != 0:
                    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgb_image.shape
                    bytes_per_line = ch * w
                    qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(qt_image)

                    # Update video label (always on UI thread)
                    self.ui.video_label.setPixmap(pixmap.scaled(
                        self.ui.video_label.size(),
                        QtCore.Qt.KeepAspectRatio,
                        QtCore.Qt.SmoothTransformation
                    ))
            except Exception as e:
                print(f"Error updating video: {e}")


    def show_settings(self):
        settings_dialog = SettingsDialog(self)
        
        # Update the information labels with current values
        settings_dialog.height_label.setText(f"Height: {self.current_height} meters")
        settings_dialog.time_label.setText(f"Time: {self.get_flight_time()} seconds")
        settings_dialog.speed_label.setText(f"Speed: {self.current_speed} m/s")
        
        settings_dialog.exec_()

    def get_flight_time(self):
        """Calculate current flight time in seconds"""
        if self.is_flying:
            return int(time.time() - self.flight_start_time)
        return 0

    def update_drone_metrics(self):
        """Update drone metrics with real data"""
        if self.drone_connected:
            try:
                # Get real metrics from drone
                self.current_height = self.drone.get_height()
                self.current_speed = max(
                    abs(self.drone.get_speed_x()),
                    abs(self.drone.get_speed_y()),
                    abs(self.drone.get_speed_z())
                )
                
                # Update UI
                self.ui.height_label_2.setText(f"Height: {self.current_height}cm")
                self.ui.speed_label_2.setText(f"Speed: {self.current_speed}cm/s")
                
                # Update flight time if flying
                if self.is_flying:
                    flight_seconds = self.get_flight_time()
                    minutes = flight_seconds // 60
                    seconds = flight_seconds % 60
                    self.ui.flight_time_label_2.setText(f"Flight Time: {minutes}:{seconds:02d}")
                
            except Exception as e:
                print(f"Error getting drone metrics: {e}")

    def check_drone_connection(self):
        """Check actual drone connection status"""
        try:
            # Try to connect if not already connected
            if not self.drone_connected:
                self.drone.connect()
                self.drone_connected = True
                self.drone.streamon()
                self.ui.connection_label.setText("Drone: Connected")
                self.ui.connection_label.setStyleSheet("color: lightgreen;")
                
                # Get battery status
                battery_level = self.drone.get_battery()
                self.ui.battery_label.setText(f"Battery: {battery_level}%")
                self.ui.battery_label.setStyleSheet("color: yellow;")
                
                # Start video stream if not already running
                if not self.video_running:
                    self.start_video_stream()
                
        except Exception as e:
            print(f"Drone connection error: {e}")
            self.drone_connected = False
            self.ui.connection_label.setText("Drone: Disconnected")
            self.ui.connection_label.setStyleSheet("color: red;")
            self.ui.battery_label.setText("Battery: --")
            self.ui.battery_label.setStyleSheet("color: grey;")
            
            # Reset metrics when disconnected
            self.reset_metrics()

    def check_internet_connection(self, host="8.8.8.8", port=53, timeout=3):
        """Check internet connection and update wifi_label accordingly"""
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            self.wifi_connected = True
            self.ui.wifi_label.setText("Wi-Fi: Connected")
            self.ui.wifi_label.setStyleSheet("color: lightgreen;")
            return True
        except Exception:
            try:
                urllib.request.urlopen('http://google.com', timeout=timeout)
                self.wifi_connected = True
                self.ui.wifi_label.setText("Wi-Fi: Connected")
                self.ui.wifi_label.setStyleSheet("color: lightgreen;")
                return True
            except Exception:
                self.wifi_connected = False
                self.ui.wifi_label.setText("Wi-Fi: Not Connected")
                self.ui.wifi_label.setStyleSheet("color: red;")
                if self.drone_connected:  # Only reset if we were connected
                    self.reset_metrics()
                return False
            
    def update_status_message(self, message):
        """Update the status message displayed below the video feed"""
        self.ui.status_message_label.setText(message)
        QtCore.QCoreApplication.processEvents()
    
    def reset_metrics(self):
        """Reset all drone metrics to zero"""
        self.current_height = 0
        self.current_speed = 0
        self.ui.height_label_2.setText("Height: 0cm")
        self.ui.speed_label_2.setText("Speed: 0cm/s")
        self.ui.flight_time_label_2.setText("Flight Time: 0:00")

    def send_keep_alive(self):
        if self.drone.is_flying:
            try:
                self.drone.send_control_command('command')
            except Exception as e:
                print(f"Keep-alive failed: {e}")

    def toggle_land_takeoff(self):
        """Take off to 50 cm or land based on the current drone state."""
        if not self.drone_connected:
            self.update_status_message("Drone not connected")
            print("Drone not connected.")
            return

        try:
            if not self.is_flying:
                self.update_status_message("Taking off...")
                print("Taking off to 50 cm...")
                retries = 4
                while retries > 0:
                    try:
                        self.drone.takeoff()
                        time.sleep(3)
                        self.current_height = 50
                        self.flight_start_time = time.time()  # <-- Add this
                        self.is_flying = True
                        self.ui.land_takeoff_button.setText("Land")
                        print("Drone is in the air at 50 cm.")
                        self.update_drone_metrics()
                        break
                    except Exception as e:
                        print(f"Error during takeoff attempt {5 - retries}: {e}")
                        retries -= 1
                        time.sleep(2)
                        if retries == 0:
                            print("Failed to take off after multiple attempts.")
            else:
                self.update_status_message("Landing...")
                print("Landing...")
                retries = 3
                while retries > 0:
                    try:
                        self.drone.land()
                        time.sleep(3)
                        self.current_height = 0  # Reset height
                        self.is_flying = False
                        self.flight_start_time = 0  # Reset flight timer after landing
                        self.ui.land_takeoff_button.setText("Take Off")
                        print("Drone has landed.")
                        self.update_drone_metrics()
                        break
                    except Exception as e:
                        print(f"Error during landing attempt {4 - retries}: {e}")
                        retries -= 1
                        time.sleep(2)
                        if retries == 0:
                            print("Failed to land after multiple attempts.")
        except Exception as e:
            print(f"Error in takeoff/landing: {e}")


    def verbal_instructions(self):
        self.ui.microphone_button.setEnabled(False)
        
        if hasattr(self, 'voice_worker') and self.voice_worker.isRunning():
            self.voice_worker.terminate()  # If an old worker is still running, force it to stop.

        self.voice_worker = VoiceCommandWorker(self)
        self.voice_worker.selected_field_path = self.selected_field_path
        self.voice_worker.command_completed.connect(self.on_voice_command_completed)
        self.voice_worker.start()

    def on_voice_command_completed(self):
        self.ui.microphone_button.setEnabled(True)

    def cleanup_drone(self):
        """Safely shut down the drone connection if still active."""
        if hasattr(self, 'keep_alive_timer'):
          self.keep_alive_timer.stop()
        if not self.drone_connected:
            print("Drone already disconnected. Skipping cleanup.")
            return
        if self.drone_connected:
            try:
                if self.is_flying:
                    print("Attempting to land before exit...")
                    try:
                        self.drone.land()
                        time.sleep(3)  # Allow landing to complete
                    except Exception as land_error:
                        print(f"Landing attempt failed: {land_error}")
                        # Emergency stop if landing fails
                        self.drone.emergency()
                    finally:
                        self.is_flying = False
                
                print("Turning off video stream...")
                try:
                    self.drone.streamoff()
                except Exception as stream_error:
                    print(f"Error turning off stream: {stream_error}")
                
                print("Closing drone connection...")
                try:
                    self.drone.end()
                except Exception as end_error:
                    print(f"Error ending connection: {end_error}")
                finally:
                    self.drone_connected = False
                
                print("Cleanup completed.")
            except Exception as e:
                print(f"Error during cleanup: {e}")

    def __del__(self):
        try:
            self.cleanup_drone()
        except Exception as e:
            print(f"Destructor cleanup error: {e}")

    def load_field_data(self, path):
        """Loads the selected field data."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                self.field_data = json.load(f)
            print("Field data loaded successfully!")
            self.extract_positions()  # Correct after update
        except Exception as e:
            print(f"Error loading field data: {e}")


    def extract_positions(self):
        starting_position = None
        vine_coordinates = []

        for feature in self.field_data["features"]:
            if feature["properties"].get("starting_position", False):
                starting_position = feature["geometry"]["coordinates"]
            if feature["geometry"]["type"] == "Point":
                vine_coordinates.append(feature["geometry"]["coordinates"])

        self.starting_position = starting_position
        self.vine_coordinates = vine_coordinates



    #Converts a GPS coordinate (longitude, latitude) to a relative (x, y) position in metersusing the starting point as the origin.
    def gps_to_relative(self, start, point):
        lat_scale = 111000  # Approximate meters per degree latitude.
        lon_scale = 111000 * cos(radians(start["lat"]))
        
        dx = (point["lon"] - start["lon"]) * lon_scale
        dy = (point["lat"] - start["lat"]) * lat_scale
        return {"x": dx, "y": dy}

    #Moves the drone from the current relative coordinate to the target.The method calculates differences in x and y and uses move_right/left and move_forward/back.
    def move_to_position(self, current, target):
        dx = target['x'] - current['x']
        dy = target['y'] - current['y']

        total_distance = (dx**2 + dy**2)**0.5
        max_step = 4.5  # Tello SDK max is 5m, stay slightly under

        steps = int(total_distance // max_step) + 1
        for i in range(1, steps + 1):
            ratio = i / steps
            intermediate_x = current['x'] + dx * ratio
            intermediate_y = current['y'] + dy * ratio

            rel_dx = intermediate_x - current['x']
            rel_dy = intermediate_y - current['y']

            # Convert to centimeters
            x_cm = int(rel_dx * 100)
            y_cm = int(rel_dy * 100)
            z = 0  # relative Z is 0 to maintain height
            speed = 20

            # Skip if there's no movement needed
            if x_cm == 0 and y_cm == 0 and z == 0:
                print("[DEBUG] No movement needed (zero distance). Skipping command.")
                continue

            command = f"go {x_cm} {y_cm} {z} {speed}"
            print(f"[DEBUG] Sending command: {command}")
            self.drone.send_command_with_return(command)

            current['x'] = intermediate_x
            current['y'] = intermediate_y

            time.sleep(2)

    
    # Step 1: Open the window to select field
    # Somewhere inside DroneControlWindow class:
    def open_select_field_window(self):
        print("[DEBUG] Opening select field window.")  # Debugging
        select_field_window = SelectFieldWindow(self)
        select_field_window.field_selected.connect(self.set_selected_field_path)  # connect to self!
        select_field_window.exec_()  # Open the select window



    # Step 2: Handle the field selection from the SelectFieldWindow
    def handle_field_selected(self, selected_field_path):
        self.selected_field = selected_field_path
        self.selected_field_path = selected_field_path
        print(f"[DEBUG] Selected field path stored: {self.selected_field}")

    # Step 3: Set the selected field and load the data
    def set_selected_field_path(self, path):
        print("Setting selected field path:", path)
        self.selected_field_path = path
        self.voice_worker.selected_field_path = path
        self.load_field_data(path)

    #created for video_recorder
    def get_drone_frame(self):
        """Helper to fetch a single frame from the drone."""
        return self.drone.get_frame_read().frame

    def start_mission_recording(self, prefix):
        if hasattr(self, 'recorder_thread') and self.recorder_thread and self.recorder_thread.isRunning():
            self.recorder_thread.stop_recording()
            self.recorder_thread.wait()
        self.recorder_thread = VideoRecorderWorker(get_frame_callback=self.get_drone_frame, filename_prefix=prefix)
        self.recorder_thread.start()

    def stop_mission_recording(self):
        if hasattr(self, 'recorder_thread') and self.recorder_thread:
            self.recorder_thread.stop_recording()
            self.recorder_thread.wait()

    def scan_field(self):
        file_path = self.selected_field_path
        print(f"[DEBUG] selected_field_path: {file_path}")

        if not file_path:
            print("No field file selected. Please select a field first.")
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception as e:
            print(f"Error loading field file: {e}")
            return

        features = data.get("features", [])
        vines = []
        self.starting_position = None

        for feature in features:
            geometry = feature.get("geometry", {})
            properties = feature.get("properties", {})

            if geometry.get("type") == "Point":
                coords = geometry.get("coordinates", [])
                if len(coords) != 2:
                    print(f"Invalid coordinates: {coords}")
                    continue

                if properties.get("starting_position", False):
                    self.starting_position = coords
                else:
                    vines.append(coords)

        if not self.starting_position:
            print("Starting position not found in the field file.")
            return

        if not vines:
            print("No vines found in the field file.")
            return

        print(f"Starting at: {self.starting_position}")
        self.current_position = self.starting_position
        print(f"Found {len(vines)} vines. Beginning sequential scan...")

        self.start_mission_recording("scan_field")  # ← START RECORDING

        try:
            self.move_drone_to_vine(self.starting_position)

            for vine_coords in vines:
                self.move_drone_to_vine(vine_coords)

            self.move_drone_to_vine(self.starting_position)
            print("Scan complete. Drone returned to starting position.")
        finally:
            self.stop_mission_recording()  # ← STOP RECORDING




    def inspect_vine(self, vine_name):
        print(f"[DEBUG] Attempting to inspect: {vine_name}")

        file_path = self.selected_field_path
        if not file_path:
            print("No field file selected.")
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception as e:
            print(f"Error loading field file: {e}")
            return

        target_coords = None
        for feature in data.get("features", []):
            props = feature.get("properties", {})
            name = next(iter(props.keys()), "").lower()
            if name == vine_name.lower():
                target_coords = feature.get("geometry", {}).get("coordinates")
                break

        if target_coords:
            self.start_mission_recording(f"inspect_{vine_name.replace(' ', '_')}")  # ← START RECORDING

            try:
                self.move_drone_to_vine(self.starting_position)
                self.move_drone_to_vine(target_coords)
                self.move_drone_to_vine(self.starting_position)
                print(f"{vine_name} inspection complete.")
            finally:
                self.stop_mission_recording()  # ← STOP RECORDING
        else:
            print(f"{vine_name} not found in the field.")



    def move_drone_to_vine(self, gps_coords):
        """Move the drone to the target GPS position."""

        # Ensure current_position is initialized
        if not hasattr(self, 'current_position') or not self.current_position or len(self.current_position) < 2:
            print("[WARN] current_position not set. Initializing to starting_position.")
            self.current_position = self.starting_position

        # Validate gps_coords
        if not gps_coords or len(gps_coords) < 2:
            print("[ERROR] Invalid target GPS coordinates.")
            return

        print(f"[DEBUG] Moving drone from {self.current_position} to {gps_coords}")

        try:
            # Convert GPS to relative coordinates
            start = {"lat": self.starting_position[1], "lon": self.starting_position[0]}
            target_point = {"lat": gps_coords[1], "lon": gps_coords[0]}
            current_point = {"lat": self.current_position[1], "lon": self.current_position[0]}

            target_relative = self.gps_to_relative(start, target_point)
            current_relative = self.gps_to_relative(start, current_point)

            # Move drone and update GPS position, not relative
            self.move_to_position(current_relative, target_relative)
            self.current_position = gps_coords  # keep it in GPS format

            time.sleep(3)  # Optional wait at each vine

        except Exception as e:
            print(f"[ERROR] Failed to move drone to vine: {e}")



    def move_up(self, distance=30):
        print(f"DEBUG: connected={self.drone_connected}, flying={self.is_flying}")
        if not (self.drone_connected and self.is_flying):
            print("Drone is not connected or not flying.")
            return

        try:
            print(f"Attempting to move up {distance}cm...")
            self.drone.send_control_command(f"up {distance}")
            print(f"Move up {distance}cm command sent.")
        except Exception as e:
            print(f"Error moving up: {e}")

    def move_down(self, distance=30):
        print(f"DEBUG: connected={self.drone_connected}, flying={self.is_flying}")
        if not (self.drone_connected and self.is_flying):
            print("Drone is not connected or not flying.")
            return

        try:
            print(f"Attempting to move down {distance}cm...")
            self.drone.send_control_command(f"down {distance}")
            print(f"Move down {distance}cm command sent.")
        except Exception as e:
            print(f"Error moving down: {e}")



class VoiceCommandWorker(QThread):
    command_completed = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.selected_field_path = None  # Initialize selected field path to None

    def run(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.parent.update_status_message("Listening for command...")
            print("Listening for command...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=20)
                command = recognizer.recognize_google(audio).lower().strip()
                self.parent.update_status_message(f"Command: {command}")
                print(f"Recognized voice input: '{command}'")
            except sr.WaitTimeoutError:
                self.parent.update_status_message("Voice recognition timed out")
                print("Voice recognition timed out.")
                self.command_completed.emit()
                return
            except sr.UnknownValueError:
                self.parent.update_status_message("Did not understand audio")
                print("Could not understand the audio.")
                self.command_completed.emit()
                return
            except sr.RequestError as e:
                self.parent.update_status_message("Voice service error")
                print(f"Could not request results from service; {e}")
                self.command_completed.emit()
                return

        # Map spoken numbers to their numeric counterparts
        number_map = {
            "one": "1", "two": "2", "three": "3", "four": "4", "for": "4", "five": "5",
            "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
            "eleven": "11", "twelve": "12", "thirteen": "13", "fourteen": "14", "fifteen": "15",
            "sixteen": "16", "seventeen": "17", "eighteen": "18", "nineteen": "19", "twenty": "20"
        }
        for word, num in number_map.items():
            command = command.replace(word, num)

        expected_commands = ["scan field", "inspect field"] + [f"inspect vine {i}" for i in range(1, 21)] + [
            "take off", "land", "landing", "up", "down", "go up", "go down", "move up", "move down", "rise", "descend"
        ]


        # Handle movement commands
        if command in ["up", "go up", "move up", "rise"]:
            self.parent.update_status_message("Moving up 30cm...")
            self.parent.move_up()
            self.parent.update_status_message("Upward movement complete")
        elif command in ["down", "go down", "move down", "descend"]:
            self.parent.update_status_message("Moving down 30cm...")
            self.parent.move_down()
            self.parent.update_status_message("Downward movement complete")
        elif command in ["land", "landing"]:
            self.parent.update_status_message("Initiating landing...")
            self.parent.toggle_land_takeoff()
        elif command == "take off":
            self.parent.update_status_message("Preparing for takeoff...")
            self.parent.toggle_land_takeoff()
        else:
            best_match = difflib.get_close_matches(command, expected_commands, n=1, cutoff=0.6)
            if best_match:
                matched_command = best_match[0]
                print(f"Matched Command: {matched_command}")

                if matched_command in ["scan field", "inspect field"]:
                    if self.selected_field_path:
                        self.parent.update_status_message("Beginning field scan...")
                        self.parent.scan_field()
                        self.parent.update_status_message("Field scan completed")
                    else:
                        self.parent.update_status_message("No field selected - cannot scan")
                        print("No field file selected. Please select a field first.")
                elif matched_command.startswith("inspect vine"):
                    vine_number = matched_command.split()[-1]
                    self.parent.update_status_message(f"Preparing to inspect vine {vine_number}...")
                    self.parent.inspect_vine(f"vine {vine_number}")
                    self.parent.update_status_message(f"Inspection of vine {vine_number} completed")
                elif matched_command in ["take off", "land", "landing"]:
                    self.parent.update_status_message(f"Preparing to {matched_command}...")
                    self.parent.toggle_land_takeoff()
            else:
                self.parent.update_status_message("Command not recognized")
                print("Command not recognized.")

        if self.parent.is_flying:
            self.parent.update_status_message("Ready - Drone airborne")
        else:
            self.parent.update_status_message("Ready - Drone on standby")
    
        self.command_completed.emit()



# Example usage (for testing)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = DroneControlWindow("Field 1")  # Pass the field name
    window.show()
    sys.exit(app.exec_())