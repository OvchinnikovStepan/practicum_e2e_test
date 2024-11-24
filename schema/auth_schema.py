"""Схема для RestFul API, auth"""

schema = {
  "type": "object",
  "properties": {
    "token": {
       "type":"string"
        }
    },
    "required": [
        "token"
      ]
}