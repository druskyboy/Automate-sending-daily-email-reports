import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Email configuration
SENDER_EMAIL = "youremail@example.com"
SENDER_PASSWORD = "yourpassword"  # Use app-specific password for Gmail
RECEIVER_EMAIL = "receiver@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_email(subject, body, attachment_path=None):
    try:
        # Set up the MIME
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Attachment (if any)
        if attachment_path and os.path.exists(attachment_path):
            attachment = open(attachment_path, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
            msg.attach(part)

        # Connect to the server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Enable security
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Define your report details
subject = "Daily Report"
body = "Please find the attached daily report."
attachment_path = "path/to/report.pdf"  # Change to your file path

# Call the function
send_email(subject, body, attachment_path)
