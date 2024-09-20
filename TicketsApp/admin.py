from django.contrib import admin
from django import forms
from .models import Country, Airport, Airline, Seat, Passenger, Flight, Booking


class FlightAdminForm(forms.ModelForm):
    number_of_seats = forms.IntegerField(label="Number of Seats", required=True, min_value=3)

    class Meta:
        model = Flight
        fields = '__all__'


class FlightAdmin(admin.ModelAdmin):
    form = FlightAdminForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        number_of_seats = form.cleaned_data.get('number_of_seats')
        seat_prefix = ['A', 'B', 'C', 'D', 'E', 'F']

        for i in range(number_of_seats):
            seat_number = f"{seat_prefix[i % len(seat_prefix)]}{i+1}"
            seat_type = 'EC'
            additional_payment = float(obj.price) * 0.2
            if i / number_of_seats <= 0.2:
                seat_type = 'FC'
                additional_payment = float(obj.price) * 0.9
            elif i / number_of_seats <= 0.4:
                seat_type = 'BS'
                additional_payment = float(obj.price) * 0.7
            Seat.objects.create(seat_number=seat_number, flight=obj, class_type=seat_type, is_available=True, price=obj.price+int(additional_payment))

        self.message_user(request, f"{number_of_seats} seats created successfully for {obj.flight_number}.")


admin.site.register(Flight, FlightAdmin)
admin.site.register(Country)
admin.site.register(Airport)
admin.site.register(Airline)
admin.site.register(Seat)
admin.site.register(Passenger)
admin.site.register(Booking)
