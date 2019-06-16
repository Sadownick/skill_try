import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
users = (response.json())
# print(users[0])

email = users[0]['email']
print(email)


new_user_1 = {
    'email': 'john@doe.ru',
    'first_name': 'John'
}

a = requests.post('https://jsonplaceholder.typicode.com/users', new_user_1)
print(a.content)
