import datetime

w = datetime.datetime.now()
print(w)
# le résultat sera une date contient l'année, le mois, le jour, 
# l'heure, la minute, la seconde et la microseconde.
M=datetime.datetime.now()
print(M.month)
print(M.strftime("%A"))
# Renvoie l'année et le nom du jour de la semaine :
D = datetime.datetime(2001,10,24)
print(D)
#it's the date of my birthday
#ici La datetime()classe nécessite trois paramètres pour créer une date : année, mois, jour.
print(D.strftime("%B"))
# la méthode strftime()sert a formater des objets de date en chaine lisible
print(D.strftime("%c"))
print(D.strftime("%C")) # centry
print(D.strftime("%z"))#timezone
print(D.strftime("%d"))#date du mois