# OVerzicht van wat ik in dit script nog wil toevegen/aanpassen/ideetjes
# - Wikipedia DB beter ophalen/betere steden
# - Aanpassen van wat specifiekere stadsnamen zodat wikidb beter werkt
# - Verschilleden soorten markers per gebied
# - Een klein laagje kleur over landen waar markers in staan
# - Fixen van ophalen afbeeldingen
# - Met script app applicatie maken waarmee ik de lijst van plaatsen kan update ipv in het script zelf hard code

# Importeren benodigde packages

print("Script is begonnen met draaien")

import folium
from geopy.geocoders import Nominatim
import time
import wikipediaapi
import wikipedia
import warnings
from urllib.parse import quote

# Opschorten van waarschuwingen voor de wikipedia packages
warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")

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
    wikipedia.set_lang('nl')  # Set the language to Dutch
    try:
        # First use wikipediaapi for summary
        wiki = wikipediaapi.Wikipedia(language='nl', user_agent="Project_kaartje_maken_met_wiki_info")
        page = wiki.page(city)
        
        if page.exists():
            summary = page.summary

            # Now use wikipedia package to get images
            images = wikipedia.page(city).images  # Using wikipedia for image fetching
            return summary, images

        else:
            return "Geen recente info beschikbaar", []

    except wikipedia.exceptions.DisambiguationError as e:
        try:
            new_title = e.options[0]
            print(f"Let op: '{city}' is onduidelijk. Probeer '{new_title}' in plaats daarvan.")
            return get_wikipedia_info(new_title)
        except Exception as e2:
            return "Geen recente info beschikbaar", []

    except wikipedia.exceptions.PageError:
        return "Geen recente info beschikbaar", []

def title_to_commons_url(title):
    # Remove any "Bestand:" or "File:" prefix, which is common for Wikimedia image titles
    filename = title.replace("Bestand:", "").replace("File:", "")
    # URL-encode the filename to handle special characters
    return f"https://commons.wikimedia.org/wiki/Special:FilePath/{quote(filename)}?width=500"


locations_list = [
    ("Amersfoort", "Netherlands"),
    ("Nieuwpoort", "Netherlands"),
    ("Rotterdam", "Netherlands"),
    ("Maastricht", "Netherlands"),
    ("Leeuwarden (stad)", "Netherlands"),
    ("Amsterdam", "Netherlands"),
    ("Utrecht (city)", "Netherlands"),
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
    ("Bremen (stad)", "Germany"),

    ("Brugge", "Belgium"),
    ("Antwerpen", "Belgium"),
    ("La Roche-en-Ardenne", "Belgium"),
    ("Bouillon", "Belgium"),

    ("Londen", "England"),

    ("Paris", "France"),
    ("Avignon", "France"),
    ("Troyes", "France"),

    ("Barcelona", "Spain"),

    ("Verona", "Italy"),
    ("Venice (city)", "Italy"),
    ("Feltre", "Italy"),

    ("Interlaken", "Switzerland"),

    ("Zagreb", "Croatia"),
    ("Split", "Croatia"),

    ("Wenen", "Austria"),

    ("Wroclaw", "Poland"),

    ("Prague (stad)", "Czech Republic"),

    ("Kefalonia", "Greece"),
    ("Santorini", "Greece"),

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
    ("Å", "Norway")
]

print(locations_list)
print("Verwerken in lijst is gelukt")
 
locations_coords = {}

for location, country in locations_list:
    coords = get_coordinates(f"{location}, {country}")
    locations_coords[location] = coords  

print(locations_coords)
print("Ophalen van coordinaten is gelukt")
     
m = folium.Map(location=[52.0907, 13.2395], zoom_start = 3)

for location, coords in locations_coords.items():
    summary, images = get_wikipedia_info(location)  # Unpack the tuple
    
    popup_content = summary
    if images:
        # Add the first image (if any) to the popup
        image_url = title_to_commons_url(images[0])  # Using the first image
        popup_content += f"<br><img src='{image_url}' width='100%'>"  # Add image below the summary

    # Create the map marker with the popup content
    folium.Marker(
        location=coords,
        popup=folium.Popup(popup_content, max_width=300),
        tooltip=location
    ).add_to(m)

m.save(r"Kaartjes_script\index.html")

print("Kaart opgeslagen als 'index.html' lets go.")

print(images)
print(summary)