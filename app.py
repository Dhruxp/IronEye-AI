import cv2
from src.pose_detector import PoseDetector
from src.analyzers.squat_analyser import SquatAnalyser
from src.angle_util import angle_calc
from src.exercise_factory import ExerciseFactory
detector = PoseDetector()
analyser = ExerciseFactory.create_exercise_analyser("pushup") # object from factory created
vid = cv2.VideoCapture("vids/bicepcurl_internet02.mp4") #internet sample
cv2.namedWindow(
    "IronEye AI",
    cv2.WINDOW_NORMAL
)
cv2.resizeWindow(
    "IronEye AI",
    1280,
    720
)
#frame_count = 0
while vid.isOpened():
    success, frame = vid.read()
    if not success:
        break
    #frame_count += 1
    #only process every 3rd frame to reduce load (1.1)
    #if frame_count % 3 != 0:
    #    continue
    frame = cv2.resize(
        frame,
        (960, 540)
    )
    result = detector.detect_pose(frame)
    if result is None:
        continue
    if result.keypoints is None:
        continue
    if len(result.keypoints.xy) == 0:
        continue
    kp = result.keypoints.xy[0].cpu().numpy()
    analyser.process_frame(kp)
    # Draw keypoints
    for point in kp:
        x = int(point[0])
        y = int(point[1])
        cv2.circle(
            frame,
            (x, y),
            5,
            (0, 255, 0),
            -1
        )
    # Calculate knee angle for debugging
    left_hip = kp[11]
    left_knee = kp[13]
    left_ankle = kp[15]
    angle = angle_calc(
        left_hip,
        left_knee,
        left_ankle
    )
    # Rep counter
    cv2.putText(
        frame,
        f"Reps: {analyser.reps}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
    # Feedback
    feedback = analyser.get_feedback()
    cv2.putText(
        frame,
        feedback,
        (10, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )
    # Knee angle
    cv2.putText(
        frame,
        f"Angle: {int(angle)}",
        (10, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )
    # Show video
    cv2.imshow(
        "IronEye AI",
        frame
    )
    # Press Q to quit
    if cv2.waitKey(20) & 0xFF == ord("q"): #more breathing space for non lag
        break
vid.release()
cv2.destroyAllWindows()