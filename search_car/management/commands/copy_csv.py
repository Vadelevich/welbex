import csv

from django.core.management import BaseCommand

from search_car.models import Location, Car, Cargo

data_csv = []


class Command(BaseCommand):
    """Команда для загрузки тестовых данных"""

    def handle(self, *args, **options):
        with open('uszips.csv') as customers:
            file = csv.DictReader(customers)
            for row in file:
                data_csv.append(
                    {'city': row['city'], 'state': row['state_name'], 'zip': row['zip'], 'width': row['lat'],
                     'longitude': row['lng']})

        location_list = []
        for item in data_csv:
            location_list.append(Location(**item))
        Location.objects.all().delete()
        Location.objects.bulk_create(location_list)

        cars = [
            {'number': '1245W', 'tonnage': '23'},
            {'number': '1245A', 'tonnage': '300'},
            {'number': '1245Q', 'tonnage': '400'},
            {'number': '1245Z', 'tonnage': '500'},
            {'number': '1245X', 'tonnage': '687'},
            {'number': '2245W', 'tonnage': '456'},
            {'number': '1345A', 'tonnage': '589'},
            {'number': '1445Q', 'tonnage': '876'},
            {'number': '5245Z', 'tonnage': '463'},
            {'number': '8245X', 'tonnage': '111'},
            {'number': '2278W', 'tonnage': '456'},
            {'number': '5345Y', 'tonnage': '589'},
            {'number': '1445U', 'tonnage': '876'},
            {'number': '5245I', 'tonnage': '463'},
            {'number': '8245P', 'tonnage': '111'},
            {'number': '2245T', 'tonnage': '456'},
            {'number': '1345B', 'tonnage': '589'},
            {'number': '1445M', 'tonnage': '876'},
            {'number': '5245N', 'tonnage': '463'},
            {'number': '8247L', 'tonnage': '111'},
        ]
        cars_list = []
        for item in cars:
            cars_list.append(Car(**item))

        Car.objects.bulk_create(cars_list)

        cargo = [
            {'pick_up': '99929', 'delivery': '99923', 'weight': '999', 'description': 'very_good', },
            {'pick_up': '24585', 'delivery': '18748', 'weight': '458', 'description': 'very_good', },
            {'pick_up': '30230', 'delivery': '10676', 'weight': '398', 'description': 'very_good', },
            {'pick_up': '32467', 'delivery': '5750', 'weight': '776', 'description': 'very_good', },
            {'pick_up': '27829', 'delivery': '10676', 'weight': '598', 'description': 'very_good', },
            {'pick_up': '373', 'delivery': '15236', 'weight': '297', 'description': 'very_good', },
            {'pick_up': '30530', '8890': '99923', 'weight': '156', 'description': 'very_good', },
        ]
        cargo_list = []
        for item in cargo:
            cargo_list.append(Cargo(**item))

        Cargo.objects.bulk_create(cargo_list)
