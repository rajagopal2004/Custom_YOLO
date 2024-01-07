from roboflow import Roboflow
rf = Roboflow(api_key="L7RaAdWLO85rQwShWU0b")
project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
dataset = project.version(4).download("yolov8")
