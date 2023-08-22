import requests
import yaml


with open("config.yaml") as file:
    my_dict = yaml.safe_load(file)


url = my_dict["url"]
url1 = my_dict["url1"]
username = my_dict["username"]
password = my_dict["password"]

'''
def login(username, password):
    obj_data = requests.post(url=url, data = {"username": username, "password": password})
    print(obj_data.json())
    token = obj_data.json()["token"]
    print(token)
    return token
'''

def token_auth(token):
    response = requests.get(url=url1, headers={"X-Auth-Token": token}, params={"owner": "notMe"})
    content_box = [item["content"] for item in response.json()["data"]]
    return content_box


def test_step2(login):
    assert 'content' in token_auth(login)
