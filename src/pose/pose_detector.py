from ultralytics import YOLO
from src.pose.pose_frame import PoseFrame
from src.biomechanics import Biomechanics
class PoseDetector:
    def __init__(self):
        self.model = YOLO("yolov8n-pose.pt")
    def detect_pose(self, frame):
        results = self.model(
            frame,
            imgsz=320,
            verbose=False
        )
        if len(results) == 0:
            return None
        result = results[0]
        if result.keypoints is None:
            return None
        if len(result.keypoints.xy) == 0:
            return None
        keypoints = result.keypoints.xy[0].cpu().numpy()
        confidence = result.keypoints.conf[0].cpu().numpy()
        best_side = Biomechanics.best_side(
            confidence
        )
        pose_frame = PoseFrame(
            keypoints=keypoints,
            confidence=confidence,
            best_side=best_side
        )
        return pose_frame
    #pipeline changes - 1.6