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
    restful_api.restful_create(request_params).status_code_should_be(200).\
        json_schema_should_be_valid('create_booking_schema').\
        have_value_in_response_parameter(['booking'], request_params.to_dict())
    
    restful_api.restful_delete(restful_api.get_payload(["bookingid"]),api_token).status_code_should_be(200)