from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_GET, require_POST, require_http_methods
import json
from .models import *


# customer curd
@require_POST
def create_customer(rq):
    cust = json.loads(rq.body.decode('utf-8'))
    c = Customer(name=cust['name'], phnum=cust['phnum'])
    c.save()
    cust['id'] = c.id
    return JsonResponse(cust)

@require_GET
def get_customers(rq):
    cs = Customer.objects.all()
    rj = []
    for c in cs:
        rj.append({
            'id': c.id,
            'name': c.name,
            'phnum': c.phnum
        })
    return JsonResponse({'d': rj})

@require_POST
def edit_customer(rq, custid):
    jsonstr = rq.body.decode('utf-8')
    cust = json.loads(jsonstr)
    c = Customer.objects.get(pk=custid)
    c.name = cust['name']
    c.phnum = cust['phnum']
    c.save()
    return JsonResponse(cust)

@require_http_methods(['DELETE'])
def delete_customer(rq, custid):
    c = Customer.objects.get(pk=custid)
    cust = {
        'id': c.id,
        'name': c.name,
        'phnum': c.phnum
    }
    c.delete()
    return JsonResponse(cust)

# source curd
@require_POST
def create_source(rq):
    src = json.loads(rq.body.decode('utf-8'))
    s = Source(estname=src['estname'], esttype=src['esttype'], owner=src['owner'], phnum=src['phnum'], address=src['address'])
    s.save()
    src['id'] = s.id
    return JsonResponse(src)

@require_GET
def get_sources(rq):
    srcs = Source.objects.all()
    rj = []
    for s in srcs:
        rj.append({
            'id': s.id,
            'estname': s.estname,
            'esttype': s.esttype,
            'owner': s.owner,
            'phnum': s.phnum,
            'address': s.address
        })
    return JsonResponse({'d': rj})

@require_POST
def edit_source(rq, srcid):
    sj = json.loads(rq.body.decode('utf-8'))
    s = Source.objects.get(pk=srcid)
    s.estname = sj['estname']
    s.esttype = sj['esttype']
    s.owner = sj['owner']
    s.phnum = sj['phnum']
    s.address = sj['address']
    s.save()
    return JsonResponse(sj)

@require_http_methods(['DELETE'])
def delete_source(rq, srcid):
    s = Source.objects.get(pk=srcid)
    rj = {
        'id': s.id,
        'estname': s.estname,
        'esttype': s.esttype,
        'owner': s.owner,
        'phnum': s.phnum,
        'address': s.address
    }
    s.delete()
    return JsonResponse(rj)

# category curd
@require_GET
def get_categories(rq):
    cats = Category.objects.all()
    rj = []
    for c in cats:
        rj.append({
            'id': c.id,
            'generalname': c.generalname,
            'specificname': c.specificname,
            'comments': c.comments
        })
    return JsonResponse({'d': rj})

@require_POST
def create_category(rq):
    cj = json.loads(rq.body.decode('utf-8'))
    c = Category(generalname=cj['generalname'], specificname=cj['specificname'], comments=cj['comments'])
    c.save()
    cj['id'] = c.id
    return JsonResponse(cj)

@require_POST
def edit_category(rq, catid):
    c = Category.objects.get(pk=catid)
    cj = json.loads(rq.body.decode('utf-8'))
    c.generalname = cj['generalname']
    c.specificname = cj['specificname']
    c.comments = cj['comments']
    c.save()
    return JsonResponse(cj)

@require_http_methods(['DELETE'])
def delete_category(rq, catid):
    c = Category.objects.get(pk=catid)
    cj = {
        'id': c.id,
        'generalname': c.generalname,
        'specificname': c.specificname,
        'comments': c.comments
    }
    c.delete()
    return JsonResponse(cj)

# procbill curd
@require_GET
def get_procbills(rq):
    pbs = Procbill.objects.all()
    rj = []
    for p in pbs:
        rj.append({
            'id': p.id,
            'createdon': p.createdon,
            'paid': p.paid,
            'source': {
                'estname': p.source.estname,
                'esttype': p.source.esttype,
                'owner': p.source.owner,
                'phnum': p.source.phnum,
                'address': p.source.address
            }
        })
    return JsonResponse({'d': rj})

@require_POST
def create_procbill(rq, srcid):
    pbj = json.loads(rq.body.decode('utf-8'))
    src = Source.objects.get(pk=srcid)
    pb = Procbill(paid=pbj['paid'], source=src)
    pb.save()
    pbj['id'] = pb.id
    pbj['createdon'] = pb.createdon
    pbj['source'] = {
        'estname': src.estname,
        'esttype': src.esttype,
        'owner': src.owner,
        'phnum': src.phnum,
        'address': src.address
    }
    return JsonResponse(pbj)

