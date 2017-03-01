from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your:views here.


def add(request, n, m):
    res = int(n) + int(m)
    result = res

    if request.GET.get('format') == 'json':
        return JsonResponse({'result':result})
    return HttpResponse(result)

def multiply(request, n, m):
    result = int(n) * int(m)
    if request.GET.get('format') == 'json':
        return JsonResponse({'result':result})
    return HttpResponse(result)


def power(request, n, m):
    result = int(n) ** int(m)
    if request.GET.get('format') == 'json':
        return JsonResponse({'result':result})
    return HttpResponse(result)


def fact(request, n):
    result = factorial(int(n))
    if request.GET.get('format') == 'json':

        return JsonResponse({'result':result})
    return HttpResponse(result)


def factorial(n):
    # if n <= 1:
    #     return 1
    # return n * factorial(n - 1)
    i = 1
    result = 1
    while i <= n:
        result *= i
        i += 1
    return result

def format_to_json(inp):
    pass
