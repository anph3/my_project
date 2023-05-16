from rest_framework.response import Response
from configs import response as cr
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from math import ceil

def data_response(data=None, status=cr.STATUS.SUCCESS.value, message=cr.SUCCESS.SUCCESS.value):
    return {
        cr.ResponseKey.STATUS_CODE.value: status,
        cr.ResponseKey.MESSAGE.value: message,
        cr.ResponseKey.DATA.value: data
    }

def response_data(data=None, status=cr.STATUS.SUCCESS.value, message=cr.SUCCESS.SUCCESS.value):
    return Response(data_response(data, status, message))

def json_response(data=None, status=cr.STATUS.SUCCESS.value, message=cr.SUCCESS.SUCCESS.value):
    return JsonResponse(data_response(data, status, message))

def response_paginator(sum, per_page, data):
    result = {
        cr.ResponseKey.MAX_PAGE.value: ceil(sum/per_page),
        cr.ResponseKey.LIST_DATA.value: data
    }
    return response_data(data=result)

def validate_error(data={}, status=cr.STATUS.INPUT_INVALID.value):
    error_message = ''
    if isinstance(data, list):
        for index, item in enumerate(data):
            error_message = 'row {}: {}'.format(str(index), message_errors(item))
        return response_data(status=status, message=error_message)
    error_message = message_errors(data)
    return response_data(status=status, message=error_message)

def message_errors(data={}):
    data = dict(data)
    error_message = ''
    for key, value in data.items():
        error_message += str(key) + ' ' + str(list(value)[0]) + cr.SEPARATE_THE_ERROR
    return str(error_message)
    
