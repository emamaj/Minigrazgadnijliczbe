#Tworzenie prostej gry. Należy odgadnąć liczbę podaną przez komputer, wybraną z zakresu od 1-10

from random import randint


losowa = randint(1, 10)
odp = -1
i = 0
print("Odgadnij liczbę z przedziału od 1 do 10")

while odp != losowa:
    i += 1
    odp = int(input("Podaj liczbę: "))
    if odp > losowa:
        print("Podana liczba jest zbyt duża, spróbuj jeszcze raz...")
    elif odp < losowa:
        print("Twoja liczba jest mniejsza od wylosowanej, spróbuj jeszcze raz...")
print("Brawo, udało Ci się odgadnąć za", i, "razem.")