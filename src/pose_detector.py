from ultralytics import YOLO
class PoseDetector:
    def __init__(self):
        self.model = YOLO("yolov8n-pose.pt") # Load pretrained pose estimator

    def detect_pose(self, frame):
        results = self.model(frame, imgsz=320, verbose=False)  # Run pose estimation on the frame
        if len(results) == 0:
            return None  # No poses detected
        return results[0] # Return the first detected pose (assuming single person)
# yolo smaller so cpu can keep up with the processing (1.1)