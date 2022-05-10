from smtplib import SMTP
from ..config import Config

sender_email = Config.EMAIL
password = Config.PASSWORD
domain = Config.SMPT_NAME

def send_email(username, useremail):
    receiver = useremail
    message = f"Welcome to CrowdPitch, {username.title()}. "
    subject = "Welcome"
    with SMTP(domain) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver,
            msg=f"Subject:{subject}\n\n{message}"
        )


send_email('Samuel', 'femap30501@eoscast.com')
