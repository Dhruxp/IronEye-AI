from src.analyzers.squat_analyser import SquatAnalyser
from src.analyzers.bicep_curl import BicepCurlAnalyser
from src.analyzers.pushup_analyser import PushUpAnalyser
class ExerciseFactory:
    @staticmethod
    def create_exercise_analyser(exercise):
        if exercise.lower() == "squat":
            return SquatAnalyser()
        if exercise.lower() == "bicep curl":
            return BicepCurlAnalyser() # Updated (1.1)
        if exercise.lower() == "pushup":
            return PushUpAnalyser() # Updated (1.2)
        else:
            raise ValueError(f"Exercise '{exercise}' not supported")
# Ease of workflow (1.1)
