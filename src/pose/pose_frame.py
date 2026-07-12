from dataclasses import dataclass
from src.pose.side import Side
import numpy as np
@dataclass
class PoseFrame:
    keypoints: np.ndarray
    confidence: np.ndarray
    best_side: Side