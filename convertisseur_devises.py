from forex_python.converter import CurrencyRates

cr = CurrencyRates()
liste_devises = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP","ZAR"]


devise = "EUR"
conversion = 0
historique = 0
fichier_historique = open("historique.txt", "r")

run = True
while run:
    devises_fav = {}
    with open('favoris.csv' , 'r') as f:
        for line in f:
            d = line.split(':')
            devises_fav[ d[0] ] = float ( d[1] )
    
    consutler_historique = input("Voulez-vous consulter l'historique? O/N \n")
    if consutler_historique.upper() == "O":
        print(fichier_historique.read())
        fichier_historique.close()

    try:
        montant = float(input("Entrer un montant en chiffres: "))
    except:
        montant = 0
    devise_conversion = input("Entrer une devise de conversion ou une nouvelle devise: ").upper()

    if devise_conversion not in liste_devises and devise_conversion not in devises_fav:
        print("La devise de conversion n'est pas dans ma base de données. /n")

        print("voulez-vous ajouter une devise? O/N")
        ajout = input().upper()
        if ajout == "O":
            new_devise = input("Entrer une nouvelle devise: ").upper()
            try:
                new_taux = float(input("Entrer un taux de conversion: "))
            except:
                print("Entrer un taux sous forme de chiffre")

            devises_fav[new_devise] = new_taux
            with open('favoris.csv', 'a') as f:
                [f.write('{0}:{1}\n'.format(key, value)) for key, value in devises_fav.items()]

    elif montant == 0:
        print("Entrez un montant valide")
    elif devise_conversion in devises_fav:
        print(montant*devises_fav[devise_conversion])
    else:
        conversion = cr.convert(devise.upper(), devise_conversion.upper(), montant)
        print(conversion)

        historique = f"{montant} {devise.upper()} -> {conversion} {devise_conversion.upper()}"
        with open("historique.txt", "a") as fichier:
            fichier.write(historique + "\n")

    stop = input("continuer ? O/N: \n")
    if stop.upper() == "N":
        run = False