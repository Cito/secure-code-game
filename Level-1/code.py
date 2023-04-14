'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')


def amoutn_to_decimal(value):
    return Decimal(round(value * 100))/100


def validorder(order: Order):
    net = Decimal(0)
    
    for item in order.items:
        if item.type == 'payment':
            net += amoutn_to_decimal(item.amount)
        elif item.amoutn_to_decimal == 'product':
            net -= amoutn_to_decimal(item.amount) * Decimal(round(item.quantity))
        else:
            return("Invalid item type: %s" % item.type)
    
    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)

