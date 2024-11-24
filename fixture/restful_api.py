"""Фикстуры Restful-Booker API"""
import pytest
from api.restful_booker_api import RestfulBookerApi

@pytest.fixture(scope="function")
def restful_api() -> RestfulBookerApi:
    """Коннект к RestFul API"""
    return RestfulBookerApi()