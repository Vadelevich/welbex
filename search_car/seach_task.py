from geopy import distance
from rest_framework.generics import get_object_or_404

from search_car.models import Cargo, Car


def search(cargo_pk):
    """Рассчитывает расстояние от начала груза до машины  """
    cargo_items = get_object_or_404(Cargo, pk=cargo_pk)
    start_point_w = cargo_items.pick_up.width  # начальная ширина поиска
    start_point_l = cargo_items.pick_up.longitude  # начальная долгота поиска
    answer = {}
    cars = Car.objects.all()
    first_car = (cars.first().location.width, cars.first().location.longitude)
    start = (start_point_w, start_point_l)
    min_distance = distance.distance(start, first_car).miles
    for car in cars:
        local_car = (car.location.width, car.location.longitude)  # Координаты машины
        res = distance.distance(start, local_car).miles  # Расчет расстояния

        if min_distance >= res and car.tonnage >= cargo_items.weight:
            answer['number'] = car.number
            answer['tonnage'] = car.tonnage
            answer['city'] = car.location.city
            answer['distance'] = min_distance
            min_distance = res

    return answer


def search_to_miles(instance):
    """Возвращает ближайшие машины до груза ( =< 450 миль)"""
    instance.count = {}
    start_point_w = instance.pick_up.width
    start_point_l = instance.pick_up.longitude
    cars = Car.objects.all()
    start = (start_point_w, start_point_l)
    for car in cars:
        local_car = (car.location.width, car.location.longitude)  # Координаты машины
        res = distance.distance(start, local_car).miles
        if res <= 450:
            instance.count['number'] = car.number
            instance.count['distance'] = res

    return instance.count


def search_delivery(instance):
    """ Возвращает  список номеров ВСЕХ машин с расстоянием до выбранного груза"""
    instance.number = {}
    start_point_w = instance.pick_up.width
    start_point_l = instance.pick_up.longitude
    end_point_w = instance.delivery.width
    end_point_l = instance.delivery.longitude
    cars = Car.objects.all()
    start = (start_point_w, start_point_l)
    end = (end_point_w, end_point_l)
    end_search = distance.distance(start, end).miles

    for car in cars:
        local_car = (car.location.width, car.location.longitude)  # Координаты машины
        res = distance.distance(start, local_car).miles
        if res <= end_search:
            instance.number['number'] = car.number
    return instance.number
