import sys
import cv2
import threading
import time
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import pyqtSignal, QObject
from djitellopy import Tello

class VideoThread(QObject):
    change_pixmap = pyqtSignal(QImage)
    error_occurred = pyqtSignal(str)

    def __init__(self, tello):
        super().__init__()
        self.tello = tello
        self._run_flag = True

    def run(self):
        frame_reader = self.tello.get_frame_read()
        while self._run_flag:
            try:
                frame = frame_reader.frame
                if frame is None or frame.size == 0:
                    time.sleep(0.1)
                    continue
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (640, 480))
                qimg = QImage(frame.data, frame.shape[1], frame.shape[0], 3 * frame.shape[1], QImage.Format.Format_RGB888)
                self.change_pixmap.emit(qimg)
                time.sleep(0.03)
            except Exception as e:
                self.error_occurred.emit(f"Video stream error: {str(e)}")
                time.sleep(1)

    def stop(self):
        self._run_flag = False

class TelloApp(QWidget):
    error_occurred = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.tello = None
        self.video_thread = None
        self.worker = None
        self.is_flying = False

        try:
            self.tello = Tello()
            self.tello.connect()
            self.tello.command_timeout = 15  # Increased timeout for 90° rotation
            self.tello.streamon()
            time.sleep(2)
            
            battery = self.tello.get_battery()
            if battery < 30:
                QMessageBox.warning(self, "Low Battery", f"Battery level is low ({battery}%). Please charge.")
            
        except Exception as e:
            QMessageBox.critical(self, "Connection Error", f"Failed to connect to Tello: {str(e)}")
            self.tello = None

        self.initUI()
        if self.tello:
            self.start_video()
        
        self.error_occurred.connect(self.show_error)

    def initUI(self):
        self.setWindowTitle("Tello Drone Controller")
        self.setGeometry(100, 100, 800, 600)

        self.video_label = QLabel(self)
        self.video_label.setFixedSize(640, 480)
        self.video_label.setText("No video feed available" if self.tello is None else "Loading video...")

        self.start_button = QPushButton("Execute Flight Plan (40cmx2 + 90°)", self)
        self.start_button.clicked.connect(self.execute_flight_plan)
        self.start_button.setEnabled(self.tello is not None)

        self.land_button = QPushButton("Emergency Land", self)
        self.land_button.clicked.connect(self.emergency_land)
        self.land_button.setEnabled(self.tello is not None)

        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.land_button)
        self.setLayout(layout)

    def start_video(self):
        self.worker = VideoThread(self.tello)
        self.worker.change_pixmap.connect(self.set_image)
        self.worker.error_occurred.connect(self.show_error)

        self.video_thread = threading.Thread(target=self.worker.run, daemon=True)
        self.video_thread.start()

    def set_image(self, image):
        try:
            self.video_label.setPixmap(QPixmap.fromImage(image))
        except Exception as e:
            print(f"Error setting image: {e}")

    def show_error(self, error_msg):
        QMessageBox.warning(self, "Error", error_msg)

    def execute_flight_plan(self):
        if self.tello and not self.is_flying:
            try:
                flight_thread = threading.Thread(target=self._execute_flight_sequence, daemon=True)
                flight_thread.start()
            except Exception as e:
                QMessageBox.warning(self, "Command Error", f"Failed to start flight thread: {str(e)}")

    def _execute_flight_sequence(self):
        """Execute the complete flight sequence with 40cm movements and 90° turn"""
        try:
            self.is_flying = True
            self.start_button.setEnabled(False)
            
            # Ensure video stream is active
            self.tello.streamon()
            time.sleep(1)
            
            # 1. Takeoff to 70cm
            self._safe_takeoff(70)
            time.sleep(2)  # Stabilize
            
            # 2. Move forward 40cm
            self._safe_move("forward", 40)
            time.sleep(1)  # Pause
            
            # 3. Rotate right 90° in one motion
            self._safe_rotate(90)
            time.sleep(1)  # Pause
            
            # 4. Move forward another 40cm
            self._safe_move("forward", 40)
            time.sleep(1)  # Pause
            
            # 5. Land
            self._safe_land()
            
        except Exception as e:
            self.error_occurred.emit(f"Flight error: {str(e)}")
            try:
                self.tello.land()
            except:
                pass
        finally:
            self.is_flying = False
            self.start_button.setEnabled(True)

    def _safe_takeoff(self, height_cm):
        """Takeoff to specific height"""
        try:
            self.tello.send_control_command(f"height {height_cm}")
            time.sleep(1)
            self.tello.takeoff()
            time.sleep(3)  # Reach height and stabilize
        except Exception as e:
            raise Exception(f"Takeoff failed: {str(e)}")

    def _safe_move(self, direction, distance_cm):
        """Move in specified direction"""
        try:
            if direction == "forward":
                self.tello.move_forward(distance_cm)
            elif direction == "back":
                self.tello.move_back(distance_cm)
            time.sleep(0.5)  # Short pause
        except Exception as e:
            raise Exception(f"Movement failed: {str(e)}")

    def _safe_rotate(self, degrees):
        """Rotate specified degrees in one motion"""
        try:
            self.tello.rotate_clockwise(degrees)
            time.sleep(2)  # Extra time for complete rotation
        except Exception as e:
            raise Exception(f"Rotation failed: {str(e)}")

    def _safe_land(self):
        """Land safely"""
        try:
            self.tello.land()
            time.sleep(3)  # Wait for landing
        except Exception as e:
            raise Exception(f"Landing failed: {str(e)}")

    def emergency_land(self):
        """Immediate landing"""
        if self.tello:
            try:
                self.tello.emergency()
                self.is_flying = False
            except Exception as e:
                QMessageBox.warning(self, "Emergency Land Error", f"Failed to emergency land: {str(e)}")

    def closeEvent(self, event):
        if self.worker:
            self.worker.stop()
        if self.video_thread:
            self.video_thread.join(timeout=1)
        if self.tello:
            try:
                if self.is_flying:
                    self.tello.land()
                self.tello.streamoff()
                self.tello.end()
            except Exception as e:
                print(f"Error during cleanup: {e}")
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelloApp()
    window.show()
    sys.exit(app.exec())