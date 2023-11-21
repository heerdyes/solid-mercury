from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
import json
from .models import *

# Create your views here.
# crud for customer, source and category
def create_customer(rq):
    if rq.method != 'POST':
        raise PermissionDenied
    jsonstr = rq.body.decode('utf-8')
    cust = json.loads(jsonstr)
    print(cust)
    # create customer
    c = Customer(name=cust['name'], phnum=cust['phnum'])
    c.save()
    return JsonResponse({
        'status': 'OK'
    })
