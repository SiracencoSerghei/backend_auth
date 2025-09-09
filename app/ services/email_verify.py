import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")


def send_verification_email(to_email: str, token: str):
    verify_url = f"http://localhost:8000/verify?token={token}"
    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=to_email,
        subject="Підтвердження email",
        html_content=f"""
        <h2>Вітаємо!</h2>
        <p>Будь ласка, підтвердіть свій акаунт, перейшовши за цим посиланням:</p>
        <a href="{verify_url}">{verify_url}</a>
        """,
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
    except Exception as e:
        print(f"SendGrid error: {e}")
