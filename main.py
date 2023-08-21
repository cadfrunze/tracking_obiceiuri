import requests

param1: dict = {
    'token': 'testing-~1985',
    'username': 'cadfrunze',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
response_post = requests.post(url='https://pixe.la/v1/users', params=param1)
print(response_post)
print('dsdssdsd')
print('ddsddsdsd')
print('a')