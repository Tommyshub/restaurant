from django.core.validators import ValidationError
import re


def validate_alpha_numeric(value):
    if not re.compile(r'^[ 0-9a-zA-ZäåöüÄÅÖÜ]*$').match(value):
        raise ValidationError(
            'Sorry, this field can only contain numbers and letters!')
    return value


def validate_phone_number(value):
    if not re.compile(r'^[+0-9]*$').match(value):
        raise ValidationError(
            'Sorry, your phone number can only contain numbers and a plus!')
    return value


def validate_postal_code(value):
    if not re.compile(r'^[0-9]*$').match(value):
        raise ValidationError(
            'Sorry, the postal code can only contain numbers!.')
    return value


def validate_city(value):
    if not re.compile(r'^[ a-zA-ZäåöüÄÅÖÜ]*$').match(value):
        raise ValidationError(
            'Sorry, the city can only contain letters!')
    return value


def validate_name(value):
    if not re.compile(r'^[ a-zA-ZäåöüÄÅÖÜ]*$').match(value):
        raise ValidationError('Sorry, your name can only contain letters!')
    return value


def validate_county(value):
    if not re.compile(r'^[ a-zA-ZäåöüÄÅÖÜ]*$').match(value):
        raise ValidationError('Sorry, the county can only contain letters!')
    return value


def validate_country(value):
    if not re.compile(r'^[ a-zA-ZäåöüÄÅÖÜ]*$').match(value):
        raise ValidationError('Sorry, the country can only contain letters!')
    return value
