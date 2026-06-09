from src.analyzers.squat_analyser import SquatAnalyser
from src.analyzers.bicep_curl import BicepCurlAnalyser
class ExerciseFactory:
    @staticmethod
    def create_exercise_analyser(exercise):
        if exercise.lower() == "squat":
            return SquatAnalyser()
        if exercise.lower() == "bicep curl":
            return BicepCurlAnalyser() # Updated (1.1)
        else:
            raise ValueError(f"Exercise '{exercise}' not supported")
# Ease of workflow (1.1)
