from django.urls import path # type: ignore
from . import views

urlpatterns = [
    # Other URL patterns...
    path('flight/<int:flight_id>/', views.flight_details, name='flight_details'),
]