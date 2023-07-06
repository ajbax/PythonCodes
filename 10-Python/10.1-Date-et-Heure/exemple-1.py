from datetime import datetime
import pytz

# Fuseau Horaire
fh_TOR = pytz.timezone('America/Toronto')

# Heure Actuelle
heure_TOR = datetime.now(fh_TOR)

# Formattage et Impression
print(f"\t>> Heure Toronto: {heure_TOR.strftime('%H:%M:%S')}")

fh_Paris = pytz.timezone('Europe/Paris')
heure_Paris = datetime.now(fh_Paris)

print(f"\t>> Heure Paris: {heure_Paris.strftime('%H:%M:%S')}")