from celery import shared_task

from config.celery import app
from search_car.models import default_location, Car


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, change_location, name='add every 10')


@app.task
@shared_task
def change_location():
    data_change = Car.objects.all()
    print(data_change)
    if data_change.exists():
        for data_item in data_change:
            data_item.location = default_location()
            data_item.save()
            print("ok")
