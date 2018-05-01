from behave import *
from stand import *

@then(u'the inventory will match')
def step_impl(context):
    success = True
    for row in context.table:
        if not row['items'] in context.banana_stand.inventory.items.keys():
            success = False
        elif int(row['qty']) != context.initial_inventory[ row['items'] ]:
            success = False
        
    assert success

