import requests

my_domain = 'ryosan.pythonanywhere.com'
username = 'ryosan'
token = '9482a90135232d6e576cbd75c50b527bea5a068d'

response = requests.post(
    'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
        username=username, domain=my_domain
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)

if response.status_code == 200:
    print('OK')
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

