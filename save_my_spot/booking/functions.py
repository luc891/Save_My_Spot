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
    
def get_password_error_message(error_code):
    if error_code == 'Your passwords do not match':
        return 'Your passwords do not match'
    elif error_code == 'password_too_short':
        return 'Password is too short'
    elif error_code == 'password_too_common':
        return 'Password is too obvious'
    else:
        return 'Erreur de mot de passe.'
    