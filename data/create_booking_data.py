"""Дата-файл для тестирования RestFul API, auth"""
# -*- coding: utf-8 -*-
from model.create_booking_model import RequestCreateModel

request=RequestCreateModel(firstname="Jhon",lastname="Smith",
                            totalprice=100,depositpaid=True,
                            bookingdates={"checkin":"2018-11-12",
                                          "checkout":"2018-12-12"},
                            additionalneeds="Breakfast")

data = [request]
