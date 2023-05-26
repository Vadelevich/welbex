import re
from rest_framework import serializers


class ValidateNumber:
    """ Валидация номера (цифра от 1000 до 9999 + случайная заглавная буква английского алфавита в конце)"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if not re.match(r'^[1-9][0-9]{3}[A-Z]+$', value.get('number')):
            raise serializers.ValidationError(
                ' Не правильный формат номера')
