import csv

total_cost = 0

with open('r.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    print("Нужно купить:")
    for row in reader:
        product, quantity, price = row
        cost = int(quantity) * int(price)
        print(product, "-", quantity, "шт. за", price, "руб.")
        total_cost += cost

print("Итоговая сумма:", total_cost, "руб.")