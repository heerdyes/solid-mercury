from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import *
from django.core.exceptions import PermissionDenied
import json 

def create_customer(rq):
    if rq.method !='POST':
        raise PermissionDenied
    jsonstr = rq.body.decode('utf-8')
    cust = json.loads(jsonstr)
    print(cust)
    # create customer
    c = Customer(name=cust['name'],phnum=cust['phnum'])
    c.save()
    return JsonResponse({
        'status':'ok'
    })

def create_source(rq):
    # Ensure the request method is POST
    if rq.method != 'POST':
        raise PermissionDenied

    # Decode the request body and load it as JSON
    try:
        request_data = json.loads(rq.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    # Extract relevant data from the request_data
    est_name = request_data.get('estname', '')
    est_type = request_data.get('esttype', '')
    owner = request_data.get('owner', '')
    ph_num = request_data.get('phnum', '')
    address = request_data.get('address', '')

    # Create the source (replace this with your actual logic)
    # For example, you might want to use a Django model to save the data to the database.
    # Here, I'm just returning the extracted data as a response.
    response_data = {
        'estname': est_name,
        'esttype': est_type,
        'owner': owner,
        'phnum': ph_num,
        'address': address,
    }

    return JsonResponse(response_data)

def create_category(rq):
    if rq.method != 'POST':
        raise PermissionDenied
    
    try:
        request_data = json.loads(rq.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    category = Category.objects.create(
        generalname=request_data.get('generalname', ''),
        specificname=request_data.get('specificname', ''),
        comments=request_data.get('comments', '')
    )

    return JsonResponse({
        'generalname': category.generalname,
        'specificname': category.specificname,
        'comments': category.comments,
    })