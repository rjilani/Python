__author__ = 'rjilani'

from geopy.geocoders import Nominatim
from geopy.distance import vincenty

geolocator = Nominatim()

location = geolocator.geocode("9611 custer Rd Plano tx 75025")

print(location.address)

print((location.latitude, location.longitude))

print(location.raw)

location = geolocator.reverse("33.0717368, -96.7369165")

print(location.address)

newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(vincenty(newport_ri, cleveland_oh).miles)

