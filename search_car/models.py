from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def default_location():
    """Выбирает локацию по умолчанию"""
    return Location.objects.all().order_by('?')[0]


class Location(models.Model):
    city = models.CharField(max_length=150, verbose_name='город')
    state = models.CharField(max_length=150, verbose_name='штат')
    zip = models.PositiveIntegerField(verbose_name='индекс')
    width = models.FloatField(verbose_name='широта')
    longitude = models.FloatField(verbose_name='долгота')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.city


class Car(models.Model):
    number = models.CharField(max_length=5, unique=True, verbose_name='номер машины')
    location = models.ForeignKey('search_car.Location', default=default_location,
                                 on_delete=models.CASCADE, related_name='car_location', verbose_name='текущая локация')
    tonnage = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)],
                                  verbose_name='грузоподъемность')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.number


class Cargo(models.Model):
    pick_up = models.ForeignKey('search_car.Location', on_delete=models.CASCADE, related_name='cargo_pick_up',
                                verbose_name='отправка из', )
    delivery = models.ForeignKey('search_car.Location', on_delete=models.CASCADE, related_name='cargo_delivery',
                                 verbose_name='отправка в')
    weight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)],
                                 verbose_name='вес')
    description = models.CharField(max_length=150, verbose_name='описание')

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'

    def __str__(self):
        return self.description
