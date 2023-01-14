from django.urls import path
from .views import PropertyListCreateAPIView,PropertyRetrieveUpdateAPIView,CityListAPIView

urlpatterns = [
    path('property/',PropertyListCreateAPIView.as_view()),
    path('property/<int:pk>/',PropertyRetrieveUpdateAPIView.as_view()),
    path('city/',CityListAPIView.as_view())
]
