# coding: utf-8
__author__ = 'Evolutiva'

import json
import urllib
import urllib2


class poderopedia(object):

    def __init__(self,base_url='http://api.poderopedia.org/visualizacion/',user_key=None):
        self.base_url='http://api.poderopedia.org/visualizacion/'
        self.user_key=user_key
        self.search_url='search'
        self.connection='connection'
        self.getEntityById='getEntityById'

    def search(self, entity='persona',alias=None):
        result=dict()
        url = self.base_url+self.search_url
        if alias is not None:
            values={'user_key':self.user_key,'entity':entity,'alias':alias}
            data = urllib.urlencode(values)
            req = urllib2.Request(url+'?'+data)
            try:
                response = urllib2.urlopen(req)
            except:
                response = None

            if response is not None:
                result=json.loads(response.read())

        return result

    def get_connections(self,entity='persona',id=None):
        result=dict()
        url = self.base_url+self.connection
        if id is not None:
            values={'user_key':self.user_key,'entity':entity,'id':id}
            data = urllib.urlencode(values)
            req = urllib2.Request(url+'?'+data)
            try:
                response = urllib2.urlopen(req)
            except:
                response = None

            if response is not None:
                result=json.loads(response.read())

        return result

    def get_entity_by_id(self,entity='persona',id=None):
        result=dict()
        url = self.base_url+self.getEntityById
        if id is not None:
            values={'user_key':self.user_key,'entity':entity,'id':id}
            data = urllib.urlencode(values)
            req = urllib2.Request(url+'?'+data)
            try:
                response = urllib2.urlopen(req)
            except:
                response = None

            if response is not None:
                result=json.loads(response.read())

        return result