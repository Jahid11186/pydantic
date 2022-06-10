from datetime import datetime
from typing import List, Optional
import pydantic
from pydantic import BaseModel

print('Compiled: ', pydantic.compiled)


class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'sign_up_ts': '2019-06-01 11;22',
    'friends': [1, 2, '3'],
}

user = User(**external_data)
print(user.id)

print(repr(user.signup_ts))

print(user.friends)

print(user.dict())
