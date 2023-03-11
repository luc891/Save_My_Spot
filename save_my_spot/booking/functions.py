from django import forms
from django.contrib.auth.password_validation import validate_password

def matching_password(self):

    if not self.get('password2'):
        return("You must confirm your password")
    if self.get('password1') != self.get('password2'):
        return("Your passwords do not match")

    try:
        validate_password(self.get('password2'))
        return True
    except Exception as e:
        return e.messages[0]
    