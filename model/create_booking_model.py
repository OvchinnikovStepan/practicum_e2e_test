"""Модели для create user"""
from dataclasses import dataclass, asdict

@dataclass
class RequestCreateModel:
    """Класс для параметров request"""
    firstname : str
    lastname : str
    totalprice : int
    depositpaid : bool
    bookingdates : dict
    additionalneeds : str
    def to_dict(self):
        """преобразование в dict для отправки body"""
        return asdict(self)
    
class ResponseCreateModel:
    """Класс для параметров request"""
    bookingid:int
    booking:dict
    def to_dict(self):
        """преобразование в dict для отправки body"""
        return asdict(self)