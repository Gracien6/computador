#  prix = input('quels ont été les revenus du pepsi du magasin?')
#  print ('le prix du pepsi est ' + prix )  
#  prix coca cola =150
#  prix pepsi =130
#  prix total =2500
#  prix unite coca cola 1.5
#  prix unite de pepsi 1.5
prixPepsi = float(input("Entrer le prix du pepsi: "))
prixTotalpepsi = float(input("Entrer le total du pepsi: "))
resultat = prixPepsi * prixTotalpepsi  
print(resultat)


prixCocaCola = float(input("Entrer le prix du coca cola: "))
prixTotalCocaCola = float(input("Entrer le total du coca cola: "))
resultat = prixCocaCola  * prixTotalCocaCola
print(resultat )

# revenuPepsi = 195
# revenuCocaCola = 225
revenuTotalP = float(input("Entrer le revenus du pepsi: "))
revenuTotalC = float(input("Entrer le revenus du coca cola: "))
resultat = revenuTotalP + revenuTotalC
print(resultat )

# revenuTotal = 420
# depanceMagasin = 2500
revenuTotal = float(input("Entrer le revenus total: "))
depanceMagasin = float(input("Entrer le depance du magasin: "))
resultat = revenuTotal - depanceMagasin
print(resultat)

benefice = - 2080
revenuTotal = 420
marge = float(input("Entrer le benefice  du magasin: "))
revenuTotalM = float(input("Entrer le revenu total du magasin: "))
resultat =  benefice / revenuTotal
print(resultat) 
