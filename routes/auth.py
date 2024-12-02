from utils.email_utils import send_password_reset_email

def login(email, password):
    print(f"Logging in user: {email}")
    return "Login successful"

def reset_password(email):
    send_password_reset_email(email)
    print(f"Password reset link sent to {email}")

