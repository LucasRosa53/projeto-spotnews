from django.core.exceptions import ValidationError


def validator_words(words):
    if len(words.split()) < 2:
        raise ValidationError('O título deve conter pelo menos 2 palavras.')