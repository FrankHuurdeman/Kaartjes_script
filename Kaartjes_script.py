# Importeren benodigde packages

print("Script is begonnen met draaien")

import folium
from geopy.geocoders import Nominatim
import time
import wikipediaapi

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

#Schrijven van functie voor het ophalen van de wikipedia gegevens
def get_wikipedia_info(city):
    wiki = wikipediaapi.Wikipedia(language='nl', user_agent="Project_kaartje_maken_met_wiki_info")
    page = wiki.page(city)
    if page.exists():
        return page.summary
    else:
        return "Geen recente info beschikbaar"


locations_list = [
    ("Amersfoort", "Netherlands"),
    ("Nieuwpoort", "Netherlands"),
    ("Rotterdam", "Netherlands"),
    ("Maastricht", "Netherlands"),
    ("Leeuwarden", "Netherlands"),
    ("Amsterdam", "Netherlands"),
    ("Utrecht", "Netherlands"),
    ("Zwolle", "Netherlands"),
    ("Den Haag", "Netherlands"),
    ("Hilversum", "Netherlands"),

    ("Potsdam", "Germany"),
    ("Hamburg", "Germany"),
    ("Berlijn", "Germany"),
    ("Leipzig", "Germany"),
    ("Osnabruck", "Germany"),
    ("Dusseldorf", "Germany"),
    ("Stuttgart", "Germany"),
    ("Ludwigsburg", "Germany"),
    ("Frankfurt", "Germany"),
    ("Uberlingen", "Germany"),
    ("Hannover", "Germany"),
    ("Esslingen", "Germany"),
    ("Trier", "Germany"),
    ("Bremen", "Germany"),

    ("Brugge", "Belgium"),
    ("Antwerpen", "Belgium"),
    ("La Roche-en-Ardenne", "Belgium"),
    ("Bouillon", "Belgium"),

    ("London", "England"),

    ("Paris", "France"),
    ("Avignon", "France"),
    ("Troyes", "France"),

    ("Barcelona", "Spain"),

    ("Verona", "Italy"),
    ("Venice", "Italy"),
    ("Feltre", "Italy"),

    ("Interlaken", "Switzerland"),

    ("Zagreb", "Croatia"),
    ("Split", "Croatia"),

    ("Vienna", "Austria"),

    ("Wroclaw", "Poland"),

    ("Prague", "Czech Republic"),

    ("Sami", "Greece"),
    ("Kamari", "Greece"),

    ("Copenhagen", "Denmark"),
    ("Roskilde", "Denmark"),

    ("Malmo", "Sweden"),
    ("Charlottenberg", "Sweden"),
    ("Arvika", "Sweden"),
    ("Karlstad", "Sweden"),
    ("Orebro", "Sweden"),
    ("Stockholm", "Sweden"),
    ("Östersund", "Sweden"),
    ("Gothenburg", "Sweden"),
    ("Storlien", "Sweden"),

    ("Oslo", "Norway"),
    ("Bergen", "Norway"),
    ("Flam", "Norway"),
    ("Lillehammer", "Norway"),
    ("Trondheim", "Norway"),
    ("Narvik", "Norway"),
    ("Svolvaer", "Norway"),
    ("Henningsvaer", "Norway"),
    ("Sydalen", "Norway"),
    ("Leknes", "Norway"),
    ("Reine", "Norway"),
    ("A", "Norway")
]

print("Verwerken in lijst is gelukt")
 
locations_coords = {}

for location, country in locations_list:
    coords = get_coordinates(f"{location}, {country}")
    locations_coords[location] = coords  

print("Ophalen van coordinaten is gelukt")
     
m = folium.Map(location=[52.0907, 13.2395], zoom_start = 3)

for location, coords in locations_coords.items():
    info = get_wikipedia_info(location)
    folium.Marker(
        location = coords, 
        popup=folium.Popup(info, max_width=300),
        tooltip=location
        ).add_to(m)

m.save(r"Kaartjes_script\index.html")
print("Kaart opgeslagen als 'index.html' lets go.")