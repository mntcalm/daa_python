def is_valid(person):
  return person['name'].startswith('A') and 18 <= person['age'] <= 30



list_ = [
    {'name': 'Alex', 'age': 25},
    {'name': 'Oleg', 'age': 23},
    {'name': 'Anna', 'age': 32},
    {'name': 'Igor', 'age': 50},
    {'name': 'Anton', 'age': 17},
]


print(list(filter(is_valid, list_)))

a=list(filter(lambda x: x['name'].startswith('A'), list_))
b=list(filter(lambda y: 18 <= y['age'] <= 30, a))
print(b)