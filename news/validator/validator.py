from django.core.exceptions import ValidationError


def validator(words):
    if len(words.split()) < 2:
        raise ValidationError('O título deve conter pelo menos 2 palavras.')