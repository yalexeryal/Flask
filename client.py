import requests

resp = requests.get('http://127.0.0.1:8080/users/1').json()
print(resp)

#
resp = requests.post('http://127.0.0.1:5051/users/',
                     json={
                         'username': 'test2',
                         'password': 'sgdsppo34FET32325',
                         'email': 'test2@test.test'
                     }).json()
print(resp)
