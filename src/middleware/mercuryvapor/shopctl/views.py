from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.template import loader
import json
from .models import *


# utility functions
def genhdr(rq):
    hdr = loader.get_template('shopctl/header.html')
    return hdr.render({
        'links': ['customers', 'sources', 'categories', 'procbills']
    }, rq)

def genstyle(rq):
    sty = loader.get_template('shopctl/styles.html')
    return sty.render({}, rq)

def symtab(rq):
    return {
        'hdrfrag': genhdr(rq),
        'stylefrag': genstyle(rq)
    }

# pages
def custpage(rq):
    tmpl = loader.get_template('shopctl/customers.html')
    cs = Customer.objects.all()
    d = symtab(rq)
    d['customers'] = cs
    return HttpResponse(tmpl.render(d, rq))

def srcpage(rq):
    tmpl = loader.get_template('shopctl/sources.html')
    ss = Source.objects.all()
    d = symtab(rq)
    d['sources'] = ss
    return HttpResponse(tmpl.render(d, rq))

def catpage(rq):
    tmpl = loader.get_template('shopctl/categories.html')
    cats = Category.objects.all()
    d = symtab(rq)
    d['categories'] = cats
    return HttpResponse(tmpl.render(d, rq))

def procbillpage(rq):
    tmpl = loader.get_template('shopctl/procbills.html')
    pbs = Procbill.objects.all()
    d = symtab(rq)
    d['procbills'] = pbs
    return HttpResponse(tmpl.render(d, rq))

def purchasepage(rq):
    tmpl = loader.get_template('shopctl/purchases.html')
    ps = Purchase.objects.all()
    d = symtab(rq)
    d['purchases'] = ps
    return HttpResponse(tmpl.render(d, rq))

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
        rj.append(c.dictform())
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
    cj = c.dictform()
    c.delete()
    return JsonResponse(cj)

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
        rj.append(s.dictform())
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
    rj = s.dictform()
    s.delete()
    return JsonResponse(rj)

# category curd
@require_GET
def get_categories(rq):
    cats = Category.objects.all()
    rj = []
    for c in cats:
        rj.append(c.dictform())
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
    cj = c.dictform()
    c.delete()
    return JsonResponse(cj)

# procbill curd
@require_GET
def get_procbills(rq):
    pbs = Procbill.objects.all()
    rj = []
    for p in pbs:
        rj.append(p.dictform())
    return JsonResponse({'d': rj})

@require_POST
def create_procbill(rq):
    pbj = json.loads(rq.body.decode('utf-8'))
    src = Source.objects.get(pk=pbj['sourceid'])
    pb = Procbill(paid=pbj['paid'], source=src)
    pb.save()
    return JsonResponse(pb.dictform())

@require_POST
def edit_procbill(rq, pbid):
    pbj = json.loads(rq.body.decode('utf-8'))
    pb = Procbill.objects.get(pk=pbid)
    src = pb.source
    pb.paid = pbj['paid']
    pb.save()
    return JsonResponse(pb.dictform())

# for now do not allow deletion of procbills

# purchase curd
@require_POST
def create_purchase(rq):
    pj = json.loads(rq.body.decode('utf-8'))
    cat = Category.objects.get(pk=pj['categoryid'])
    pb = Procbill.objects.get(pk=pj['procbillid'])
    p = Purchase(category=cat, qty=pj['qty'], price=pj['price'], procbill=pb)
    p.save()
    pj['id'] = p.id
    return JsonResponse(pj)

@require_GET
def get_purchases(rq):
    ps = Purchase.objects.all()
    rj = []
    for p in ps:
        rj.append(p.dictform())
    return JsonResponse({'d': rj})

# since a purchase is transactional let us not allow its updation/deletion

# batch curd
@require_POST
def create_batch(rq):
    bj = json.loads(rq.body.decode('utf-8'))
    p = Purchase.objects.get(pk=bj['purchaseid'])
    b = Batch(expireson=bj['expireson'], sp=bj['sp'], purchase=p)
    b.save()
    bj['id'] = b.id
    return JsonResponse(bj)

@require_GET
def get_batches(rq):
    bs = Batch.objects.all()
    rj = []
    for b in bs:
        rj.append(b.dictform())
    return JsonResponse({'d': rj})

@require_POST
def edit_batch(rq, bid):
    b = Batch.objects.get(pk=bid)
    bj = json.loads(rq.body.decode('utf-8'))
    if bj['purchaseid'] != b.purchase.id:
        p = Purchase.objects.get(pk=bj['purchaseid'])
        b.purchase = p
    b.sp = bj['sp']
    b.expireson = bj['expireson']
    b.save()
    return JsonResponse(bj)

# delete batch does not make sense

# custbill curd
@require_POST
def create_custbill(rq):
    cbj = json.loads(rq.body.decode('utf-8'))
    c = Customer.objects.get(pk=cbj['customerid'])
    cb = Custbill(paid=cbj['paid'], customer=c)
    cb.save()
    return JsonResponse(cb.dictform())

@require_GET
def get_custbills(rq):
    rj = []
    for cb in Custbill.objects.all():
        rj.append(cb.dictform())
    return JsonResponse({'d': rj})

@require_GET
def custbill_paid(rq, cbid):
    cb = Custbill.objects.get(pk=cbid)
    cb.paid = 1
    cb.save()
    return JsonResponse(cb.dictform())

# no deletion required for customer bills, maybe archiving at a later point

# sale curd
@require_POST
def create_sale(rq):
    sj = json.loads(rq.body.decode('utf-8'))
    b = Batch.objects.get(pk=sj['batchid'])
    cb = Custbill.objects.get(pk=sj['custbillid'])
    s = Sale(batch=b, qty=sj['qty'], price=sj['price'], custbill=cb)
    s.save()
    return JsonResponse(s.dictform())

@require_GET
def get_sales(rq):
    rj = []
    for s in Sale.objects.all():
        rj.append(s.dictform())
    return JsonResponse({'d': rj})

