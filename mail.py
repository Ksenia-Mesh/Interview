import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:
    def __init__(self, login, password):
        self.sending = {
                        'login': login,
                        'password': password
                        }

    def send_mail(self, recipients, subject, text_message, server, port):
        try:
            message = MIMEMultipart()
            message['From'] = self.sending['login']
            message['To'] = ', '.join(recipients)
            message['Subject'] = subject
            message.attach(MIMEText(text_message))
            your_date = smtplib.SMTP(server, port)
            your_date.ehlo()
            your_date.starttls()
            your_date.ehlo()
            your_date.login(self.sending['login'], self.sending['password'])
            result = your_date.sendmail(message['From'], message['To'], message.as_string())
            your_date.quit()
            return result
        except Exception as e:
            return f'Failed to send email: {e}'


    def receive_mail(self, server, inbox, header=None):
        receive_mail_ = imaplib.IMAP4_SSL(server)
        try:
            receive_mail_.login(self.send_mail['login'], self.send_mail['password'])
            receive_mail_ = '(HEADER Subject "%s")' % header if header else 'ALL'.list()
            receive_mail_.select(inbox)
            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            result, data = receive_mail_.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            print(latest_email_uid.decode('utf-8'))
            result, data = receive_mail_.uid('fetch', latest_email_uid.decode('utf-8'), '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email.decode('utf-8'))
            receive_mail_.logout()
            return email_message
        except Exception as e:
            return f'Failed to receive email:{e}'



if __name__ == '__main__':
    mail = Mail('login@gmail.com', 'qwerty')
    print(mail.send_mail(
        'smtp.gmail.com',
        587,
        ['smterrrp.gmail.com', 'imhggfap.gmail.com'],
        'Subject',
        'Test message'
    ))
    print(mail.receive_mail('imap.gmail.com', 'inbox'))





