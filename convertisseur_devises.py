from forex_python.converter import CurrencyRates

def ajout_historique(conv):
    # enregistrement dans l'historique
    historique = f"{montant} {devise} -> {conv} {devise_conversion}"
    with open("historique.txt", "a") as fichier:
        fichier.write(historique + "\n")

cr = CurrencyRates()
liste_devises = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP","ZAR"]

devise = "EUR"
conversion = 0
historique = 0

run = True
while run:
    fichier_historique = open("historique.txt", "r")
    # liste pour les nouvelles devises
    new_fav = {}
    # récupérer les devises favorites depuis le fichier .csv
    devises_fav = {}
    with open('favoris.csv' , 'r') as f:
        for line in f:
            d = line.split(':')
            devises_fav[ d[0] ] = float ( d[1] )
    
    # demander si l'utilisateur veux consulter l'historique
    consutler_historique = input("Voulez-vous consulter l'historique? O/N \n")
    if consutler_historique.upper() == "O":
        print(fichier_historique.read())    # afficher le contenu du fichier
        fichier_historique.close()

    try:
        montant = float(input("Entrer un montant en Euro: "))
    except:
        montant = 0
    devise_conversion = input("Entrer une devise de conversion ou une nouvelle devise: ").upper()

    # si la devise n'est pas connue
    if devise_conversion not in liste_devises and devise_conversion not in devises_fav:
        print("La devise de conversion n'est pas dans ma base de données. \n")

        # ajouter une nouvelle devise
        print("voulez-vous ajouter une devise? O/N")
        ajout = input().upper()
        if ajout == "O":
            new_devise = input("Entrer une nouvelle devise: ").upper()
            try:
                new_taux = float(input("Entrer un taux de conversion: "))
            except:
                print("Entrer un taux sous forme de chiffre")

            # enregistrer la devise dans un fichier .csv
            new_fav[new_devise] = new_taux # enregistrer la nouvelle paire clé : valeur
            with open('favoris.csv', 'a') as f:
                [f.write('{0}:{1}\n'.format(key, value)) for key, value in new_fav.items()]

    elif montant == 0:
        print("Entrez un montant valide")

    elif devise_conversion in devises_fav:  # conversion avec une devise perso
        print(f"{montant} Eur -> {montant*devises_fav[devise_conversion]} {devise_conversion}")
        ajout_historique(montant*devises_fav[devise_conversion])

    else:   # conversion avec forex_python
        conversion = cr.convert(devise.upper(), devise_conversion.upper(), montant)
        print(f"{montant} Eur -> {conversion} {devise_conversion}")
        ajout_historique(conversion)

    stop = input("continuer ? O/N: \n").upper()
    if stop == "N":
        run = False