from rest_framework import status, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, get_object_or_404, \
    DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from search_car.models import Car, Cargo, Location
from search_car.serializers import CarSerializer, CargoSerializer, CargoListSerializer, CargoRetrieveSerializer, \
    CarUpdateSerializer
from search_car.seach_task import search


class CarCreateAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarListAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarUpdateAPIView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarUpdateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = {
            "number": request.data.get('number', None),
            "tonnage": request.data.get('tonnage', None),
            "location": request.data.get('location', None),
        }
        new_loc = get_object_or_404(Location, zip=data['location'])
        data['location'] = new_loc.pk
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class SearchCarAPIView(APIView):

    def get(self, *args, **kwargs):
        cargo_pk = kwargs.get('pk')
        result = search(cargo_pk)
        return Response(result)


class CargoCreateAPIView(CreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def create(self, request, *args, **kwargs):
        data = {
            "pick_up": request.data.get('pick_up', None),
            "delivery": request.data.get('delivery', None),
            "weight": request.data.get('weight', None),
            "description": request.data.get('description', None),

        }

        new_pick = get_object_or_404(Location, zip=data['pick_up'])
        data['pick_up'] = new_pick.pk
        new_del = get_object_or_404(Location, zip=data['delivery'])
        data['delivery'] = new_del.pk

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CargoListAPIView(ListAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['weight', ]


class CargoRetrieveAPIView(RetrieveAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoRetrieveSerializer


class CargoUpdateAPIView(UpdateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = {
            "pick_up": request.data.get('pick_up', None),
            "delivery": request.data.get('delivery', None),
            "weight": request.data.get('weight', None),
            "description": request.data.get('description', None),

        }
        new_pick = get_object_or_404(Location, zip=data['pick_up'])
        data['pick_up'] = new_pick.pk
        new_del = get_object_or_404(Location, zip=data['delivery'])
        data['delivery'] = new_del.pk
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class CargoDestroyAPIView(DestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
