import uuid
import os
import json

from django.conf import settings
from storage.exceptions import UserDoestNotExistException
from storage.models import User, KeyValue
from collections import defaultdict

def uuid4():
    return str(uuid.uuid4())


def create_user():
    identifier = uuid4()
    User.objects.create(id=identifier)
    return identifier


def store_data(*, identifier, data):
    user = User.objects.filter(id=identifier).first()
    if not user:
        raise UserDoestNotExistException
    keyval = user.key_values.filter(key=data['key']).first()
    if keyval is None:
        keyval = KeyValue.objects.create(key=data['key'], value=data['value'], user=user)
        user.key_values.add(keyval)
    else:
        keyval.value = data['value']
        keyval.save()
    user.save()
    return data


def get_user_from_db(identifier):
    user = User.objects.filter(id=identifier).first()
    if user is None:
        raise UserDoestNotExistException
    return user

def get_value_with_key(*, identifier, key):
    user = get_user_from_db(identifier=identifier)
    if user is None:
        raise UserDoestNotExistException

    key_value = user.key_values.filter(key=key).first()
    if key_value is None:
        return None
    return key_value.value


def delete_key_value(*, identifier, key):
    user = get_user_from_db(identifier=identifier)
    if user is None:
        raise UserDoestNotExistException
    key_val = user.key_values.filter(key=key).first()

    if key_val is None:
        return None

    old_key = key_val.key
    user.key_values.filter(key=old_key).delete()
    user.save()
    return old_key



def create_histogram(objects):
    d = defaultdict(int)
    for o in objects:
        d[o] += 1

    return dict(d)


