import requests
import yaml


''' Задание
Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, 
а потом проверяется его наличие на сервере по полю «описание».
Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts 
с передачей параметров title, description, content.
'''

with open("config.yaml") as file:
    my_dict = yaml.safe_load(file)

url = my_dict["url"]
url1 = my_dict["url1"]
username = my_dict["username"]
password = my_dict["password"]


def token_auth(token):
    response = requests.get(url=url1, headers={"X-Auth-Token": token}, params={'owner': "notMe"})
    content_box = [item["content"] for item in response.json()["data"]]
    return content_box

def create_new_post(token, title, description, content):
    data = {
        "title": title,
        "description": description,
        "content": content
    }
    response = requests.post(url=url1, headers={"X-Auth-Token": token}, data=data)
    return response.json()


def test_step1(login):
    assert 'content' in token_auth(login)


def test_step2(login):
    new_post_data = {
        "title": "New Test Post",
        "description": "This is a test post description",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    }
    create_response = create_new_post(login, **new_post_data)

    description_to_check = new_post_data["description"]
    assert description_to_check in token_auth(login)
