sayi_listesi: list = list()

for i in range(1, 11):
    sayi =int(input(f"{i}. sayi: "))
    sayi_listesi.append(sayi)

    print(sum(sayi_listesi)/ len(sayi_listesi))