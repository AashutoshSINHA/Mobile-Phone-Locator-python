import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import  geocoder
from phonenumbers import timezone

numbers = input( "Your Mobile Phone Number: ")
numbers = ph.parse(numbers)
print(timezone.time_zones_for_number(numbers))
print(carrier.name_for_number(numbers, "en"))
print(geocoder.description_for_number(numbers, "en"))
print("Thank You So Much For choosing Us:❤️")