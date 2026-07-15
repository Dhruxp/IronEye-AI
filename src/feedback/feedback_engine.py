from src.feedback.feedback_models import FeedbackReport
class FeedbackEngine:
    @staticmethod
    def generate(exercise: str, metrics: dict) -> FeedbackReport:
        exercise = exercise.lower() #check for existence of exercise in v1.0
        if exercise == "squat":
            return FeedbackEngine._evaluate_squat(metrics)
        elif exercise == "curl":
            return FeedbackEngine._evaluate_curl(metrics)
        elif exercise == "pushup":
            return FeedbackEngine._evaluate_pushup(metrics)
        elif exercise == "shoulderpress":
            return FeedbackEngine._evaluate_shoulder_press(metrics)
        elif exercise == "deadlift":
            return FeedbackEngine._evaluate_deadlift(metrics)
        raise ValueError(f"Unsupported exercise: {exercise}")
    #squat eval
    def _evaluate_squat(metrics: dict) -> FeedbackReport:
        deepest_angle = metrics["deepest_angle "]
        torse_lean = metrics["torse_lean"]
        knee_valgus = metrics["knee_valgus"]
        score = 10.0
        positives =[]
        issues = []
        if deepest_angle <= 90: #depth check
            positives.append("Good depth achieved.")
        elif deepest_angle <= 100:
            issues.append("Depth is slightly shallow. Aim for a deeper squat.")
            score -= 1.0
        else:
            issues.append("Depth is too shallow. Aim for a deeper squat.")
            score -= 2.0
        if torse_lean < 25: #torse lean check
            positives.append("Good torso lean.")
        elif torse_lean < 35:
            issues.append("Torso lean is slightly excessive. Keep your back more upright.")
            score -= 0.5 #light punishing for lean
        else:
            issues.append("Torso lean is excessive. Keep your back more upright.")
            score -= 2.0
        if knee_valgus: #knee valgus check
            issues.append("Knee valgus detected. Focus on keeping your knees aligned with your toes.")
            score -= -3.0 #heavy punishing
        else:
            positives.append("No knee valgus detected.")
        #score calculation
        score = max(0.0, round(score, 1)) #ensure score is not negative and round to 1 decimal place
        return FeedbackReport(score=score, issues=issues,
                               positives=positives,
                               metrics = {"deepest knee angle": deepest_angle,
                                          "maximum torse lean": torse_lean,}
                               )
    #curl, pushup, shoulder press, and deadlift evaluation methods coming with v1.1
    @staticmethod
    def _evaluate_curl(metrics: dict) -> FeedbackReport: #curl evaluation
        return FeedbackReport(  score=10.0, 
                                issues=[],
                                positives=["Coming soon"], 
                                metrics=metrics
                            )
    def _evaluate_pushup(metrics: dict) -> FeedbackReport: #pushup evaluation
        return FeedbackReport(  score=10.0, 
                                issues=[],
                                positives=["Coming soon"], 
                                metrics=metrics
                            )
    def _evaluate_shoulder_press(metrics: dict) -> FeedbackReport: #shoulder press evaluation
        return FeedbackReport(  score=10.0, 
                                issues=[],
                                positives=["Coming soon"], 
                                metrics=metrics
                            )
    def _evaluate_deadlift(metrics: dict) -> FeedbackReport: #deadlift evaluation
        return FeedbackReport(  score=10.0, 
                                issues=[],
                                positives=["Coming soon"], 
                                metrics=metrics
                            )