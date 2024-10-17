import csv
import sys
import os
import matplotlib.pyplot as plt

file_path = 'Data.csv'

if not os.path.exists(file_path):
    print(f"Файл {file_path} не знайдено!")
    sys.exit()

data = {}
years = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        country = row[0]
        values = row[4:14]
        data[country] = [float(v) if v not in ['..', ''] else 0 for v in values]

country = input("Введіть назву країни для побудови стовпчастої діаграми: ")

if country not in data:
    print("Невірно введена країна або дані відсутні!")
    sys.exit()

values = data[country]

plt.figure(figsize=(10, 6))
plt.bar(years, values, color='orange')
plt.xlabel('Рік')
plt.ylabel('Children out of school, primary')
plt.title(f'Показник "Children out of school, primary" для {country}')
plt.grid(True)
plt.show()
