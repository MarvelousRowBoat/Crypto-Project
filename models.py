from datetime import datetime
from typing import Any
import time


class Property:

    properties = []

    def __init__(self, name, amount, owner=None):
        self.id = len(self.properties)
        self.name = name
        self.owner = owner
        self.amount = amount
        self.transaction_history = []
        self.properties.append(self)

    def viewProperties(self):
        for property in self.properties:
            print(property.id , property.name , property.owner.username , property.amount)


class Transaction:

    def __init__(self, seller, buyer, property):
        self.buyer = buyer
        self.seller = seller
        self.propertyId = property.id
        self.propertyName = property.name
        self.timestamp = time.time()
        self.transactionId = str(hash(buyer.username + property.name))
        
        property.owner = buyer


class User:

    users = []

    def __init__(self, username, password, wealth=1500):
        self.username = username
        self.password = password
        self.wealth = wealth
        self.assets = {}
        self.users.append(self)

    def viewMoney(self):
        return self.wealth
    
    def addMoney(self, amount):
        self.wealth += amount

    def add_property(self, property):   
        self.wealth -= property.amount
        self.assets[property.id] = property
        property.owner = self

    def register_property(self, property):   
        self.assets[property.id] = property
        property.owner = self

    def remove_property(self, property):
        self.wealth += property.amount
        del self.assets[property.id]

    def get_assets(self):
        for key in self.assets:
            print(str(key) + ':', self.assets[key].name)
