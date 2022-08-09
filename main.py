import requests

def get_data(n):
    # url randomuser
    url = 'https://randomuser.me/api/?results={}'.format(n)
    response = requests.get(url).json()
    data = response.get('results')
    return data

data = get_data(5)
print(len(data))