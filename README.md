# IronEye AI

IronEye AI is a computer vision-based exercise analysis system that uses YOLOv8 Pose Estimation to track human movement, count repetitions, analyze exercise form, and provide real-time feedback.

The goal of the project is to build an AI-powered gym coach capable of analyzing multiple exercises, providing biomechanical insights, and helping users improve their training technique.

## Features

### Current Features

- YOLOv8 Pose Estimation
- Real-time video processing
- Squat repetition counting
- Knee angle calculation
- Live feedback overlay
- Keypoint visualization

### Planned Features

- Bicep Curl Analysis
- Push-Up Analysis
- Deadlift Analysis
- Shoulder Press Analysis
- Lunge Analysis
- Exercise Classification
- Workout Reports
- Webcam Support
- Streamlit Dashboard
- Progress Tracking

## Project Structure

```text
IronEye-AI/

├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── pose_detector.py
│   ├── angle_utils.py
│   ├── exercise_factory.py
│   │
│   └── analyzers/
│       ├── __init__.py
│       ├── base_analyser.py
│       ├── squat_analyser.py
│       └── curl_analyser.py
│
├── tests/
│
├── vids/
└── outputs/
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/IronEye-AI.git
cd IronEye-AI
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

Place a video file inside the `vids/` directory.

Run:

```bash
python app.py
```

The application will:

1. Load the video.
2. Detect human pose using YOLOv8 Pose.
3. Extract body keypoints.
4. Calculate joint angles.
5. Count repetitions.
6. Display live exercise metrics and feedback.

## Current Squat Analysis

The current implementation supports squat analysis using:

- Hip, knee, and ankle keypoints
- Knee angle computation
- State-machine based repetition counting
- Depth assessment
- Real-time feedback display

## Technologies Used

- Python
- YOLOv8 Pose
- Ultralytics
- OpenCV
- NumPy
- Streamlit (planned)
- PyTest

## Roadmap

### Phase 1: MVP

- [x] Video processing pipeline
- [x] Pose estimation
- [x] Angle calculation
- [x] Squat repetition counting
- [x] Feedback overlay
- [x] Keypoint visualization

### Phase 2: Multi-Exercise Support

- [x] Bicep Curl Analysis
- [x] Push-Up Analysis
- [x] Deadlift Analysis
- [x] Shoulder Press Analysis
- [ ] Lunge Analysis
- [x] Exercise Factory Architecture

### Phase 3: Product Features

- [ ] Streamlit Dashboard
- [ ] Webcam Support
- [ ] Workout Reports
- [ ] Session History
- [ ] Progress Tracking

### Phase 4: Advanced Features

- [ ] Automatic Exercise Classification
- [ ] Form Error Detection
- [ ] Personalized Feedback
- [ ] Real-Time Coaching
- [ ] Performance Analytics

## Contributing

Contributions, suggestions, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## License

This project is licensed under the MIT License.

## Author

Dhruv P.