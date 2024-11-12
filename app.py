import os
import pandas as pd
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from groq import Groq  # Import Groq client
from flask_cors import CORS  # Import CORS for cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins
api = Api(app, version="1.0", title="Email Sending API", description="A simple API to send customized emails")
ns = api.namespace("emails", description="Email operations")

# Directly set Gmail credentials and Groq API key for testing
GMAIL_USER = 'pvlsyama@gmail.com'  # Gmail account
GMAIL_PASSWORD = 'sr1_saloastamini@google2'
 # Gmail password (App Password recommended)
GROQ_API_KEY = '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'  # Groq API Key

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Increase file upload size limit
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

# Define models for request body validation in Swagger
upload_model = api.model('Upload', {
    'file': fields.String(description='CSV file to upload', required=True)
})

email_model = api.model('Email', {
    'subject': fields.String(description='Email Subject', required=True),
    'bodyTemplate': fields.String(description='Email Body Template', required=True),
    'prompt': fields.String(description='Prompt for personalization', required=True)
})

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if not file.filename.endswith('.csv'):
            return jsonify({"error": "Only CSV files are allowed"}), 400

        # Log file details
        print(f"Uploading file: {file.filename}")

        # Process the file (save or read it)
        df = pd.read_csv(file)
        print("File content preview:", df.head())  # Print a preview of the file content

        app.config['csv_data'] = df  # Save the data in the app configuration
        return jsonify({"message": "File uploaded successfully", "data": df.to_dict()}), 200
    except Exception as e:
        print(f"Error during file upload: {str(e)}")
        return jsonify({"error": f"Error during upload: {str(e)}"}), 500

@app.route('/send_emails', methods=['POST'])
def send_emails():
    data = request.get_json()
    print("Received JSON data:", data)

    try:
        # Retrieve the CSV data from the uploaded file
        df = app.config.get('csv_data', None)
        if df is None:
            return {"error": "No CSV data found. Please upload a CSV file first."}, 400

        # Setup the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        print("SMTP server connection established.")

        # Iterate over each row in the CSV file (each recipient)
        for _, row in df.iterrows():
            try:
                recipient_email = row['email']
                recipient_name = row['name']

                # Customize email body using Groq API for personalization
                prompt = data['prompt'].replace("{name}", recipient_name)
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama3-8b-8192",
                )
                personalized_content = chat_completion.choices[0].message.content

                # Customize email body template with personalized content
                personalized_body = data['bodyTemplate'].replace("{name}", recipient_name).replace("{content}", personalized_content)

                # Create email message
                msg = MIMEMultipart()
                msg['From'] = GMAIL_USER
                msg['To'] = recipient_email
                msg['Subject'] = data['subject']
                msg.attach(MIMEText(personalized_body, 'plain'))

                # Send email
                server.sendmail(GMAIL_USER, recipient_email, msg.as_string())
                print(f"Email sent to {recipient_email}")

            except KeyError as e:
                print(f"Missing field in CSV for {row}: {str(e)}")
            except Exception as e:
                print(f"Error sending email to {recipient_email}: {str(e)}")

        server.quit()
        return {"message": "Emails have been sent successfully."}, 200

    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication error: {str(e)}")
        return {"error": "SMTP Authentication failed. Check email credentials."}, 500
    except smtplib.SMTPException as e:
        print(f"SMTP error: {str(e)}")
        return {"error": f"SMTP error: {str(e)}"}, 500
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return {"error": f"Unexpected error: {str(e)}"}, 500

if __name__ == '__main__':
    app.run(debug=True)
