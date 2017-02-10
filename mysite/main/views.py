import json
import logging

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def proxy(request, api = 'default', args = ''):
    logging.warning(request)
    logging.warning(api)

    return HttpResponse('api:' + json.dumps(api) + '\nargs:' + args)
