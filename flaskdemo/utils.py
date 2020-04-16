import requests
from requests.auth import HTTPBasicAuth


user = 'jclark'
pa = 'Test!23'
query = 'http://local-d8.dol.docksal/node/{}?_format=json'
auth = HTTPBasicAuth(user, pa)
headers = {
        'content-type': 'application/hal+json',
        'accept': 'application/json'
    }


def get_node_title(id_):
    url = query.format(id_)
    try:
        r = requests.get(url, headers=headers)
        json = r.json()
        title = json['title'][0]
        return title['value']
    except:
        return None


def get_node_alias(id_):
    url = query.format(id_)
    try:
        r = requests.get(url, headers=headers)
        json = r.json()
        path = json['metatag']
        path = path['value']
        return path['canonical_url']
    except:
        return None


def get_node_field_rows(id_):
    url = query.format(id_)
    r = requests.get(url, headers=headers)
    json = r.json()
    rows = json['field_row']


def get_paragraph(paragraph):
    url = 'http://local-d8.dol.docksal/entity/paragraph/{}?_format=json'

