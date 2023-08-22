import pytest
import requests
import yaml


with open("config.yaml") as file:
    my_dict = yaml.safe_load(file)

url = my_dict["url"]
username = my_dict["username"]
password = my_dict["password"]

@pytest.fixture()
def login(username="Ivan1234", password="416b69ce0b"):
    obj_data = requests.post(url=url, data = {"username": username, "password": password})
    token = obj_data.json()["token"]
    return token
