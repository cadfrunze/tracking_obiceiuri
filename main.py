import requests

pixela_endpoint: str = 'https://pixe.la/v1/users'
param1: dict = {
    'token': 'testing1985',
    'username': 'cadfrunze',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# response_post = requests.post(url='https://pixe.la/v1/users', json=param1)
# print(response_post.text)
param_graph_endpoint = {
    'id': 'grafica1',
    'name': 'Contabilizare timp petrecut pt invatare',
    'unit': 'hours',
    'type': 'int',
    'color': 'sora',
    'timezone': 'Europe/Bucharest'
}
headers_key: dict = {
    'X-USER-TOKEN': param1['token']
}

graph_endpoint = requests.post(url=f"{pixela_endpoint}/{param1['username']}/graphs",
                               headers=headers_key, json=param_graph_endpoint)

