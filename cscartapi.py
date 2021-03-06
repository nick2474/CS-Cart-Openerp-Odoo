# Author: tejas tank, snippetbucket@gmail.com, www.snippetbucket.com
# Its private licensed under permission of snippetbucket.com, you can't share it directly.
# One copy per computer licensed, for more contact at snippetbucket.com or snippetbucket@gmail.com
# or skype: live.snippetbucket

#from requests.auth import HTTPBasicAuth
import requests
import json
import logging
import threading

class CsCart(object):

    url = 'http://cscart.snippetbucket.com'
    auth = ('snippetbucket@gmail.com', 'K272W27rN7a0vwf13adq1N4Q72CbE2Za')
    debug = False
    rewrite = False # website rewrite enabled
    ssl = False

    def __init__(self, url=None, auth=None, debug=False, rewrite=False, ssl=False):
        if url and auth:
            self.url = url
            self.auth = auth
            self.debug = debug
            self.rewrite = rewrite
            self.ssl = ssl

    def get(self, servicename, params={}):
        r = None
        if self.rewrite:
            if self.ssl:
                r = requests.get('%s/api/%s'%(self.url, servicename), verify=self.ssl, auth=self.auth)
                return r.json() 
            else :
                r = requests.get('%s/api/%s'%(self.url, servicename), auth=self.auth)
                return r.json() 
        else:
            if self.ssl:
                r = requests.get('%s/api.php?_d=%s&ajax_custom=1'%(self.url, servicename),verify=self.ssl, auth=self.auth)
                return json.loads(r.content)
            else:
                r = requests.get('%s/api.php?_d=%s&ajax_custom=1'%(self.url, servicename), auth=self.auth,params=params)
                return json.loads(r.content)

    def create(self, servicename, data={}):
        headers = {'content-type': 'application/json'}
        if self.rewrite:
            return requests.post('%s/cscart/api/%s'% (self.url, servicename), auth=self.auth,verify=self.ssl, data=json.dumps(data), headers=headers)
        else:
            return requests.post('%s/api.php?_d=%s'% (self.url, servicename), auth=self.auth,verify=self.ssl, data=json.dumps(data), headers=headers)

    def write(self, servicename, id, data={}):
        headers = {'content-type': 'application/json'}
        if self.rewrite:
            return requests.put('%s/cscart/api/%s/%s'%(self.url, servicename, id), auth=self.auth,verify=self.ssl, data=json.dumps(data), headers=headers)
        else:
            return requests.put('%s/api.php?_d=%s/%s'% (self.url, servicename,id), auth=self.auth,verify=self.ssl, data=json.dumps(data), headers=headers)

    def unlink(self, servicename, id):
        headers = {'content-type': 'application/json'}
        r = requests.delete('%s/cscart/api/%s/%s'%(self.url, servicename, id), auth=self.auth,verify=self.ssl, headers=headers)
        return r.json()

    def putCategories(self, data):
        return self.put('categories')

    def getCategories(self,params={}):
        return self.get('categories', params=params)

    def getCategory(self, id):
        return self.get('categories/%s'%id)

    def getSuppliers(self,params={}):
        return self.get('suppliers', params=params)

    def getSupplier(self, id):
        return self.get('suppliers/%s'%id)

    def getProducts(self,params={}):
        return self.get('products', params=params)

    def getProduct(self, id):
        return self.get('products/%s'%id)

    def getOrders(self,params={}):
        return self.get('orders', params=params)

    def getOrder(self, id):
        return self.get('orders/%s'%id)

    def getPayments(self):
        return self.get('payments')

    def getPayment(self, id):
        return self.get('payment/%s'%id)

    def getShippings(self):
        return self.get('shippings')

    def getShipping(self, id):
        return self.get('shippings/%s'%id)

    def getStatuses(self):
        return self.get('statuses')

    def getStatus(self, id):
        return self.get('statuses/%s'%id)

    def getTaxes(self):
        return self.get('taxes')

    def getTaxe(self, id):
        return self.get('taxes/%s'%id)

    def getUsers(self,params={}):
        return self.get('users',params=params)

    def getUser(self, id):
        return self.get('users/%s'%id)

    def getCountryStates(self,country_code):
        return self.get('states')

    def getCountryState(self, id):
        return self.get('states/%s'%id)

    def getShipments(self):
        return self.get('shipments')

    def getShipment(self, id):
        return self.get('shipments/%s'%id)


    def getpayments(self,params={}):
        return self.get('payments',params=params)

    def getpayment(self, id):
        return self.get('payments/%s'%id)

#ob = CsCart('http://localhost/cscart_v4.1.1',('snippetbucket@gmail.com', 'PB9S31R04aW80O71UZ4f1J65pQfx2Sz6'),False,False,False)

#o = ob.getOrder(124)
#print "\n\nOrder--------->>>>>>>>",o

#o = ob.getpayment(10)
#print "\n\nPayment--------->>>>>>>>",o
#o = ob.getpayments()
#print "\n\nPayments--------->>>>>>>>",o




# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
