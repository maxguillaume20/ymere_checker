import smtplib
from email.message import EmailMessage


class Notifier(object):

    gmail_user = 'margaxs.rental.notifier@gmail.com'
    gmail_password = '8K4JwyG6sG6NmMy'

    def __init__(self, recipients):
        self.recipients = recipients

    def send_email(self, subject, content):
        msg = EmailMessage()
        msg.set_content(content)
        msg['Subject'] = subject
        msg['From'] = Notifier.gmail_user
        msg['To'] = ','.join(self.recipients)
        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(Notifier.gmail_user, Notifier.gmail_password)
            smtp_server.send_message(msg)
            smtp_server.close()
            print("Email sent successfully!")
        except Exception as ex:
            print("Something went wrong….", ex)

