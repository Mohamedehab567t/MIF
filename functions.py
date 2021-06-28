from wtforms.validators import ValidationError
from DB import Student

def validate_email(self , email):
    user = Student.find_one({'email': email.data})
    if not user:
        raise ValidationError('No user with these email')


def calcAgree(vote):
    var = 0
    if vote['state'] == 'agree':
        var = var +1
    return var

def calcDisAgree(vote):
    num = 0
    if vote['state'] == 'disagree':
        num = num +1
    return num