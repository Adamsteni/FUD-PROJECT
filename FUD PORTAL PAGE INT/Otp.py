from flask import Flask, render_template, request, redirect, url_for, session, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# Initialize Flask app and set template folder to the current directory
app = Flask(__name__, template_folder='.')
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'kingteni3000@gmail.com'  # Replace with your email address
EMAIL_PASSWORD = 'kpnn mapv rwla keqj'  # Replace with your email password or app password

# Helper function to generate OTP
def generate_otp():
    return str(random.randint(100000, 999999))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Redirect to the login page when the form is submitted
        return redirect(url_for('login'))
    return render_template('index.html')  # Render the index page when accessed

 

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        user_otp = request.form.get('otp')  # Get the OTP entered by the user
        if user_otp == session.get('otp'):  # Check if the OTP matches
            flash('Email verified successfully!')
            # Clear session data after successful verification
            session.pop('otp', None)
            session.pop('email', None)
            return redirect(url_for('successful'))  # Redirect to the index page after verification
        else:
            flash('Invalid OTP. Please try again.')
    return render_template('verify.html')

@app.route('/successful', methods=['GET'])
def successful():
    return render_template('successful.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
@app.context_processor
def inject_base_url():
 return {'base_url': '' if app.debug else '/your-netlify-path'}

