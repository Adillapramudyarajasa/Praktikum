Nama : Adilla Pramudya Rajasa
Nim  : 064002100018
"""

import csv

Negara = []

with open('Negara.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        Negara.append(row)

print("Negara \t\t\t Ibu Kota \t Benua \t Luas \tPopulasi")
print("-" * 52)

for data in Negara:
    print(f"{data['Negara']} \t {data['Ibu Kota']} \t {data['Benua']} \t {data['Luas']} \t {data['Populasi']}")
    
