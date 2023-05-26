from django.urls import path

from search_car.views import CarCreateAPIView, SearchCarAPIView, CargoCreateAPIView, CargoListAPIView, \
    CargoRetrieveAPIView, CarUpdateAPIView, CargoUpdateAPIView, CargoDestroyAPIView, CarListAPIView

urlpatterns = [
    path('create_car/', CarCreateAPIView.as_view()),
    path('update_car/<int:pk>/', CarUpdateAPIView.as_view()),
    path('list_car/', CarListAPIView.as_view()),
    path('api/<int:pk>/', SearchCarAPIView.as_view()),
    path('list_cargo/', CargoListAPIView.as_view()),
    path('create_cargo/', CargoCreateAPIView.as_view()),
    path('detail_cargo/<int:pk>/', CargoRetrieveAPIView.as_view()),
    path('update_cargo/<int:pk>/', CargoUpdateAPIView.as_view()),
    path('delete_cargo/<int:pk>/', CargoDestroyAPIView.as_view()),

]
