import numpy as np
from src.angle_util import angle_calc
class biomechanics:
    #joints
    @staticmethod
    def left_shoulder(kp):
        return kp[5]
    @staticmethod
    def right_shoulder(kp):
        return kp[6]
    @staticmethod
    def left_hip(kp):
        return kp[11] 
    @staticmethod
    def right_hip(kp):
        return kp[12]
    @staticmethod
    def left_knee(kp):
        return kp[13]
    @staticmethod
    def right_knee(kp):
        return kp[14]
    @staticmethod
    def left_ankle(kp):
        return kp[15]
    @staticmethod
    def right_ankle(kp):
        return kp[16]
    @staticmethod
    def left_elbow(kp):
        return kp[7]
    @staticmethod
    def right_elbow(kp):
        return kp[8]
    @staticmethod
    def left_wrist(kp):
        return kp[9]    
    @staticmethod
    def right_wrist(kp):
        return kp[10]
    #angle extraction - elbow
    @staticmethod
    def left_elbow_angle(kp):
        return angle_calc(biomechanics.left_shoulder(kp), biomechanics.left_elbow(kp), biomechanics.left_wrist(kp))
    @staticmethod
    def right_elbow_angle(kp):
        return angle_calc(biomechanics.right_shoulder(kp), biomechanics.right_elbow(kp), biomechanics.right_wrist(kp))
    #angle extraction - knee
    @staticmethod
    def left_knee_angle(kp):    
        return angle_calc(biomechanics.left_hip(kp), biomechanics.left_knee(kp), biomechanics.left_ankle(kp))   
    @staticmethod
    def right_knee_angle(kp):
        return angle_calc(biomechanics.right_hip(kp), biomechanics.right_knee(kp), biomechanics.right_ankle(kp))
    #angle extraction - hip
    @staticmethod
    def left_hip_angle(kp):
        return angle_calc(biomechanics.left_shoulder(kp), biomechanics.left_hip(kp), biomechanics.left_knee(kp))
    @staticmethod
    def right_hip_angle(kp):
        return angle_calc(biomechanics.right_shoulder(kp), biomechanics.right_hip(kp), biomechanics.right_knee(kp))
    #angle extraction - torso
    @staticmethod
    def torso_lean_left(kp):
        shoulder = biomechanics.left_shoulder(kp)
        hip = biomechanics.left_hip(kp)
        torso_dx = shoulder[0] - hip[0]
        torso_dy = shoulder[1] - hip[1]
        return abs(np.degrees(np.arctan2(torso_dy, torso_dx)))
    @staticmethod
    def torso_lean_right(kp):
        shoulder = biomechanics.right_shoulder(kp)
        hip = biomechanics.right_hip(kp)
        torso_dx = shoulder[0] - hip[0]
        torso_dy = shoulder[1] - hip[1]
        return abs(np.degrees(np.arctan2(torso_dy, torso_dx)))
    #body alignment
    @staticmethod
    def body_alignment_left(kp):
        return angle_calc(biomechanics.left_shoulder(kp), biomechanics.left_hip(kp), biomechanics.left_knee(kp))
    @staticmethod
    def body_alignment_right(kp):
        return angle_calc(biomechanics.right_shoulder(kp), biomechanics.right_hip(kp), biomechanics.right_knee(kp))
    #knee valgus detection
    @staticmethod
    def knee_valgus_left(kp, threshold=15):
        knee = biomechanics.left_knee(kp)
        ankle = biomechanics.left_ankle(kp)
        return abs(knee[0] - ankle[0]) < threshold
    @staticmethod
    def knee_valgus_right(kp, threshold=15):
        knee = biomechanics.right_knee(kp)
        ankle = biomechanics.right_ankle(kp)
        return abs(knee[0] - ankle[0]) < threshold
    #ROM help functions
    @staticmethod
    def full_extension(angle, threshold=160):
        return angle >= threshold
    @staticmethod
    def full_flexion(angle, threshold=90):
        return angle <= threshold
    @staticmethod
    def partial_range(angle, lower_threshold=90, upper_threshold=160):
        return lower_threshold <= angle <= upper_threshold
    #distance help functions
    @staticmethod
    def euclidean_distance(point1, point2):
        return np.linalg.norm(np.array(point1) - np.array(point2))
    #confidence helpers - 1.6
    @staticmethod
    def midpoint(point1, point2):
        return np.array([(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2])
    #side detection (new)
    @staticmethod
    def side_confidence(conf, side):
        if side == "left":
            indices = [5, 7, 9, 11, 13, 15]  # left shoulder, elbow, wrist, hip, knee, ankle
        elif side == "right":
            indices = [6, 8, 10, 12, 14, 16]  # right shoulder, elbow, wrist, hip, knee, ankle
        return np.mean(conf[indices])
    @staticmethod
    def best_side(conf):
        left_conf = biomechanics.side_confidence(conf, "left")
        right_conf = biomechanics.side_confidence(conf, "right")
        return "left" if left_conf >= right_conf else "right" #check for side
    #return angle based on side
    @staticmethod
    def elbow_angle(kp, conf):
        side = biomechanics.best_side(conf)
        if side == "left":
            return biomechanics.left_elbow_angle(kp)
        else:
            return biomechanics.right_elbow_angle(kp)
    @staticmethod
    def knee_angle(kp, conf):
        side = biomechanics.best_side(conf)
        if side == "left":
            return biomechanics.left_knee_angle(kp)
        else:
            return biomechanics.right_knee_angle(kp)
    @staticmethod
    def hip_angle(kp, conf):
        side = biomechanics.best_side(conf)
        if side == "left":
            return biomechanics.left_hip_angle(kp)
        else:
            return biomechanics.right_hip_angle(kp)
    @staticmethod
    def torso_lean(kp, conf):
        side = biomechanics.best_side(conf)
        if side == "left":
            return biomechanics.torso_lean_left(kp)
        else:
            return biomechanics.torso_lean_right(kp)
    @staticmethod
    def body_alignment(kp, conf):
        side = biomechanics.best_side(conf)
        if side == "left":
            return biomechanics.body_alignment_left(kp)
        else:
            return biomechanics.body_alignment_right(kp)
    @staticmethod
    def knee_valgus(kp, conf, threshold=15):
        side = biomechanics.best_side(conf)
        if side == "left":
            return biomechanics.knee_valgus_left(kp, threshold)
        else:
            return biomechanics.knee_valgus_right(kp, threshold)
