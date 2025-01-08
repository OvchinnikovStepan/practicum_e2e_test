"""Дата-файл для тестирования RestFul API, auth"""
# -*- coding: utf-8 -*-
from model.auth_model import RequestAuthModel

data = [RequestAuthModel(username='admin',password='password123')]
bad_data = [ {'username':'123','password':'password'}, 
           {'username':'','password':'password123'},
              {'username':'admin','password':''},
            {'username':123,'password':'password123'},
             {'username':'admin','password':''},
             {'username':'admin'},
              {'password':'password123'},
              {}]