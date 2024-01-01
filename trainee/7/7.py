greetings = {
'ru': 'Привет',
'us': 'Hello',
'es': 'Hola',
'unknown country': 'Hi',
'aserg': 'aswdsasasd'
}


users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
    ('Someone', 'unknosghfjtjtyjwn country'),
]

def greet(user):
  name, code = user
  greeting = greetings.get(code, 'default_Hi')
  return f'{greeting}, {name}!'

greeted_users = map(greet, users_list)
print(list(greeted_users))

