from src.analyzers.base_analyser import BaseAnalyser
from src.angle_util import angle_calc
class DeadliftAnalyser(BaseAnalyser):
    def __init__(self):
        super().__init__()
        self.max_angle = 0
    def process_frame(self, kp):
        shoulder = kp[6]
        hip = kp[12]
        knee = kp[14]
        angle = angle_calc(
            shoulder,
            hip,
            knee
        )
        self.max_angle = max(self.max_angle, angle)
        if self.stage is None:
            if angle > 130:
                self.stage = "down"
            else:
                self.stage = "up"
        if angle > 150:
            self.stage = "up"
        if angle < 130 and self.stage == "up":
            self.stage = "down"
            self.rep_count += 1
    def get_feedback(self):
        if self.max_angle < 150:
            return "Finish your lockout"
        return "Good lockout"