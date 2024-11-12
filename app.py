import os
import pandas as pd
from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Replace these with your email credentials
GMAIL_USER = 'pvlsyama@gmail.com'
GMAIL_PASSWORD = 'sr1_saloastamini@google2'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        # Read the CSV file
        df = pd.read_csv(file)
        
        # You can check the data (this prints the first 5 rows)
        print(df.head())  # Display the first few rows to confirm the data
        
        # Save the DataFrame to a global variable for later use
        app.config['csv_data'] = df
        
        return jsonify({"message": "File uploaded successfully", "data": df.to_dict()}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/send_emails', methods=['POST'])
def send_emails():
    data = request.get_json()

    if not data or 'subject' not in data or 'bodyTemplate' not in data or 'prompt' not in data:
        return jsonify({"error": "Invalid data received"}), 400

    # Retrieve the CSV data from the uploaded file
    df = app.config.get('csv_data', None)
    if df is None:
        return jsonify({"error": "No CSV data found. Please upload a CSV file first."}), 400

    # Set up the SMTP server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)

        # Iterate over each row in the CSV file (each recipient)
        for _, row in df.iterrows():
            recipient_email = row['email']
            recipient_name = row['name']
            
            # Customize email body
            personalized_body = data['bodyTemplate'].replace("{name}", recipient_name)
            
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = GMAIL_USER
            msg['To'] = recipient_email
            msg['Subject'] = data['subject']

            msg.attach(MIMEText(personalized_body, 'plain'))
            
            try:
                # Send email
                server.sendmail(GMAIL_USER, recipient_email, msg.as_string())
                print(f"Email sent to {recipient_email}")
            except Exception as e:
                print(f"Error sending email to {recipient_email}: {str(e)}")
        
        server.quit()
        return jsonify({"message": "Emails are being sent."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
