"""
This toy code simulates a stand that sells frozen bananas. You could sell anything you
want really, 

* The stand has an inventory, which is populated when a new stand is created.
* As sales are made, items in the inventory are consumed and sales totals and quantities arae calculated
"""

class Stand():
    """Represents a Stand that sells something

    Arguments:
    inventory -- An dict of {string: int} pairs that represent ingredients available to the stand.

    """
    class Inventory():
        """Represents the stand inventory of ingredients
        
        Keyword Arguments:

        items -- a dictionary of ingredients and their quantities of the form { string: integer }

        """

        def __init__( self, items={} ):
            """Create a new inventory object with optional items """
            self.items = items

        def add_item( self, item_name, item_qty ):
            """Add an item and its quantity to the inventory. If it already exists, increment its quantity.
               Returns the inventory {item:qty} dict of the item and the new quantity available { string: int }
            """
            if item_name in self.items.keys():
                # Increment the quantity if it already exists
                self.items[ item_name ] += item_qty
            else:
                # Add the item if it doesn't exist
                self.items.setdefault( item_name, item_qty )

            return self.items[ item_name ]

        def has_item( self, item_name, item_qty ):
            """Returns an item dict from the inventory if the given {item:qty} exists in sufficient quantity, or None"""
            if item_name in self.items.keys():
                if self.items[ item_name ] >= item_qty:
                    return self.items[ item_name ]
            return None

        def has_items( self, item_dict ):
            """Returns True or False if all {item:qty} pairs in a given dict exist in the inventory in sufficient quantity """
            for k, v in item_dict.items():
                if not self.has_item( k, v ):
                    return False 

            return True

        def use_items( self, items_dict ):
            """Returns a dict of {item:qty} pairs consumed from inventory, given a dict of {item:qty} to consume.
               All given {item:qty} pairs must exist and have sufficient quantity.
            """
            changed_items = {}

            if self.has_items( items_dict ):
                for k, v in items_dict.items():
                    self.items[ k ] -= v
                    changed_items[ k ] = self.items[ k ]
                return changed_items
            else:    
                return {}
       
        def __repr__( self ):
            return "<Inventory: {}>".format( self.items.items() )


    def __init__( self, inventory_from_dict={} ):
        """Returns a new Stand with an inventory, total sales and total quantity sold """
        self.inventory           = self.Inventory( items=inventory_from_dict )
        self.total_sales         = 0.0
        self.total_products_sold = 0

    def sell_product( self, recipe, sale_price ):
        """Returns True/False outcome of sale. Returns True if all recipe ingredients exist in inventory """
        if self.inventory.has_items( recipe ):
            self.inventory.use_items( recipe )
            self.total_sales += sale_price
            self.total_products_sold += 1
            return True
        return False

    def __repr__( self ):
        return "<Stand - Sales: {} Product sold: {}>".format( self.total_sales, self.total_products_sold ) 

def main():

    # What we're selling
    frozen_banana_recipe = { "bananas": 1, "nuts": 1, "choc": 1 }
    # What we're charging
    frozen_banana_price  = 4.50

    # Our brand new banana stand!
    banana_stand = Stand( inventory_from_dict = {"bananas": 10, "nuts": 10, "choc": 10} ) 
    
    # Initial state
    print( "{} / {}".format( banana_stand, banana_stand.inventory) )

    # Make some sales!
    banana_stand.sell_product( frozen_banana_recipe, frozen_banana_price )
    banana_stand.sell_product( frozen_banana_recipe, frozen_banana_price )
    banana_stand.sell_product( frozen_banana_recipe, frozen_banana_price )
    banana_stand.sell_product( frozen_banana_recipe, frozen_banana_price )
    banana_stand.sell_product( frozen_banana_recipe, frozen_banana_price )

    # Final state
    print( "{} / {}".format( banana_stand, banana_stand.inventory) )

if __name__ == '__main__':
    main()
