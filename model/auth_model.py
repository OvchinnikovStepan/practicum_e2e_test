"""Модели для create user"""
from dataclasses import dataclass, asdict

@dataclass
class RequestAuthModel:
    """Класс для параметров request"""
    username: str
    password: str

    def to_dict(self):
        """преобразование в dict для отправки body"""
        return asdict(self)

@dataclass
class ResponseAuthModel:
    """Класс для параметров респонса"""
    token: str