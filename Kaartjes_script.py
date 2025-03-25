# Importeren benodigde packages

import folium
from geopy.geocoders import Nominatim
import time

# Schrijven functie voor het ophalen van de OSM gegeven
def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="osm_map", timeout=5)

    try:
        location = geolocator.geocode(city_name)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except GeocoderTimedOut:
        print(f"Timeout bij ophalen van: {city_name}, opnieuw proberen...")
        time.sleep(2)  
        return get_coordinates(city_name)  

# Coördinaten ophalen voor de reislocaties Nederland
amersfoort_coords = get_coordinates("Amersfoort, Netherlands")
nieuwpoort_coords = get_coordinates("Nieuwpoort, Netherlands")
rotterdam_coords = get_coordinates("Rotterdam, Netherlands")
maastricht_coords = get_coordinates("Maastricht, Netherlands")
leeuwarden_coords = get_coordinates("Leeuwarden, Netherlands")
amsterdam_coords = get_coordinates("Amsterdam, Netherlands")
utrecht_coords = get_coordinates("Utrecht, Netherlands")
zwolle_coords = get_coordinates("Zwolle, Netherlands")
denhaag_coords = get_coordinates("Den Haag, Netherlands")
hilversum_coords = get_coordinates("Hilversum, Netherlands")

# Coordinaten ophalen voor de reislocaties van Duitsland
potsdam_coords = get_coordinates("Potsdam, Germany")
hamburg_coords = get_coordinates("Hamburg, Germany")
berlijn_coords = get_coordinates("Berlin, Germany")
leipzig_coords = get_coordinates("Leipzig, Germany")
osnabruck_coords = get_coordinates("Osnabruck, Germany")
dusseldorf_coords = get_coordinates("Dusseldorf, Germany")
stuttgart_coords = get_coordinates("Stuttgart, Germany")
ludwigsburg_coords = get_coordinates("Ludwigsburg, Germany")
frankfurt_coords = get_coordinates("Frankfurt, Germany")
uberlingen_coords = get_coordinates("Uberlingen, Germany")
hannover_coords = get_coordinates("Hannover, Germany")
esslingen_coords = get_coordinates("Esslingen, Germany")
trier_coords = get_coordinates("Trier, Germany")
bremen_coords = get_coordinates("Bremen, Germany")

# Coordinaten ophalen voor reislocaties van Frankrijk
parijs_coords = get_coordinates("Paris, France")
avignon_coords = get_coordinates("Avignon, France")

# Coordinaten ophalen voor reislocaties van Spanje
barcelona_coords = get_coordinates("Barcelona, Spain")

# Coordinaten ophalen voor reislocaties van Italie
verona_coords = get_coordinates("Verona, Italy")
venice_coords = get_coordinates("Verince, Italy")
feltre_coords = get_coordinates("Feltre, Italy")

# Coordinate ophalen voor reislocaties van Zwitserland
interlaken_coords = get_coordinates("Interlaken, Suiss")

# Coordinaten ophalen voor reislocaties van Kroatie
zagreb_coords = get_coordinates("Zagreb, Croatia")
split_coords = get_coordinates("Split, Croatia")

# Coordinaten ophalen voor reislocaties van Oostenrijk
vienna_coords = get_coordinates("Vienna, Austria")

# Coordinaten ophalen voor reislocaties van Denemarken
kopenhagen_coords = get_coordinates("Copenhagen, Denmark")
roskilde_coords = get_coordinates("Roskilde, Denmark")

# Coordinaten

orebro_coords = get_coordinates("Orebro, Sweden")
stockholm_coords = get_coordinates("Stockholm, Sweden")
narvik_coords = get_coordinates("Narvik, Norway")
ostersund_coords = get_coordinates("Östersund, Sweden")
trondheim_coords = get_coordinates("Trondheim, Norway")
lillehammer_coords = get_coordinates("Lillehammer, Norway")
goteborg_coords = get_coordinates("Gothenburg, Sweden")

    # Maak een folium kaart
m = folium.Map(location=[52.0907, 13.2395], zoom_start=6)  # Beginlocatie ergens in Europa

locations = {
    "Amersfoort": amersfoort_coords,
    "Nieuwpoort": nieuwpoort_coords,
    "Rotterdam": rotterdam_coords,
    "Maastricht": maastricht_coords,
    "Leeuwarden": leeuwarden_coords,
    "Amsterdam": amsterdam_coords,
    "Utrecht": utrecht_coords,
    "Zwolle": zwolle_coords,
    "Den Haag": denhaag_coords,
    "Potsdam": potsdam_coords,
    "Hamburg": hamburg_coords,
    "Berlijn": berlijn_coords,
    "Leipzig": leipzig_coords,
    "Osnabruck": osnabruck_coords,
    "Dusseldorf": dusseldorf_coords,
    "Stuttgart": stuttgart_coords,
    "Ludwigsburg": ludwigsburg_coords,
    "Frankfurt": frankfurt_coords,
    "Uberlingen": uberlingen_coords,
    "Barcelona": barcelona_coords,
    "Orebro": orebro_coords,
    "Vienna": vienna_coords,
    "Bremen": bremen_coords,
    "Kopenhagen": kopenhagen_coords,
    "Stockholm": stockholm_coords,
    "Narvik": narvik_coords,
    "Östersund": ostersund_coords,
    "Trondheim": trondheim_coords,
    "Lillehammer": lillehammer_coords,
    "Gothenburg": goteborg_coords,
    "Hannover": hannover_coords,
    "Esslingen": esslingen_coords,
    "Trier": trier_coords,
    "Parijs": parijs_coords,
    "Avignon": avignon_coords,
    "Hilversum": hilversum_coords
}

for city, coords in locations.items():
    folium.Marker(coords, popup=city).add_to(m)

m.save(r"Kaartjes_script\index.html")
print("Kaart opgeslagen als 'index.html'.")