from django.core.validators import ValidationError
import re


def validate_alpha_numeric(value):
    if not re.compile(r'^[0-9a-zA-ZäåöüÄÅÖÜ]*$').match(value):
        raise ValidationError(
            'Sorry, this field must only contain numbers and letters!')
    return value


def validate_phone_number(value):
    if not re.compile(r'^[+0-9]*$').match(value):
        raise ValidationError(
            'Sorry, your phone number can only contain numbers and a plus!')
    return value


def validate_postal_code(value):
    if not re.compile(r'^[0-9]*$').match(value):
        raise ValidationError(
            'Sorry, the postal code must only contain numbers!.')
    return value


def validate_city(value):
    if not re.compile(r'^[ a-zA-ZäåöüÄÅÖÜ]*$').match(value):
        raise ValidationError(
            'Sorry, the city must only contain letters!')
    return value


def validate_name(value):
    if not re.compile(r'^[ a-zA-ZäåöüÄÅÖÜ]*$').match(value):
        raise ValidationError('Sorry, your name must only contain letters!')
    return value


def validate_county(value):
    if not re.compile(r'^[ a-zA-ZäåöüÄÅÖÜ]*$').match(value):
        raise ValidationError('Sorry, the county must only contain letters!')
    return value


def validate_country(value):
    if not re.compile(r'^[ a-zA-ZäåöüÄÅÖÜ]*$').match(value):
        raise ValidationError('Sorry, the country must only contain letters!')
    return value
