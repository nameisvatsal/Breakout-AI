Email Sending Dashboard
This project provides a simple web interface for uploading a CSV file and sending customized emails to multiple recipients. The system allows users to upload data, customize email content with a template and personalization prompts, and send emails through a Gmail SMTP server.

Features
File Upload: Upload CSV files containing recipient data (e.g., name, email).
Email Customization: Customize the subject, body template, and personalization prompt for each email.
Real-Time Status: Display upload and email sending statuses.
Groq Integration: Personalize email content using AI-generated responses from the Groq API.
Email Sending: Send emails using a Gmail SMTP server.
Prerequisites
Python 3.x
Flask
Flask-RESTX
Groq Client (for personalization)
Pandas
Flask-CORS
Gmail SMTP credentials
Environment Variables
Make sure to set the following environment variables in your development environment:

GMAIL_USER: Your Gmail address (e.g., example@gmail.com).
GMAIL_PASSWORD: Your Gmail account password or an app-specific password.
GROQ_API_KEY: Your Groq API key for AI-powered personalization.
Installation
Step 1: Clone the repository
bash
Copy code
git clone https://github.com/yourusername/email-sending-dashboard.git
cd email-sending-dashboard
Step 2: Install dependencies
Make sure you have pip installed, then run:

bash
Copy code
pip install -r requirements.txt
Step 3: Set up environment variables
Create a .env file and add your environment variables:

makefile
Copy code
GMAIL_USER=your_email@gmail.com
GMAIL_PASSWORD=your_password
GROQ_API_KEY=your_groq_api_key
Step 4: Run the application
Start the Flask application:

bash
Copy code
python app.py
The server will start, and the dashboard can be accessed at http://127.0.0.1:5000/.

Usage
Upload Data: Click the "Upload File" button to upload a CSV file containing recipient information (e.g., name and email).
Customize Email: Enter a subject, body template, and a prompt for personalization.
Send Emails: Click the "Send Emails" button to send personalized emails to all recipients in the CSV file.
Check Status: Monitor the real-time status of the upload and email sending process.
API Endpoints
/upload (POST)
Description: Upload a CSV file containing recipient information.
Body: A file upload (CSV format).
Response:
200 OK: If the file is uploaded successfully.
400 Bad Request: If the file is not valid or missing.
500 Internal Server Error: If an error occurs during the upload.
/send_emails (POST)
Description: Send emails using the provided subject, body template, and personalization prompt.
Body: JSON containing:
subject: The subject of the email.
bodyTemplate: The body template of the email.
prompt: The prompt for generating personalized content (e.g., "Write a professional greeting for {name}").
Response:
200 OK: If emails are sent successfully.
400 Bad Request: If required data is missing.
500 Internal Server Error: If an error occurs while sending emails.
Folder Structure
php
Copy code
email-sending-dashboard/
│
├── app.py            # Main Flask application
├── requirements.txt  # Python dependencies
├── static/           # Static files (CSS, JS)
│   └── styles.css    # Stylesheet for the front-end
│   └── script.js     # JavaScript logic for the front-end
└── templates/        # HTML templates
    └── index.html    # Dashboard interface
Contributions
Contributions are welcome! If you want to contribute, please fork the repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
