from Profesor import Profesor


profesor1=Profesor("Ivan", "Matematika", "V-3", True)

profesor1.ime=input("Unesite ime profesora: ")

print(profesor1.ime + " predaje: " + profesor1.predmet)

profesor2=Profesor("Sanja", "Informatika", "VI-4", True)

if profesor1.stalno:
    print(profesor1.ime+ " ima stalni radni odnos")
else:
    print("Privremeni radni odnos")