from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def phone_number_validator(phone_no):
    if phone_no:
        if len(phone_no) != 10:
            return "not valid"

        if phone_no[:2] != '98' :
            # raise ValidationError("Phone number is invalid.")
            return "not valid"
    return phone_no


def is_alphabetic(value):
    if not value.isalpha():
        raise ValidationError("The value should be alphabetic.")
    return value

def name_validator(value):
    if value:
        if not value.replace(' ', '').replace("'", "").isalpha():
            raise ValidationError("The value should be alphabetic.")
    return value.strip()


def is_alphabetic_with_space(value):
    if not value.replace(" ", "").isalpha():
        raise ValidationError("The value should be alphabetic.")
    return value.strip()


def is_numeric_value(value):
    if value:
        if not value.isnumeric():
            raise ValidationError(_("%(value)s: The value should be numeric."),params={'value': value})
    return value

def image_validator(image):
    if image.file.size > 8 * 1024 * 512:
        raise ValidationError("Image size should be less than 1.5 MB.")
    return image