import time
from celery import group, chord
from celery.result import AsyncResult
from celery_app import app
from itertools import zip_longest
from random import randint

#def get_results(result_obj, index):
#    res = AsyncResult(result_obj[index].task_id)
#    return res

@app.task
def sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
#    spliting = group(sort.si(array[:mid]),
#                     sort.si(array[mid:]))

    # How to pass splitted arrays to merge?
#    result = chord(spliting)(merge.s())
    left = sort(array[:mid])
    right = sort(array[mid:])
    return merge(left, right)
#    return result


#@app.task
def merge(left, right):
#    left = arrays[0]
#    right = arrays[1]
#
#    if not isinstance(right, list) or not isinstance(left, list):
#        return arrays, 'NEKOI NE E LISTTTT'
#    for x in left:
#        if not isinstance(x, int):
#            return left, 'NEKOI NE E INT'
#    for x in right:
#        if not isinstance(x, int):
#            return right, 'NEKOI NE E INT'

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result
