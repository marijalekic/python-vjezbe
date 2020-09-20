imena=["Marija", "Ivana", "Danijela", "Dragan", "Petar"]

for ime in imena:
    print(ime)


novo_ime=input("Unesite novo ime: ")

imena.append(novo_ime)

print("Nova lista imena: ")
for ime in imena:
    print(ime)
