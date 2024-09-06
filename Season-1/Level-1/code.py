#!/usr/bin/env python3
'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal as D, getcontext as gc

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')



def validorder(order: Order):
    net = D(0)
    for item in order.items:
        try:
            de = D(item.description.split('_')[-1])
            if de != 'NaN' and de > 10:
                return "Total amount payable for an order exceeded"
        except:
            pass
        if item.type == 'payment':
            net += D(item.amount).quantize(D('0.01'))
        elif item.type == 'product':
            net -= D(item.amount).quantize(D('0.01')) * D(item.quantity).quantize(D('0.01'))
        else:
            return "Invalid item type: %s" % item.type

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id



''' alt
    Order = namedtuple('Order', 'id, items')
    Item = namedtuple('Item', 'type, description, amount, quantity')
    MAX_PAY = 1e5
    MAX_EXP = 1e6


    def validorder(order: Order):
        pay = D(0)
        exp = D(0)
        for item in order.items:
            if item.type == 'payment':
                if abs(item.amount) <= MAX_PAY:
                    pay += D(item.amount).quantize(D('0.01'))
            elif item.type == 'product':
                if type(item.quantity) is int and 0 < item.quantity <= 100 and 0 < item.amount <= MAX_EXP:
                    exp += D(item.amount * item.quantity).quantize(D('0.01'))
            else:
                return "Invalid item type: %s" % item.type

        if abs(pay) > MAX_PAY or exp > MAX_EXP:
            return "Total amount payable for an order exceeded"

        if pay != exp:
            return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, pay - exp)
        else:
            return "Order ID: %s - Full payment received!" % order.id
'''
