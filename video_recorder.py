from PyQt5.QtCore import QThread
import cv2
import os
import time
from datetime import datetime

class VideoRecorderWorker(QThread):
    def __init__(self, get_frame_callback, save_dir=None, filename_prefix="mission"):
        super().__init__()
        self.get_frame_callback = get_frame_callback
        self.recording = True
        
        # Set a default save directory if none is provided
        if save_dir is None:
            self.save_dir = os.path.expanduser("~/Desktop/diplomatikh/drone-disease-monitor/DroneRecordings")
        else:
            self.save_dir = os.path.expanduser(save_dir)

        os.makedirs(self.save_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename_prefix}_{timestamp}.avi"
        self.output_path = os.path.join(self.save_dir, filename)
        self.video_writer = None

        print(f"Videos will be saved to: {self.save_dir}")  # Debug: Print the exact save path

    def run(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        time.sleep(0.1)  # small delay for frame readiness

        while self.recording:
            frame = self.get_frame_callback()
            if frame is not None:
                height, width = frame.shape[:2]
                if self.video_writer is None:
                    self.video_writer = cv2.VideoWriter(
                        self.output_path, fourcc, 30.0, (width, height)
                    )
                    print(f"Video recording started: {self.output_path}")  # Debug: Video started

                self.video_writer.write(frame)

            self.msleep(33)  # approx 30 FPS

        if self.video_writer:
            self.video_writer.release()
            self.video_writer = None
            print(f"Video saved successfully at: {self.output_path}")  # Debug: Video saved message

    def stop_recording(self):
        self.recording = False
