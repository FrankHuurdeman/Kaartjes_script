import folium
from geopy.geocoders import Nominatim

# Functie om de coördinaten op te halen via OSM
def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="osm_map")
    location = geolocator.geocode(city_name)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

# Coördinaten ophalen voor Amersfoort en Potsdam
amersfoort_coords = get_coordinates("Amersfoort, Netherlands")
potsdam_coords = get_coordinates("Potsdam, Germany")
barcelona_coords = get_coordinates("Barcelona, Spain")
orebro_coords = get_coordinates("Orebro, Sweden")
nieuwpoort_coords = get_coordinates("Nieuwpoort, Netherlands")
vienna_coords = get_coordinates("Vienna, Austria")

# Controleer of de coördinaten correct zijn
if amersfoort_coords and potsdam_coords and barcelona_coords:
    print(f"Amersfoort: {amersfoort_coords}")
    print(f"Potsdam: {potsdam_coords}")
    print(f"Barcelona: {barcelona_coords}")
    print(f"Orebro: {orebro_coords}")
    print(f"Vienna: {vienna_coords}")
    print(f"Nieuwpoort: {nieuwpoort_coords}")

    # Maak een folium kaart
    m = folium.Map(location=[52.0907, 13.2395], zoom_start=6)  # Beginlocatie ergens in Europa

    # Voeg markers toe voor Amersfoort en Potsdam
    folium.Marker(amersfoort_coords, popup="Amersfoort").add_to(m)
    folium.Marker(potsdam_coords, popup="Potsdam").add_to(m)
    folium.Marker(barcelona_coords, popup="Barcelona").add_to(m)
    folium.Marker(orebro_coords, popup="Onsliefdesstadje_jwz").add_to(m)
    folium.Marker(nieuwpoort_coords, popup= "Geboortestadje", icon=folium.Icon(color="blue")).add_to(m)
    folium.Marker(vienna_coords, popup= "Wenen", icon=folium.Icon(color="red")).add_to(m)

    # Sla de kaart op als HTML-bestand
    m.save("index.html")
    print("Kaart opgeslagen als 'kaart_met_markers.html'.")
else:
    print("Kon de coördinaten niet ophalen voor een of beide steden.")

print("Git commit test")