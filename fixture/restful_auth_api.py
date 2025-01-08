import pytest
import requests
from api.restful_booker_api import RestfulBookerApi
from data.auth_data_fixture import data
@pytest.fixture(scope="function")
def api_token() -> str:
    # Задайте URL и данные для авторизации
    api=RestfulBookerApi().restful_auth(data[0])
    # Проверяем успешность запроса
    if api.json_schema_should_be_valid('auth_schema'):
        return api.get_payload(['token'])
    else:
        raise Exception("Ошибка авторизации, статус код: {}".format(api.response.status_code))