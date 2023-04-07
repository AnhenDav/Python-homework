print('Домашнее задание 1')
import json

#
# purchase = dict()
# while True:
#     product = input('Укажите название покупки:').lower()
#     if product == 'стоп':
#         break
#     cost = input('Укажите стоимость:')
#     purchase[product] = cost
# print(purchase)
#
# with open('day_purchase.json', 'w', encoding='UTF-8') as file:
#     json.dump(purchase, file, ensure_ascii=False)
# print()

print('Домашнее задание 2')
with open('day_purchase.json', encoding='UTF-8') as file1:
    purchases = json.load(file1)
cost_per_day = 0
for value in purchases.values():
    cost_per_day += int(value)
print(cost_per_day)
