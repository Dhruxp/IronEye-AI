from src.analyzers.base_analyser import BaseAnalyser
from src.angle_util import angle_calc
class PushUpAnalyser(BaseAnalyser):
    def __init__(self):
        super().__init__()
    def process_frame(self, kp):
        shoulder = kp[6]
        elbow = kp[8]
        wrist = kp[10]
        angle = angle_calc(shoulder, elbow, wrist)
        if self.stage is None:
            if angle > 130:
                self.stage = "up"
            else:
                self.stage = "down"
        if angle < 80:
            self.stage = "down"
        if (angle > 130 and self.stage == "down"):
            self.count += 1
            self.stage = "up"
    def get_feedback(self):
        return "Good pushup form"
    
        