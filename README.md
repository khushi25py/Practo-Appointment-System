🏥 Practo Appointment System
📌 Overview
Practo Appointment System is a full-stack web application that allows doctors and patients to connect easily.
Doctors can create profiles, log in, and manage appointments, while patients can register, log in, and schedule appointments seamlessly.
This project is inspired by the online healthcare consultation system Practo, designed for educational and practical learning in full-stack web development using Django.

⚙️ Features
👨‍⚕️ For Doctors
Register and manage profile information
Log in securely
View and manage appointments

👩‍🦰 For Patients
Create an account and log in
Browse doctors and book appointments
Manage scheduled appointments

| Layer                     | Technology            |
| ------------------------- | --------------------- |
| **Frontend**              | HTML, CSS, JavaScript |
| **Backend**               | Django (Python)       |
| **Database**              | MySQL (via XAMPP)     |
| **Deployment**            | Render                |
| **Static Files Handling** | WhiteNoise            |

🗂️ Project Structure
Practo-Appointment-System/
│
├── doctor/                # Doctor app
├── patient/               # Patient app
├── mypracto/              # Main project folder
├── static/                # Static assets (CSS, JS, images)
├── templates/             # HTML templates
├── manage.py
└── requirements.txt


⚡ How to Run Locally

1.Clone the repository
git clone https://github.com/khushi25py/Practo-Appointment-System.git
cd Practo-Appointment-System


2.Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3.Install dependencies
pip install -r requirements.txt

4.Run migrations
python manage.py migrate

5.Start the server
python manage.py runserver

6.Visit the app at http://127.0.0.1:8000/

🌐 Live Demo

🔗 https://practo-appointment-system.onrender.com
(for now it's not working,fixing the cache)

📸 Screenshots
<img width="1890" height="718" alt="image" src="https://github.com/user-attachments/assets/12f74583-6a1b-438c-bff3-841d0b46cb38" />
<img width="1208" height="873" alt="image" src="https://github.com/user-attachments/assets/b4229d27-3706-4910-9416-51b788b9072f" />
<img width="1886" height="867" alt="image" src="https://github.com/user-attachments/assets/4c1962b4-534b-435b-8463-43453216a96a" />

🧾 Requirements
Python 3.x
Django 4.x
MySQL
XAMPP
Render (for deployment)

💡 Future Improvements
Add email verification and notifications
Enable password reset
Enhance UI with modern design
Add appointment reminders

👩‍💻 Author
Khushi Gupta
