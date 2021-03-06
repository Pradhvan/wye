import threading

from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def send_email_to_list(subject, body, users_list, text_body,
                       bcc_admins=True, bcc_managers=False):
    bcc = []
    if bcc_admins:
        bcc += [email for name, email in settings.ADMINS]  # @UnusedVariable

    if bcc_managers:
        bcc += [email for name, email in settings.MANAGERS]  # @UnusedVariable
    from_user = 'PythonExpress <noreply@pythonexpress.in>'
    email = EmailMultiAlternatives(
        subject, text_body, from_user, users_list, bcc)
    email.attach_alternative(body, "text/html")
    EmailThread(email).start()


def send_email_to_id(subject, body, email_id, text_body,
                     bcc_admins=True, bcc_managers=False):
    bcc = []
    if bcc_admins:
        bcc += [email for name, email in settings.ADMINS]  # @UnusedVariable

    if bcc_managers:
        bcc += [email for name, email in settings.MANAGERS]  # @UnusedVariable

    from_user = 'PythonExpress <noreply@pythonexpress.in>'
    email = EmailMultiAlternatives(
        subject, text_body, from_user, [email_id], bcc=bcc)
    email.attach_alternative(body, "text/html")
    EmailThread(email).start()


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.email.send()
        except Exception as e:
            print(e)
