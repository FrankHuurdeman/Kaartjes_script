import folium
from geopy.geocoders import Nominatim

# Functie om de coördinaten op te halen via OSM
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="osm_map", timeout=5)  # Timeout toegevoegd

    try:
        location = geolocator.geocode(city_name)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except GeocoderTimedOut:
        print(f"Timeout bij ophalen van: {city_name}, opnieuw proberen...")
        time.sleep(2)  # Wacht 2 seconden en probeer opnieuw
        return get_coordinates(city_name)  # Herhaal de aanvraag

# Coördinaten ophalen voor de reislocaties
amersfoort_coords = get_coordinates("Amersfoort, Netherlands")
potsdam_coords = get_coordinates("Potsdam, Germany")
barcelona_coords = get_coordinates("Barcelona, Spain")
orebro_coords = get_coordinates("Orebro, Sweden")
nieuwpoort_coords = get_coordinates("Nieuwpoort, Netherlands")
vienna_coords = get_coordinates("Vienna, Austria")
rotterdam_coords = get_coordinates("Rotterdam, Netherlands")
maastricht_coords = get_coordinates("Maastricht, Netherlands")
hamburg_coords = get_coordinates("Hamburg, Germany")
bremen_coords = get_coordinates("Bremen, Germany")
kopenhagen_coords = get_coordinates("Copenhagen, Denmark")
stockholm_coords = get_coordinates("Stockholm, Sweden")
narvik_coords = get_coordinates("Narvik, Norway")
ostersund_coords = get_coordinates("Östersund, Sweden")
trondheim_coords = get_coordinates("Trondheim, Norway")
lillehammer_coords = get_coordinates("Lillehammer, Norway")
goteborg_coords = get_coordinates("Gothenburg, Sweden")

# Controleer of de coördinaten correct zijn
if all([
    amersfoort_coords, potsdam_coords, barcelona_coords, orebro_coords, nieuwpoort_coords, vienna_coords,
    rotterdam_coords, maastricht_coords, hamburg_coords, bremen_coords, kopenhagen_coords, stockholm_coords,
    narvik_coords, ostersund_coords, trondheim_coords, lillehammer_coords, goteborg_coords
]):
    print(f"Amersfoort: {amersfoort_coords}")
    print(f"Potsdam: {potsdam_coords}")
    print(f"Barcelona: {barcelona_coords}")
    print(f"Orebro: {orebro_coords}")
    print(f"Vienna: {vienna_coords}")
    print(f"Nieuwpoort: {nieuwpoort_coords}")
    print(f"Rotterdam: {rotterdam_coords}")
    print(f"Maastricht: {maastricht_coords}")
    print(f"Hamburg: {hamburg_coords}")
    print(f"Bremen: {bremen_coords}")
    print(f"Kopenhagen: {kopenhagen_coords}")
    print(f"Stockholm: {stockholm_coords}")
    print(f"Narvik: {narvik_coords}")
    print(f"Östersund: {ostersund_coords}")
    print(f"Trondheim: {trondheim_coords}")
    print(f"Lillehammer: {lillehammer_coords}")
    print(f"Göteborg: {goteborg_coords}")

    # Maak een folium kaart
    m = folium.Map(location=[52.0907, 13.2395], zoom_start=6)  # Beginlocatie ergens in Europa

    # Voeg markers toe voor alle reislocaties
    folium.Marker(amersfoort_coords, popup="Amersfoort").add_to(m)
    folium.Marker(potsdam_coords, popup="Potsdam").add_to(m)
    folium.Marker(barcelona_coords, popup="Barcelona").add_to(m)
    folium.Marker(orebro_coords, popup="Onsliefdesstadje_jwz").add_to(m)
    folium.Marker(nieuwpoort_coords, popup= "Geboortestadje", icon=folium.Icon(color="blue")).add_to(m)
    folium.Marker(vienna_coords, popup= "Wenen", icon=folium.Icon(color="red")).add_to(m)
    folium.Marker(rotterdam_coords, popup="Rotterdam").add_to(m)
    folium.Marker(maastricht_coords, popup="Maastricht").add_to(m)
    folium.Marker(hamburg_coords, popup="Hamburg").add_to(m)
    folium.Marker(bremen_coords, popup="Bremen").add_to(m)
    folium.Marker(kopenhagen_coords, popup="Kopenhagen").add_to(m)
    folium.Marker(stockholm_coords, popup="Stockholm").add_to(m)
    folium.Marker(narvik_coords, popup="Narvik").add_to(m)
    folium.Marker(ostersund_coords, popup="Östersund").add_to(m)
    folium.Marker(trondheim_coords, popup="Trondheim").add_to(m)
    folium.Marker(lillehammer_coords, popup="Lillehammer").add_to(m)
    folium.Marker(goteborg_coords, popup="Göteborg").add_to(m)

    # Sla de kaart op als HTML-bestand
    m.save("index.html")
    print("Kaart opgeslagen als 'index.html'.")
else:
    print("Kon de coördinaten niet ophalen voor een of beide steden.")