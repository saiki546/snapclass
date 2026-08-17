# SnapClass – AI-Powered Smart Classroom Platform

**SnapClass** is an AI-powered smart classroom platform designed to automate student attendance using **facial recognition and speaker verification**, while providing secure authentication, cloud-based data management, QR-based workflows, and attendance history.

The application combines **computer vision, audio processing, machine learning, and cloud database technologies** into a practical classroom management solution.

## Live Demo

**Live Application:**
https://snapclass-aiapp.streamlit.app/

> The live application is deployed using Streamlit.

---

## Overview

Traditional classroom attendance systems often depend on manual roll calls or basic attendance mechanisms.

SnapClass explores a multimodal approach to attendance automation by combining:

* Facial recognition
* Speaker recognition
* Secure authentication
* QR code generation
* Cloud database integration
* Attendance history
* Data processing and analytics
* Interactive Streamlit dashboard

The project demonstrates how multiple AI modalities can be integrated into a single application to solve a practical real-world problem.

---

## Key Features

### Face Recognition

SnapClass uses **dlib and face-recognition technologies** to identify students through facial features.

The attendance workflow can identify registered users and associate the recognition result with the corresponding attendance record.

### Speaker Recognition

The application uses **Librosa** for audio processing and **Resemblyzer** for speaker recognition.

The voice-processing workflow allows the application to verify users using voice characteristics.

### Secure Authentication

The application includes an authentication layer using:

* Supabase
* bcrypt

Authentication is performed before users access protected classroom functionality.

### Automated Attendance

Once a student's identity has been verified, the application processes and records attendance information in the connected database.

### QR Code Generation

SnapClass uses **Segno** to generate QR codes for classroom and attendance-related workflows.

### Attendance History

The application maintains attendance records and provides users with access to historical attendance information through the Streamlit dashboard.

### Cloud Database

**Supabase** is used for cloud-based data storage and application data management.

### Interactive Dashboard

The Streamlit interface provides a simple web-based experience for authentication, attendance workflows, recognition features, and attendance history.

---

## System Architecture

```text
                         ┌──────────────────────┐
                         │        User          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Streamlit UI      │
                         │      Dashboard       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Authentication     │
                         │  Supabase + bcrypt   │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
             ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
             │    Face     │ │   Speaker   │ │     QR      │
             │ Recognition │ │ Recognition │ │ Generation  │
             └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
                    │               │               │
                    └───────────────┼───────────────┘
                                    ▼
                         ┌──────────────────────┐
                         │ Attendance Processing │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       Supabase       │
                         │    Cloud Database    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Attendance History   │
                         │     & Dashboard      │
                         └──────────────────────┘
```

---

## AI & Recognition Pipeline

### Facial Recognition Workflow

```text
Camera / Image
      ↓
Face Detection
      ↓
Facial Feature Extraction
      ↓
Face Comparison
      ↓
Student Identification
      ↓
Attendance Processing
```

### Speaker Recognition Workflow

```text
Voice Input
     ↓
Audio Processing
     ↓
Speaker Representation
     ↓
Speaker Comparison
     ↓
User Verification
     ↓
Attendance Processing
```

By combining both visual and audio recognition, the project demonstrates a **multimodal AI approach** to identity verification.

---

## End-to-End Workflow

```text
1. User opens SnapClass
          ↓
2. User authenticates
          ↓
3. Classroom / attendance workflow starts
          ↓
4. Student identity is captured
          ↓
5. Face or voice recognition is performed
          ↓
6. Identity is verified
          ↓
7. Attendance is recorded
          ↓
8. Data is stored in Supabase
          ↓
9. Attendance history is available
          ↓
10. Dashboard displays attendance information
```

---

## Technology Stack

| Category              | Technologies           |
| --------------------- | ---------------------- |
| Programming Language  | Python                 |
| Application Framework | Streamlit              |
| Machine Learning      | Scikit-learn           |
| Computer Vision       | dlib, Face Recognition |
| Audio Processing      | Librosa                |
| Speaker Recognition   | Resemblyzer            |
| Database              | Supabase               |
| Authentication        | bcrypt                 |
| Data Processing       | NumPy, Pandas          |
| Image Processing      | Pillow                 |
| QR Code Generation    | Segno                  |
| Deployment            | Streamlit              |

These technologies correspond to the stack currently documented in the repository.

---

## Project Structure

The repository currently separates the application into source code, Streamlit configuration, application entry point, and dependency configuration.

```text
snapclass/
│
├── .streamlit/
│
├── src/
│
├── app.py
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

The current repository contains the `src/` directory, `.streamlit/` configuration, `app.py`, `requirements.txt`, and project documentation.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/saiki546/snapclass.git
cd snapclass
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Configure the required Supabase credentials and other sensitive configuration values through environment variables.

**Do not commit API keys, passwords, database credentials, or other secrets to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser through the local Streamlit server.

---

## Engineering Challenges

### 1. Face Recognition Accuracy

Facial recognition can be affected by:

* Lighting conditions
* Camera quality
* Face orientation
* Distance from the camera
* Variations in facial appearance

The project explores practical face-recognition-based identification within a classroom attendance workflow.

### 2. Speaker Recognition

Voice recognition can be affected by:

* Background noise
* Microphone quality
* Recording conditions
* Differences in speaking style
* Environmental conditions

The project uses audio processing and speaker representations to support voice-based verification.

### 3. Multimodal AI Integration

Integrating facial recognition, speaker recognition, authentication, database operations, and attendance processing requires coordinating several different components within one application.

### 4. Cloud Database Integration

Attendance information needs to be persisted and retrieved reliably from the cloud database while remaining connected to the application's authentication and attendance workflows.

---

## Security

The application includes authentication functionality using **Supabase and bcrypt**.

The current project demonstrates application-level authentication, but a production deployment involving biometric information would require additional security and privacy controls.

Potential production considerations include:

* HTTPS/TLS
* Strong access-control policies
* Secure secret management
* Database security policies
* Audit logging
* Biometric data protection
* Data retention policies
* Privacy and consent mechanisms
* Rate limiting
* Liveness / anti-spoofing mechanisms

These are **production considerations and should not be interpreted as currently implemented features unless explicitly configured in the application.**

---

## Current Capabilities

SnapClass currently demonstrates:

* AI-assisted attendance automation
* Face recognition
* Speaker recognition
* Audio processing
* Machine learning integration
* Secure authentication
* Cloud database integration
* QR code generation
* Attendance history
* Interactive Streamlit dashboard
* Cloud deployment

---

## Future Improvements

Potential improvements include:

### AI & Recognition

* Face anti-spoofing / liveness detection
* Improved recognition under different lighting conditions
* More robust speaker verification
* Noise-resistant audio processing
* Improved recognition confidence handling

### Classroom Management

* Multiple classroom support
* Teacher and student roles
* Teacher analytics dashboard
* Attendance reports
* Real-time notifications
* Automated attendance summaries

### Security & Privacy

* Stronger role-based access control
* Improved biometric data protection
* Secure data retention policies
* Comprehensive audit logging
* Production-grade security architecture

### Platform

* Mobile application
* Responsive interface improvements
* Improved analytics
* Scalable cloud architecture

---

## What This Project Demonstrates

This project demonstrates practical experience in:

**Artificial Intelligence**

* Machine Learning
* Computer Vision
* Facial Recognition
* Speaker Recognition
* Multimodal AI

**Software Development**

* Python
* Streamlit
* Application Architecture
* Authentication
* Database Integration

**Data & AI Processing**

* NumPy
* Pandas
* Librosa
* Image Processing

**Cloud & Deployment**

* Supabase
* Streamlit Deployment

---

## Project Highlights

### Multimodal AI

Combines facial and speaker recognition within a single classroom attendance workflow.

### End-to-End Application

Connects AI models, user authentication, database operations, attendance processing, and a web interface into one application.

### Practical Problem Solving

Addresses a real-world classroom problem rather than implementing an isolated machine-learning model.

### Cloud-Connected

Uses Supabase for persistent application data and is deployed as an accessible Streamlit web application.

---

## Live Application

**SnapClass:**
https://snapclass-aiapp.streamlit.app/

---

## Repository

**GitHub:**
https://github.com/saiki546/snapclass

---

## Author

**Animela Venkata Sai Kiran**

B.Tech — Computer Science and Engineering (AI-ML)

GitHub: https://github.com/saiki546
LinkedIn: https://linkedin.com/in/saikiran-animela-44b5b5352/
Email: [saikirananimela01@gmail.com](mailto:saikirananimela01@gmail.com)

---

## Disclaimer

SnapClass is an AI/ML portfolio project developed to explore the integration of computer vision, speaker recognition, authentication, cloud databases, and application development.

Biometric recognition systems can involve sensitive personal data. Any production deployment should implement appropriate privacy, consent, security, and data-protection measures.
