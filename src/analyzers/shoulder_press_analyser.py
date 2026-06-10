from src.analyzers.base_analyser import BaseAnalyser
from src.angle_util import angle_calc
class ShoulderPressAnalyser(BaseAnalyser):
    def __init__(self):
        super().__init__()
        self.min_angle = 999
        self.max_angle = 0
    def process_frame(self, kp):
        shoulder = kp[6]
        elbow = kp[8]
        wrist = kp[10]
        angle = angle_calc(shoulder, elbow, wrist)
        self.min_angle = min(self.min_angle, angle)
        self.max_angle = max(self.max_angle, angle)
        if self.stage is None:
            if angle < 120:
                self.stage = "down"
            else:
                self.stage = "up"
        if angle > 150:
            self.stage = "up"
        if (angle < 110 and self.stage == "up"):
            self.reps += 1
            self.stage = "down"
    def get_feedback(self):
        if self.max_angle < 150:
            return "Lock out your arms at the top"
        return "Lower the weight more at the bottom"
# New analyser for shoulder press (1.3)