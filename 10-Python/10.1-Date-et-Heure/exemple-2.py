from datetime import datetime
import pytz


villes = ['Toronto', 'Paris', 'London', 'Montreal', 'Seoul', 'Chicago', 'Tokyo', 'Detroit', 'Los Angeles']


for ville in villes:
    if ' ' in ville:
        ville = ville.replace(' ', '_')

    for tz in pytz.all_timezones:

        if ville in tz:
            fh_Ville = pytz.timezone(tz)
            heureVille = datetime.now(fh_Ville)

            print(f"\t>> Heure {ville}: {heureVille.strftime('%H:%M:%S')}")