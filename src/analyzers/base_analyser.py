from abc import ABC, abstractmethod
class BaseAnalyser(ABC):
    def __init__(self):
        self.reps = 0
        self.stage = None
    @abstractmethod
    def process_frame(self, keypoints):
        pass
    @abstractmethod
    def get_feedback(self):
        pass    
# Parent class for all 
