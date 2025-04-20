import requests, pytest

expRes = "Ожидаемый результат:"
actRes = "Фактический результат:"

@pytest.fixture
def session_api():
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture
def url():
    return "https://restful-booker.herokuapp.com"

@pytest.fixture
def second_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def data():
    payload = {
        "username" : "admin",
        "password" : "password123"
        }
    return payload

@pytest.fixture
def second_data():
    payload = {
	       "title": "Passed"
        }
    return payload