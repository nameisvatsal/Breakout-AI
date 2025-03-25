
---

# 📧 Email Sending Dashboard

![Email Dashboard](https://github.com/user-attachments/assets/90f9c14b-ad00-4370-a836-a0bbfa0fa901)

This project provides a simple web interface for uploading a CSV file and sending customized emails to multiple recipients. It allows users to upload data, customize email content with a template and personalization prompts, and send emails through a Gmail SMTP server.

---

## 🚀 Features

✅ **File Upload:** Upload CSV files containing recipient data (e.g., name, email).  
✅ **Email Customization:** Customize the subject, body template, and personalization prompt.  
✅ **Real-Time Status:** Display upload and email sending statuses.  
✅ **Groq API Integration:** Personalize email content using AI-generated responses.  
✅ **Email Sending:** Send emails via Gmail SMTP.

---

## 🛠 Prerequisites

- Python 3.x
- Flask
- Flask-RESTX
- Flask-CORS
- Pandas
- Groq Client (for AI personalization)
- Gmail SMTP credentials

---

## 🔐 Environment Variables

Create a `.env` file with the following variables:

```
GMAIL_USER=your_email@gmail.com
GMAIL_PASSWORD=your_app_password
GROQ_API_KEY=your_groq_api_key
```

---

## ⚙️ Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/email-sending-dashboard.git
cd email-sending-dashboard
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python app.py
```

Access the dashboard at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📖 Usage

1. **Upload Data:** Click **"Upload File"** to upload a CSV with recipient data (`name`, `email`).
2. **Customize Email:** Enter:
   - **Subject**
   - **Body Template**
   - **Personalization Prompt**
3. **Send Emails:** Click **"Send Emails"** to process and send customized emails.
4. **Monitor Status:** View real-time updates on upload and sending progress.

---

## 🧩 API Endpoints

### 📥 `/upload` (POST)
- **Description:** Upload CSV with recipient data.
- **Body:** Multipart form-data (CSV file)
- **Responses:**
  - `200 OK`: File uploaded successfully.
  - `400 Bad Request`: Invalid or missing file.
  - `500 Internal Server Error`: Upload failure.

---

### 📤 `/send_emails` (POST)
- **Description:** Send personalized emails.
- **Body:** JSON
```json
{
  "subject": "Your Email Subject",
  "bodyTemplate": "Hello {name}, your message here.",
  "prompt": "Write a professional greeting for {name}"
}
```
- **Responses:**
  - `200 OK`: Emails sent successfully.
  - `400 Bad Request`: Missing data.
  - `500 Internal Server Error`: Sending failure.

---

## 📂 Folder Structure

```
email-sending-dashboard/
│
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
│
├── static/             # Static files (CSS, JS)
│   ├── styles.css
│   └── script.js
│
└── templates/          # HTML templates
    └── index.html      # Dashboard Interface
```

---

## 🎯 Future Improvements (Optional Ideas)
- Add email preview before sending.
- Schedule email delivery.
- Add more AI personalization options.
- Export email delivery reports.

---

## 📝 License
MIT License

---
