from django.core.exceptions import ValidationError
import re 

def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_val):
    add_attr(field,'placeholder', placeholder_val)

# defenir os characters a ser usados na pw!
def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(
            'Password must have at least one uppercase letter,'
            'one lowercase letter and one number. Have length should be'
            'at least 8 characters'
        )
code='invalid'

    # defenir os characters a ser usados na pw!
def admin_regex(input):
    regex = re.compile(r'^[a-zA-Z0-9\s]+$')

    if not regex.match(input):
        raise ValidationError(
            'The description must start with an uppercase letter and may contain lowercase letters,'
            'numbers, and spaces. It should not contain special characters like <> !#$, and so on.'
        )
code='invalid'

description = "<<>"
try:
    admin_regex(description)
    print("Descrição válida!")
except ValidationError as e:
    print(e)