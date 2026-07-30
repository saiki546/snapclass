# SnapClass – AI-Powered Smart Classroom Platform

An AI-powered smart classroom platform that automates student attendance using face recognition and speaker verification while providing secure authentication and classroom management features.

## 🚀 Live Demo

🌐 Live Application:
(https://snapclass-aiapp.streamlit.app/)

## ✨ Features

- Secure user authentication
- Face Recognition based attendance
- Speaker Recognition
- QR Code generation
- Cloud database integration
- Attendance history
- Streamlit dashboard
- Fast and user-friendly interface

## 📸 Screenshots

### Login

(image)

### Dashboard

(image)

### Face Recognition

(image)

### Attendance

(image)

## 🛠 Tech Stack

### Frontend
- Streamlit

### Programming Language
- Python

### Machine Learning
- Scikit-learn

### Computer Vision
- dlib
- Face Recognition

### Audio Processing
- Librosa
- Resemblyzer

### Database
- Supabase

### Authentication
- bcrypt

### Data Processing
- NumPy
- Pandas

### Image Processing
- Pillow

### QR Code
- Segno


### Project Architecture

User
   │
   ▼
Streamlit UI
   │
   ▼
Authentication (Supabase + bcrypt)
   │
   ├─────────────┐
   ▼             ▼
Face Recognition Speaker Recognition
   │             │
   └──────┬──────┘
          ▼
 Attendance Processing
          ▼
      Supabase Database



### Folder Structure

SnapClass
│
├── pages/
├── utils/
├── models/
├── database/
├── images/
├── app.py
├── requirements.txt
└── README.md

### Installation
git clone https://github.com/yourusername/SnapClass.git

cd SnapClass

pip install -r requirements.txt

streamlit run app.py


### How It Works
## Workflow

1. User logs into the system.
2. Authentication is verified.
3. Face Recognition identifies the student.
4. Speaker Recognition verifies the user's voice.
5. Attendance is recorded.
6. Data is stored in Supabase.
7. Dashboard displays attendance history.

### Challenges

- Improving face recognition accuracy
- Handling different lighting conditions
- Reducing false voice matches
- Secure authentication
- Managing cloud database integration

## Future Improvements

- Mobile application
- Multiple classroom support
- Real-time notifications
- Teacher analytics dashboard
- Face anti-spoofing
- Attendance reports

## Skills Demonstrated

- Python Development
- Machine Learning
- Computer Vision
- Face Recognition
- Speaker Recognition
- Authentication
- Streamlit
- Database Integration
- Cloud Deployment
- Data Processing

## Author

Sai

LinkedIn:https://www.linkedin.com/in/sai-kiran-492283318/
GitHub:https://github.com/saiki546
Email:saikirananimela01@gmail.com

