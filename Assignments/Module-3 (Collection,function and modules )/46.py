sample_data = [{'item': 'item1', 'amount': 100}, {'item': 'item2', 'amount': 300},
               {'item': 'item1', 'amount': 150}]

combined_data = {}

for i in sample_data:
    item = i['item']
    amount = i['amount']
    if item in combined_data:
        combined_data[item] += amount
    else:
        combined_data[item] = amount

print(combined_data)
