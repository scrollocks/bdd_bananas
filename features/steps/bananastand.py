from behave import *
from stand import *

frozen_banana_recipe = { "bananas": 1, "nuts": 1, "choc": 1 } #Yum!

@given(u'we have have a banana stand with inventory')
def step_impl(context):
    inventory = {}
    for row in context.table:
        inventory.setdefault( row['items'], int(row['qty']) )

    context.banana_stand = Stand( inventory_from_dict=inventory )
    context.initial_inventory = inventory

@when(u'we sell {qty:d} frozen bananas at {price:f} each')
def step_impl(context, qty, price ):
    for i in range( qty ):
        context.banana_stand.sell_product( frozen_banana_recipe, price )


@then(u'we will have total sales of {sales:f}')
def step_impl(context, sales):
    assert sales == context.banana_stand.total_sales

@then(u'we will have total quantity sold of {qty:d}')
def step_impl(context, qty):
    assert qty == context.banana_stand.total_products_sold
