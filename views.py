from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import Flight # type: ignore

def flight_details(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, 'airplane_flight.html', {'flight': flight})