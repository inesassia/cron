#scriptt de text des cron, avec ecriture dans une fichier text de la date actuelle


from datetime import datetime
now=datetime.now()
print (now)
with open('/home/milaa/cron/script_test.txt','a') as f:
    f.write('Actuellement nous somme {}\n'.format(now))
