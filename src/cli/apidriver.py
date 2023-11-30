import requests
import json
from conf import *

apiurl = '%s://%s:%s/%s' % (proto, host, port, pfix)

def yc():
    url = apiurl + 'createcategory'
    payload = json.dumps({
      "generalname": input('generalname: '),
      "specificname": input('specificname: '),
      "comments": input('comments: ')
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def yr():
    url = apiurl + 'categories'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def yu():
    url = apiurl + 'editcategory/' + input('catid: ')
    payload = json.dumps({
      "generalname": input('generalname: '),
      "specificname": input('specificname: '),
      "comments": input('comments: ')
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def sc():
    url = apiurl + 'createsource'
    payload = json.dumps({
      "estname": input('estname: '),
      "esttype": input('esttype: '),
      "owner": input('owner: '),
      "phnum": input('phnum: '),
      "address": input('address: ')
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def sr():
    url = apiurl + 'sources'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def su():
    url = apiurl + 'editsource/' + input('sourceid: ')
    payload = json.dumps({
      "estname": input('new estname: '),
      "esttype": input('new est type: '),
      "owner": input('new owner: '),
      "phnum": input('new phnum: '),
      "address": input('new address: ')
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def sd():
    url = apiurl + 'deletesource/' + input('sourceid: ')
    payload = {}
    headers = {}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def cr():
    url = apiurl + 'customers'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def cc():
    url = apiurl + 'createcustomer'
    payload = json.dumps({
      "name": input('name: '),
      "phnum": input('phnum: ')
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def cu():
    url = apiurl + 'editcustomer/' + input('custid: ')
    nm = input('  new name: ')
    pn = input('  new phnum: ')
    payload = json.dumps({
      "name": nm,
      "phnum": pn
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def cd():
    url = apiurl + 'deletecustomer/' + input('custid: ')
    payload = {}
    headers = {}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def pc():
    url = apiurl + 'createprocbill'
    print('/// sources:')
    sr()
    payload = json.dumps({
      "paid": int(input('paid: ')),
      "sourceid": int(input('sourceid: '))
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def pr():
    url = apiurl + 'procbills'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def pu():
    url = apiurl + 'editprocbill/' + input('pbid: ')
    payload = json.dumps({
      "paid": int(input('paid: '))
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def uc():
    url = apiurl + 'createpurchase'
    print('/// categories:')
    yr()
    print('/// procbills:')
    pr()
    payload = json.dumps({
      'categoryid': int(input('[category] catid: ')),
      'qty': float(input('[category] qty: ')),
      'price': float(input('[category] price: ')),
      'procbillid': int(input('[category] procbillid: '))
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def ur():
    url = apiurl + 'purchases'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def bc():
    url = apiurl + 'createbatch'
    print('/// purchases:')
    ur()
    payload = json.dumps({
      'expireson': input('expireson: '),
      'sp': float(input('sp: ')),
      'purchaseid': int(input('purchaseid: '))
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def br():
    url = apiurl + 'batches'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def bu():
    url = apiurl + 'editbatch/' + input('[batch] batchid: ')
    print('/// purchases:')
    ur()
    payload = json.dumps({
      'expireson': input('expireson: '),
      'sp': float(input('sp: ')),
      'purchaseid': int(input('purchaseid: '))
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def tc():
    url = apiurl + 'createcustbill'
    print('/// customers:')
    cr()
    payload = json.dumps({
      'paid': int(input('paid: ')),
      'customerid': int(input('customerid: '))
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def tr():
    url = apiurl + 'custbills'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

def tp():
    print('/// custbills:')
    tr()
    url = apiurl + 'custbillpaid/' + input('[custbill] custbillid: ')
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent=2))

# flow
while True:
    print('\n---- entity menu ----')
    print('c. customer')
    print('s. source')
    print('y. category')
    print('p. procbill')
    print('u. purchase')
    print('b. batch')
    print('t. custbill')
    print('q. quit')
    ch = input('-> ')
    if ch == 'q':
        break
    if ch == 't':
        while True:
            x = input('\n[custbill] choose (c/p/r/d/q): ')
            if x == 'q':
                break
            if x == 'c':
                tc()
            elif x == 'r':
                tr()
            elif x == 'p':
                tp()
    elif ch == 'b':
        while True:
            x = input('\n[batch] choose (c/u/r/d/q): ')
            if x == 'q':
                break
            if x == 'c':
                bc()
            elif x == 'r':
                br()
            elif x == 'u':
                bu()
    elif ch == 'u':
        while True:
            x = input('\n[purchase] choose (c/r/q): ')
            if x == 'q':
                break
            if x == 'c':
                uc()
            elif x == 'r':
                ur()
    elif ch == 'p':
        while True:
            x = input('\n[procbill] choose (c/u/r/q): ')
            if x == 'q':
                break
            if x == 'c':
                pc()
            elif x == 'r':
                pr()
            elif x == 'u':
                pu()
    elif ch == 'y':
        while True:
            x = input('\n[category] choose (c/u/r/d/q): ')
            if x == 'q':
                break
            if x == 'c':
                yc()
            elif x == 'r':
                yr()
            elif x == 'u':
                yu()
            else:
                print('unknown choice:', x)
    elif ch == 's':
        while True:
            x = input('\n[source] choose (c/u/r/d/q): ')
            if x == 'q':
                break
            if x == 'c':
                sc()
            elif x == 'r':
                sr()
            elif x == 'u':
                su()
            elif x == 'd':
                sd()
            else:
                print('unknown choice:', x)
    elif ch == 'c':
        while True:
            x = input('\n[customer] choose (c/u/r/d/q): ')
            if x == 'q':
                break
            if x == 'r':
                cr()
            elif x == 'c':
                cc()
            elif x == 'u':
                cu()
            elif x == 'd':
                cd()
            else:
                print('unknown choice:', x)

