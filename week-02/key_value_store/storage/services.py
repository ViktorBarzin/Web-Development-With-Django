import uuid
import os
import json

from django.conf import settings
from storage.exceptions import UserDoestNotExistException
from storage.models import User, KeyValue

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


def get_user_from_db(identifier):
    user = User.objects.filter(id=identifier).first()
    if user is None:
        raise UserDoestNotExistException
    return user

def get_value_with_key(*, identifier, key):
    user = get_user_from_db(identifier=identifier)
    key_value = user.key_values.filter(key=key).first()
    if key_value is None:
        return None
    return key_value.value


def delete_key_value(*, identifier, key):
    user = get_user_from_db(identifier=identifier)
    key_val = user.key_values.filter(key=key).first()
    if key_val:
        old_key = key_val.key
        user.key_values.filter(key=old_key).delete()
        user.save()
        return old_key


