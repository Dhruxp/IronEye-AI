from dataclasses import dataclass
from typing import List, Dict
@dataclass
class FeedbackReport: #issues, positives and metrics scores come as a FeedbackReport() object 
    score: float
    issues: List[str]
    positives: List[str]
    metrics: Dict[str, float]