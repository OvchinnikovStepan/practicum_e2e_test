import allure
from api.api import Api
from model.auth_model import RequestAuthModel,ResponseAuthModel
from model.create_booking_model import RequestCreateModel
class RestfulBookerApi(Api):

    """URl"""
    _URL = 'https://restful-booker.herokuapp.com'

    """Endpoint"""
    _ENDPOINT_AUTH = '/auth/'
    _ENDPOINT_BOOKING = '/booking/'

    #_TOKEN=None

    @allure.step('Обращение к auth')
    def restful_auth(self, param_request_body: RequestAuthModel):
        api=self.post(url=self._URL,
                         endpoint=self._ENDPOINT_AUTH,
                         json_body=param_request_body.to_dict())
    #    global _TOKEN
    #    _TOKEN=api.get_payload(['token'])
        return api
    
    @allure.step('Обращение к post')
    def restful_create(self,param_request_body: RequestCreateModel):
        return self.post(url=self._URL,
                         endpoint=self._ENDPOINT_BOOKING,
                         json_body=param_request_body.to_dict())
    
    @allure.step('Обращение к delete')
    def restful_delete(self, booking_id: int, token: str):
        return self.delete(url=self._URL,
                           endpoint=self._ENDPOINT_BOOKING + str(booking_id),headers={'token':f'token={token}'})