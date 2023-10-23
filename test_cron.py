#essaie de cron, ecrire dans un fichier si le nom de domaine a  expirer ou pas


from datetime import datetime
import time
from datetime import datetime
from dateutil.parser import parse
from datetime import date

def set_reminder(date_str, message):
    reminder_time = time.mktime(time.strptime(date_str, "%Y-%m-%d %H:%M:%S"))
    reminder_date = parse(date_str).date()
    current_date=date.today()
    date_diff=reminder_date - current_date
    current_time = time.time()
    time_diff = reminder_time - current_time
    # Convertir le timestamp en objet datetime
    dt_object = datetime.fromtimestamp(time_diff)

# Formater l'objet datetime en une chaîne de caractères représentant l'heure
    formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')

    if time_diff > 0:
        with open('/home/milaa/cron/test_cron.txt','a') as f:
            f.write('Votre nom de domaine expire dans:  {}\n'.format(date_diff))

    else:
     with open('/home/milaa/cron/test_cron.txt','a') as f:

            f.write("Votre nom de domaine a espirer\n")

date_input = "2023-08-30 21:35:58"
message_input = "yes"

set_reminder(date_input, message_input)

