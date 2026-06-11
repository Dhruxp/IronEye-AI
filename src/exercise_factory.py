from src.analyzers.squat_analyser import SquatAnalyser
from src.analyzers.bicep_curl import BicepCurlAnalyser
from src.analyzers.pushup_analyser import PushUpAnalyser
from src.analyzers.shoulder_press_analyser import ShoulderPressAnalyser
from src.analyzers.deadlift_analyser import DeadliftAnalyser
class ExerciseFactory:
    @staticmethod
    def create_exercise_analyser(exercise):
        if exercise.lower() == "squat":
            return SquatAnalyser()
        if exercise.lower() == "bicep curl":
            return BicepCurlAnalyser() # Updated (1.1)
        if exercise.lower() == "pushup":
            return PushUpAnalyser() # Updated (1.2)
        if exercise.lower() == "shoulder press":
            return ShoulderPressAnalyser() # Updated (1.3)
        if exercise.lower() == "deadlift":
            return DeadliftAnalyser() # Updated (1.4)
        else:
            raise ValueError(f"Exercise '{exercise}' not supported")
# Ease of workflow (1.1)
