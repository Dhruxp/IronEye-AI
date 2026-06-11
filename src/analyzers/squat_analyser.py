# implements squats
from src.analyzers.base_analyser import BaseAnalyser
from src.angle_util import angle_calc
import numpy as np # 1.4
class SquatAnalyser(BaseAnalyser):
    def __init__(self):
        super().__init__()
        self.deepest_angle = 180  # Track the deepest squat angle
        self.max_angle_lean = 0 # Check for back bend
        self.depths = []  # Store squat depths for feedback
        self.knee_valg_detected = False #Knee collapse checker 
    def process_frame(self, kp):
        left_hip = kp[11] 
        left_knee = kp[13]
        left_ankle = kp[15]
        shoulder = kp[5] # check for coaching cues (1.4)
        hip = kp[11] # 1.4
        knee = kp[13] # 1,4
        ankle = kp[15] # 1.4 # New initialisations to seperate 1.1 and 1.4 
        torso_dx = shoulder[0] - hip[0]
        torso_dy = shoulder[1] - hip[1]
        torso_angle = abs(np.degrees(np.arctan2(torso_dy, torso_dx))) # 1.4 
        # angle calculated based on formula 
        angle = angle_calc(left_hip, left_knee, left_ankle)
        self.deepest_angle = min(self.deepest_angle, angle) # fine tune (1.4)
        self.max_angle_lean = max(self.max_angle_lean, torso_angle) #fine tune (1.4)
        self.depths.append(angle)
        if angle < 100: #check only when down 
            hip_x = hip[0] # for knee collapses 
            knee_x = knee[0]
            ankle_x = ankle[0]
            if abs(knee_x - ankle_x) < 15:
                self.knee_valg_detected = True 
        if angle < 90:
            self.stage = "down"
        if (angle > 160 and self.stage == "down"):
            self.reps += 1
            self.stage = "up"
    def get_feedback(self): # 1.4, multi feedback model 
        #if len(self.depths) == 0: (1.1 workflow)
            #return "No squats detected"
        #min_angle = min(self.depths)
        #if min_angle > 100:
            #return "Try to squat deeper"
        #return "Good squat depth"
        feedback = []
        if self.deepest_angle > 100:
            feedback.append("Squat deeper")
        if self.max_angle_lean > 35:
            feedback.append("Excessive lean")
        if self.knee_valg_detected:
            feedback.append("Knee collapsing")
        if len(feedback) == 0:
            feedback.append("Form is good maintain")
        return "|".join(feedback) # string needed in app.py 
    

