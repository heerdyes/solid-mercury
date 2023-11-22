import requests
import json

proto = 'http'
host = '127.0.0.1'
port = '8000'
pfix = 'api/v0/'
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
    print(response.text)

def yr():
    url = apiurl + 'categories'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    cats = response.json()
    for c in cats['d']:
        print('[%d] %s <%s> (%s)'%(c['id'], c['generalname'], c['specificname'], c['comments']))

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
    print(response.text)

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
    print(response.text)

def sr():
    url = apiurl + 'sources'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    ss = response.json()
    for s in ss['d']:
        print('[%d] %s <%s> c/o: %s (%s), %s'%(s['id'], s['estname'], s['esttype'], s['owner'], s['phnum'], s['address']))

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
    print(response.text)

def sd():
    url = apiurl + 'deletesource/' + input('sourceid: ')
    payload = {}
    headers = {}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.text)

def cr():
    url = apiurl + 'customers'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    cs = response.json()
    for c in cs['d']:
        print('[%d] %s (%s)'%(c['id'], c['name'], c['phnum']))

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
    print(response.text)

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
    print(response.text)

def cd():
    url = apiurl + 'deletecustomer/' + input('custid: ')
    payload = {}
    headers = {}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.text)

# flow
while True:
    print('\n---- entity menu ----')
    print('c. customer')
    print('s. source')
    print('y. category')
    print('q. quit')
    ch = input('-> ')
    if ch == 'q':
        break
    elif ch == 'y':
        while True:
            x = input('\nchoose (c/u/r/d/q): ')
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
            x = input('\nchoose (c/u/r/d/q): ')
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
            x = input('\nchoose (c/u/r/d/q): ')
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

