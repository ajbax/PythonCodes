from datetime import datetime
## Définition de la classe parent

class Telephone:
    def __init__(self, numero):
        self.numero = numero

    def appel(self, numeroDestinataire):
        if self.numero != numeroDestinataire:
            print(f"Appel en cours vers {numeroDestinataire}")
        else:
            print("Mauvais numéro!")

    @staticmethod
    def verificationHeure():
        maintenant = datetime.now()
        heureActuelle = maintenant.strftime("%H:%M:%S")
        print(f"Heure: {heureActuelle}")



# Définition de la classe enfant par héritage de la classe Telephone
class Smartphone(Telephone):

    def appel(self, numeroDestinataire):
        if self.numero != numeroDestinataire:
            print("Options d'appel:\n\t- (A) pour appel Audio\n\t- (V) pour appel Vidéo")
            option = input(">> Veuillez saisir votre choix: ")
            if option.upper() == 'A':
                print(f"Appel AUDIO en cours vers {numeroDestinataire}")
            elif option.upper() == 'V':
                print(f"Appel AUDIO en cours vers {numeroDestinataire}")
            else:
                print("Mauvaise Option!!!")
        else:
            print("Mauvais numéro!")


# Démonstration de l'appel de la méthode appel()

t1 = Telephone("647-000-0001")
t2 = Smartphone("647-00-0011")

t1.appel("514-001-0003")
t2.appel("514-001-0003")

# On peut faire appel à la méthode verificationHeure
t1.verificationHeure()
