from os import name
import overview
from pydantic import ValidationError


print("-----------1----------")
try:
    overview.User(signup_ts='broken', friends=[1, 2,3, 'not number'])
except ValidationError as error:
    print(error.json())


print("-----------2----------")
try:
    overview.User(signup_ts='2019-06-01 11;22', friends=[1, 2, '9'])
except ValidationError as error:
    print(error.json())


print("-----------3----------")
try:
    overview.User(signup_ts='broken', friends=[1, 2, '9'], id=2, name='john')
except ValidationError as error:
    print(error.json())