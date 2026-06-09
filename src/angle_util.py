import numpy as np
def angle_calc(a, b, c):
    # Returns angle in degrees
    a = np.array(a)
    b = np.array(b) 
    c = np.array(c)
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    cosine_angle = np.clip(cosine_angle, -1.0, 1.0)  # Clip to avoid numerical issues
    angle = np.degrees(np.arccos(cosine_angle))
    return angle