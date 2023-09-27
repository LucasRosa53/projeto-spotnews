from django.core.exceptions import ValidationError


def validator(words):
    if len(words.split()) < 1:
        raise ValidationError('O título deve conter pelo menos 2 palavras.')