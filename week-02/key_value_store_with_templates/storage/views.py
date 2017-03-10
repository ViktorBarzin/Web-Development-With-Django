from django.http import HttpResponse
from django.shortcuts import render, redirect
from storage.services import create_histogram, get_user_from_db
from storage.models import KeyValue, User
from storage.exceptions import UserDoestNotExistException



def home_view(request):
    # total number of users
    number_of_users = len(User.objects.all())

    # total number of keys
    number_of_keys = len(KeyValue.objects.all())

    # histogram of all keys
    keys_histogram = create_histogram([x.key for x in KeyValue.objects.all()])
    return render(request, 'index.html', locals())

def user_detail_view(request, identifier):
    try:
        user = get_user_from_db(identifier=identifier)
    except UserDoestNotExistException:
        return HttpResponse(status=404)
    else:
        keyvalues = user.key_values.all()


    if request.method == 'POST':
        pass
    return render(request, 'user_detail.html', locals())

def add_key_view(request, identifier):
    try:
        user = get_user_from_db(identifier=identifier)
    except UserDoestNotExistException:
        return HttpResponse(status=404)

    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        if not key or not value:
            return HttpResponse('Invalid input form data!',status=400)
        KeyValue.objects.create(key=key, value=value, user=user)
        # TODO: redirect using url names
        return redirect('/user-detail/{}'.format(identifier))
    else:
        user_id = str(user.id)
        return render(request, 'add_key.html', locals())


