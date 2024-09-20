from datetime import datetime
from django.shortcuts import render
from .models import Flight
from .forms import FlightSearchForm


def searchFlights(request):
    form = FlightSearchForm()
    flights = None

    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            departure_country = form.cleaned_data['departure_country']
            arrival_country = form.cleaned_data['arrival_country']
            date = form.cleaned_data['date']
            all_flights = list()

            if date is not None:
                all_flights = Flight.objects.filter(departure_time__date=date)
            else:
                all_flights = Flight.objects.filter(departure_time__gte=datetime.now())  # show all flights whose dep time is after now

            flights = list()
            for i in range(all_flights.count()):
                if all_flights[i].departure_airport.country == departure_country and all_flights[i].arrival_airport.country == arrival_country:
                    flights.append(all_flights[i])

    return render(request, 'searchFlights.html', {'form': form, 'flights': flights})
