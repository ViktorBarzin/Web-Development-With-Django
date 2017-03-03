import uuid
import os
import json

from django.conf import settings
from storage.exceptions import UserDoestNotExistException

def uuid4():
    return str(uuid.uuid4())


def create_user():
    # get uuid
    identifier = uuid4()
    # write uuid to db
    user_file = os.path.join(settings.JSON_DATABASE_DIR, identifier + '.json')

    with open(user_file, 'w') as f:
        f.write('{}')

    # return uuid
    return identifier


def store_data(*, identifier, data):
    user_file = os.path.join(settings.JSON_DATABASE_DIR, identifier + '.json')
    if not os.path.exists(user_file):
        raise UserDoestNotExistException
    with open(user_file, 'w') as f:
    # saving 1 key-value pair at the time

        f.write(json.dumps({data.get('key'):data.get('value')}, indent=4))

def get_user_from_db(identifier):
    user_file = os.path.join(settings.JSON_DATABASE_DIR, identifier + '.json')

    if not os.path.exists(user_file):
        return None

    with open(user_file, 'r') as f:
        # import ipdb; ipdb.set_trace()

        user = json.loads(f.read())
    return user

def get_value_with_key(*, identifier, key):
    user = get_user_from_db(identifier)

    if user is None:
        raise UserDoestNotExistException

    value = user.get(key)
    return value


def delete_key_value(*, identifier, key):
    # import ipdb; ipdb.set_trace()# BREAKPOINT)
    user = get_user_from_db(identifier)
    if user is None:
        raise UserDoestNotExistException
    if key not in user:
        return None
    value = user.pop(key)
    store_data(identifier=identifier, data=user)
    return value




