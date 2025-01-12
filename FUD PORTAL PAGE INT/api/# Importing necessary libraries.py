# Importing necessary libraries
import pyotp  # This library helps to verify time-based OTP (TOTP)
import smtplib  # This is used to send emails involving the SMTP protocol
from email.mime.text import MIMEText  # For creating the email body
from email.mime.multipart import MIMEMultipart  # For creating a multi-part email
from twilio.rest import Client  # For sending SMS through the Twilio API

# Generate (new users) or retrieve (old users) the secret key
secretkey = pyotp.random_base32()  # Generates a unique 32-character secret key

# Generate the TOTP code
totp = pyotp.TOTP(secretkey)  # Creates a TOTP object using the secret key
current_code = totp.now()  # Generates the TOTP code, which changes every 30 seconds

# Prompt the user to choose how they want to receive their MFA code (SMS or email)
send_via = input("Would you like to receive your code via 'Email' or 'SMS'? ").strip().lower()

# Function to send email
def send_email(recipient_email, subject, body):
    sender_email = "kingteni3000@gmail.com"  # Replace with your actual email address
    sender_password = "djgv evxo anyp ozav"  # Replace with your actual email password or use your Mail Providers App Password

    msg = MIMEMultipart()  # Creates a MIMEMultipart object for the email
    msg['From'] = sender_email  # Sets the sender of the email
    msg['To'] = recipient_email  # Sets the recipient of the email
    msg['Subject'] = subject  # Sets the subject of the email

    msg.attach(MIMEText(body, 'plain'))  # Attaches the email body as plain text

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Connects to Gmail's SMTP server
        server.starttls()  # Secures the connection with TLS
        server.login(sender_email, sender_password)  # Logs into the email account
        server.sendmail(sender_email, recipient_email, msg.as_string())  # Sends the email
        server.quit()  # Closes the SMTP server connection
        print("Email sent successfully.")
    except Exception as ex:
        print(f"Failed to send email: {ex}")  # Prints any exception that occurs

# Function to send SMS
def send_sms(to_phone_number, body):
    account_sid = 'your_account_sid'  # Replace with your Twilio account SID
    auth_token = 'your_auth_token'  # Replace with your Twilio auth token
    twilio_phone_number = '+1234567890'  # Replace with your Twilio phone number

    client = Client(account_sid, auth_token)  # Creates a Twilio client object

    try:
        message = client.messages.create(
            body=body,
            from_=twilio_phone_number,
            to=to_phone_number
        )
        print(f"SMS successfully sent: {message.sid}")
    except Exception as ex:
        print(f"Failed to send SMS: {ex}")  # Prints any exception that occurs

# Process the user's choice for receiving the OTP
if send_via == 'email':
    recipient_email = input("Enter your email address: ")
    subject = "Your OTP Code"
    body = f"Your OTP Code is: {current_code}"
    send_email(recipient_email, subject, body)
elif send_via == 'sms':
    to_phone_number = input("Enter your phone number (e.g., +2348076452022): ")
    sms_body = f"Your OTP Code is: {current_code}"
    send_sms(to_phone_number, sms_body)
else:
    print("Invalid option. Please choose either 'email' or 'sms'.")

# Ask the user to provide the received OTP code
user_input = input("Enter the OTP code: ")

# Verify the OTP code provided by the user
otp = pyotp.TOTP('base32secret3232')
user_otp = input("Enter OTP: ")
if otp.verify(user_otp):
    print("OTP is Valid!")
else:
    print("invalid OTP Code. Try again.")


