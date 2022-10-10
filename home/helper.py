from email import message
from django.utils.text import slugify

#Circular importing is a form of circular dependency that is created with the import statement in Python.
# slug should be unique
#It is a feature of the Pyforest module that allows the user to perform the task without adding libraries to the code snippet as the task of this function is to add those libraries themselves into the code snippet
import string
import random

# random string generator
def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=N))
    return res


def generate_slug(text):
    new_slug = slugify(text)
    from home.models import BlogModel

    if BlogModel.objects.filter(slug=new_slug).first():
        return generate_slug(text + generate_random_string(5))
    return new_slug
from django.conf import settings
from django.core.mail import send_mail
def send_mail_to_user(token, email):
    subject =f"your account needs to be verified"
    message = f"Hi paste the link to verify the account http://127.0.0.1.8000/verify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message,email_from, recipient_list)
    return True