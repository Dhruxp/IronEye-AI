# implements squats
from src.analyzers.base_analyser import BaseAnalyser
from src.angle_util import angle_calc
class SquatAnalyser(BaseAnalyser):
    def __init__(self):
        super().__init__()
        self.depths = []  # Store squat depths for feedback
    def process_frame(self, kp):
        left_hip = kp[11] 
        left_knee = kp[13]
        left_ankle = kp[15]
        angle = angle_calc(left_hip, left_knee, left_ankle)
        self.depths.append(angle)
        if angle < 90:
            self.stage = "down"
        if (angle > 160 and self.stage == "down"):
            self.reps += 1
            self.stage = "up"
    def get_feedback(self):
        if len(self.depths) == 0:
            return "No squats detected"
        min_angle = min(self.depths)
        if min_angle > 100:
            return "Try to squat deeper"
        return "Good squat depth"
# 3 keypoints: hip, knee, ankle
# Single view only as of v1
