import requests
from datetime import datetime

pixela_endpoint: str = 'https://pixe.la/v1/users'
param1: dict = {
    'token': '****',
    'username': '*test',
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

# graph_endpoint = requests.post(url=f"{pixela_endpoint}/{param1['username']}/graphs",
#                                headers=headers_key, json=param_graph_endpoint)
astazi: str = datetime(year=2023, month=8, day=27).strftime('%Y%m%d')
# update_graph_param: dict = {
#     'date': astazi,
#     'quantity': '3',
#     # 'optionalData': 'testing'
# }
#
#
# update_graph = requests.post(
#     url=f'{pixela_endpoint}/{param1["username"]}/graphs/{param_graph_endpoint["id"]}',
#     headers=headers_key,
#     json=update_graph_param
# )
# print(update_graph.text)

put_endpoint = f'{pixela_endpoint}/{param1["username"]}/graphs/{param_graph_endpoint["id"]}/{astazi}'
dict_put: dict = {
    'quantity': '4'
}
cerere_put = requests.put(url=put_endpoint, headers=headers_key, json=dict_put)
print(cerere_put.text)

# delete_end_point = /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
# delete_endpoint = f'{pixela_endpoint}/{param1["username"]}/graphs/{param_graph_endpoint["id"]}/{astazi}'
# cerere_delete = requests.delete(url=delete_endpoint, headers=headers_key)
# print(cerere_delete.text)
