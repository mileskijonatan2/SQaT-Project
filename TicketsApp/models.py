from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} - {self.country_code}"


class Airport(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Airline(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date_established = models.DateField()
    num_of_planes = models.IntegerField()

    def __str__(self):
        return f"{self.name} - ({self.country.country_code})"


class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    airline = models.ForeignKey(Airline, related_name='flights', on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(Airport, related_name='departure_flights', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='arrival_flights', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.DurationField(help_text='Duration in hours')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.flight_number} - {self.airline}"


class Seat(models.Model):
    flight = models.ForeignKey(Flight, related_name='seats', on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=8, unique=False)
    CLASS_CHOICES = [
        ('EC', 'Economy'),
        ('BS', 'Business'),
        ('FC', 'First Class'),
    ]
    class_type = models.CharField(max_length=20, choices=CLASS_CHOICES, default='EC')
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Seat {self.seat_number} ({self.class_type}) on {self.flight.flight_number}"


class Booking(models.Model):
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, related_name='bookings', on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, related_name='booking', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking for {self.user.username} - {self.flight.flight_number}"


class Passenger(models.Model):
    booking = models.ForeignKey(Booking, related_name='passengers', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    country_of_residence = models.ForeignKey(Country, related_name='citizens', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.passport_number})"
