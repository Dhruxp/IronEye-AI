from src.analyzers.base_analyser import BaseAnalyser
from src.angle_util import angle_calc
class BicepCurlAnalyser(BaseAnalyser):
    def __init__(self):
        super().__init__()
    def process_frame(self, kp):
        shoulder = kp[5]
        elbow = kp[7]
        wrist = kp[9]
        angle = angle_calc(
            shoulder,
            elbow,
            wrist
        )
        if angle < 80:
            self.stage = "up"
        if (angle > 120 and self.stage == "up"):
            self.reps+=1
            self.stage = "down"
    def get_feedback(self):
        if self.stage == "up":
            return "Good job! Keep going!"
        else:
            return "Lower your arm to complete the rep."
    