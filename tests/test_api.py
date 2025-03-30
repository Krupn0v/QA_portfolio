import pytest, json 
from conftest import expRes, actRes, data, second_data


#    Проверка GET

def test_get(session_api, url):
    response = session_api.get(f"{url}/booking")
    assert response.status_code == 200, f"Failed. {expRes} 200, {actRes} {response.status_code}"
    assert len(response.json()) != 0, "Ответ пустой"


#    Проверка POST c валидным паролем и с пустым значением.

@pytest.mark.parametrize("data, expected_status, expected_token", [({"username" : "admin", "password": "password123"}, 200, True), ({"username" : "admin", "password": ""}, 200#для тестового api, в реальном ожидаем 400
, False)])
def test_post_auth(session_api, url, data, expected_status, expected_token):
    response = session_api.post(f"{url}/auth", json=data)
    assert response.status_code == expected_status, f"Failed. {expRes} {expected_status}, {actRes} {response.status_code}"
    if expected_token:
        assert "token" in response.json().keys(), "Не вернулся токен"
    else:
         assert "reason" in response.json().keys(), "Невернулась ошибка"

#    Проверка POST. Создает новый пост с "title": "Passed"
@pytest.mark.parametrize("second_data, expected_status, expected_title", [({"title": "Passed", "Body": "Test_post"}, 201, "Passed"), ({"title": "", "Body": "Test_post"}, 201, "")])
def test_second_post(session_api, second_url, second_data, expected_status, expected_title):
    response = session_api.post(f"{second_url}/posts",json=second_data)
    assert response.status_code == 201, f"Failed. {expRes} {expected_status}, {actRes} {response.status_code}"
    if expected_title:
        assert response.json()["title"] == "Passed", "Не соответствует title"
    else:
        assert response.json()["title"] == ""

#    Проверка PUT. Добавляет к посту (id:1) - "title": "Passed"

def test_put(session_api, second_url, second_data):
    response = session_api.put(f"{second_url}/posts/1",json=second_data)
    assert response.status_code == 200, f"Failed. {expRes} 200, {actRes} {response.status_code}"
    assert response.json()["title"] == "Passed", "Не соответствует title"


#    Проверка Patch. Изменяет title поста (id:1) на  "Passed" 
       
def test_patch(session_api, second_url, second_data):
    response = session_api.patch(f"{second_url}/posts/1",json=second_data)
    assert response.status_code == 200, f"Failed. {expRes} 200, {actRes} {response.status_code}"
    assert response.json()["title"] == "Passed", "Не соответствует title"
    
    
#    Удаляет пост (id:1)

def test_delete(session_api, second_url):
    response = session_api.delete(f"{second_url}/posts/1")
    assert response.status_code == 200, f"Failed. {expRes} 200, {actRes} {response.status_code}"
    assert (response.content == b"{}"), "Пост не удален"
    
