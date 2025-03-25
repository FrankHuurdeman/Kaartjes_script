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

# Coordinaten ophalen voor reislocaties van Belgie
brugge_coords = get_coordinates("Brugge, Belgium")
antwerpen_coords = get_coordinates("Antwerp, Belgium")
la_roche_coords = get_coordinates("La Roche-en-Ardenne, Belgium")
bouillon_coords = get_coordinates("Bouillon, Belgium")

# Coordinaten ophalen voor reislocaties van Engeland
london_coords = get_coordinates("London, England")

# Coordinaten ophalen voor reislocaties van Frankrijk
parijs_coords = get_coordinates("Paris, France")
avignon_coords = get_coordinates("Avignon, France")
troyes_coords = get_coordinates("Troyes, France")

# Coordinaten ophalen voor reislocaties van Spanje
barcelona_coords = get_coordinates("Barcelona, Spain")

# Coordinaten ophalen voor reislocaties van Italie
verona_coords = get_coordinates("Verona, Italy")
venice_coords = get_coordinates("Venice, Italy")
feltre_coords = get_coordinates("Feltre, Italy")

# Coordinate ophalen voor reislocaties van Zwitserland
interlaken_coords = get_coordinates("Interlaken, Switzerland")

# Coordinaten ophalen voor reislocaties van Kroatie
zagreb_coords = get_coordinates("Zagreb, Croatia")
split_coords = get_coordinates("Split, Croatia")

# Coordinaten ophalen voor reislocaties van Oostenrijk
vienna_coords = get_coordinates("Vienna, Austria")

# Coordinaten ophalen voor reislocaties van Polen
wrolcaw_coords = get_coordinates("Wroclaw, Poland")

# Coordinaten ophalen voor reislocaties van Tsjechie
prague_coords = get_coordinates("Prague, Czech Republic")

# Coordinaten ophalen voor Griekenland 
sami_coords = get_coordinates("Sami, Greece")
kamari_coords = get_coordinates("Kamari, Greece")

# Coordinaten ophalen voor reislocaties van Denemarken
kopenhagen_coords = get_coordinates("Copenhagen, Denmark")
roskilde_coords = get_coordinates("Roskilde, Denmark")

# Coordinaten ophalen voor reisloacties van Zweden
malmo_coords = get_coordinates("Malmo, Sweden")
charlottenberg_coords = get_coordinates("Charlottenberg, Sweden")
arvika_coords = get_coordinates("Arvika, Sweden")
karlstad_coords = get_coordinates("Karlstad, Sweden")
orebro_coords = get_coordinates("Orebro, Sweden")
stockholm_coords = get_coordinates("Stockholm, Sweden")
ostersund_coords = get_coordinates("Östersund, Sweden")
goteborg_coords = get_coordinates("Gothenburg, Sweden")
storlien_coords = get_coordinates("Storlien, Sweden")

# Coordinaten ophalen voor reislocaties van Noorwegen
oslo_coords = get_coordinates("Oslo, Norway")
bergen_coords = get_coordinates("Bergen, Norway")
flam_coords = get_coordinates("Flam, Norway")
lillehammer_coords = get_coordinates("Lillehammer, Norway")
trondheim_coords = get_coordinates("Trondheim, Norway")
narvik_coords = get_coordinates("Narvik, Norway")
svolvaer_coords = get_coordinates("Svolvaer, Norway")
henningsvaer_coords = get_coordinates("Henningsvaer, Norway")
sydalen_coords = get_coordinates("Sydalen, Norway")
leknes_coords = get_coordinates("Leknes, Norway")
reine_coords = get_coordinates("Reine, Norway")
a_coords = get_coordinates("A, Norway")

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
    "Hilversum": hilversum_coords,

    # Duitsland
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
    "Hannover": hannover_coords,
    "Esslingen": esslingen_coords,
    "Trier": trier_coords,
    "Bremen": bremen_coords,

    # België
    "Brugge": brugge_coords,
    "Antwerpen": antwerpen_coords,
    "La Roche-en-Ardenne": la_roche_coords,
    "Bouillon": bouillon_coords,

    # Engeland
    "Londen": london_coords,

    # Frankrijk
    "Parijs": parijs_coords,
    "Avignon": avignon_coords,
    "Troyes": troyes_coords,

    # Spanje
    "Barcelona": barcelona_coords,

    # Italië
    "Verona": verona_coords,
    "Venetië": venice_coords,
    "Feltre": feltre_coords,

    # Zwitserland
    "Interlaken": interlaken_coords,

    # Kroatië
    "Zagreb": zagreb_coords,
    "Split": split_coords,

    # Oostenrijk
    "Wenen": vienna_coords,

    # Polen
    "Wroclaw": wrolcaw_coords,

    # Tsjechië
    "Praag": prague_coords,

    # Griekenland
    "Sami": sami_coords,
    "Kamari": kamari_coords,

    # Denemarken
    "Kopenhagen": kopenhagen_coords,
    "Roskilde": roskilde_coords,

    # Zweden
    "Malmö": malmo_coords,
    "Charlottenberg": charlottenberg_coords,
    "Arvika": arvika_coords,
    "Karlstad": karlstad_coords,
    "Orebro": orebro_coords,
    "Stockholm": stockholm_coords,
    "Östersund": ostersund_coords,
    "Göteborg": goteborg_coords,
    "Storlien": storlien_coords,

    # Noorwegen
    "Oslo": oslo_coords,
    "Bergen": bergen_coords,
    "Flåm": flam_coords,
    "Lillehammer": lillehammer_coords,
    "Trondheim": trondheim_coords,
    "Narvik": narvik_coords,
    "Svolvær": svolvaer_coords,
    "Henningsvær": henningsvaer_coords,
    "Sydalen": sydalen_coords,
    "Leknes": leknes_coords,
    "Reine": reine_coords,
    "Å": a_coords
}

for city, coords in locations.items():
    if coords is None or not isinstance(coords, (list, tuple)) or len(coords) != 2:
        print(f"⚠️ Fout: Geen geldige coördinaten voor {city}: {coords}")
    else:
        folium.Marker(coords, popup=city).add_to(m)

m.save(r"Kaartjes_script\index.html")
print("Kaart opgeslagen als 'index.html'.")