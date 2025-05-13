import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_massage(email, massage):
    sender_email = "elchintoyirov@gmail.com"
    password = "ywyr kvgq yocc krrt"

    subject = "Test Email"
    receiver_email = email
    body = massage

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")
