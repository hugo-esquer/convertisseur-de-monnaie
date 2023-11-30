from forex_python.converter import CurrencyRates

cr = CurrencyRates()
liste_devises = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP","ZAR"]

conversion = 0
historique = 0
fichier_historique = open("historique.txt", "r")

run = True
while run:
    
    consutler_historique = input("Voulez-vous consulter l'historique? O/N \n")
    if consutler_historique.upper() == "O":
        print(fichier_historique.read())
        fichier_historique.close()

    devise = input("Entrer une devise: ")
    try:
        montant = float(input("Entrer un montant en chiffres: "))
    except:
        montant = 0
    devise_conversion = input("Entrer une devise de conversion: ")

    if devise.upper() not in liste_devises:
        print("La devise de départ n'est pas bonne.")
    elif devise_conversion.upper() not in liste_devises:
        print("La devise de conversion n'est pas bonne.")
    elif montant == 0:
        print("Entrez un montant valide")
    else:
        conversion = cr.convert(devise.upper(), devise_conversion.upper(), montant)
        print(conversion)

        historique = f"{montant} {devise.upper()} -> {conversion} {devise_conversion.upper()}"
        with open("historique.txt", "a") as fichier:
            fichier.write(historique + "\n")
            
    stop = input("continuer ? O/N: \n")
    if stop.upper() == "N":
        run = False