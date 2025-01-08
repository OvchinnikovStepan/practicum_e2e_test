"""Тест кейс для Restful API, create booking"""
from helper.load import load_data
import allure
import pytest


pytest_plugins = ["fixture.restful_api","fixture.restful_auth_api"]
pytestmark = [allure.parent_suite("restful"),
              allure.suite("create")]

@allure.title('Запрос на создание брони')
@pytest.mark.parametrize('request_params',
                         load_data('create_booking_data','data'))
def test_auth_valid_parameters(restful_api, request_params,api_token):
    restful_api.restful_create_from_dict(request_params).status_code_should_be(200).\
        json_schema_should_be_valid('create_booking_schema').\
        have_value_in_response_parameter(['booking'], request_params)
    
    id = restful_api.get_payload(["bookingid"])
    restful_api.restful_get(id).\
        have_value_in_response_parameter([],request_params)

    restful_api.restful_delete(id,api_token).status_code_should_be(200)
    
@allure.title('Некорректный запрос на создание брони')
@pytest.mark.parametrize('request_params',
                         load_data('create_booking_data','bad_data'))
def test_auth_not_valid_parameters(restful_api, request_params,api_token):
    req=restful_api.restful_create_from_dict(request_params)
    req.status_code_should_be(400)
