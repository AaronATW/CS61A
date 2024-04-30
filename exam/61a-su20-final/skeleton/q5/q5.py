email = 'example_key'


"""
This question is in 4 parts (a) - (d). If you want to run the tests for
    later parts, you need to do the parts in order.

NOTE: in all parts, you can assume that there are never two items with the same name

"""

class Item:

    def __init__(self, name, price, type):
        """
        An instance of the Item class has three attributes: the name of the
        item, the price of the item, and the type of food that item is.
        """
        self.name = name
        self.price = price
        self.type = type

    def __repr__(self):
        """
        The __repr__ method for the Item class. Defined for you so that the
        output of GroceryList methods is easier to understand.

        >>>> tomato = Item("tomato", 4, "vegetable")
        >>>> tomato
        tomato
        """
        return self.name

class GroceryList:

    def __init__(self, items):
        """
        Part (a)

        A GroceryList is a class that represents a list of items that need to
        be bought. Each item is represented with the Item class defined
        above.

        To run tests just for this part, run
            python3 ok -q a

        >>>> tomato = Item("tomato", 4, "vegetable")
        >>>> apple = Item("apple", 2, "fruit")
        >>>> chicken = Item("chicken", 3, "meat")
        >>>> oreos = Item("oreos", 6, "junk_food")
        >>>> stuff = GroceryList([tomato, apple, chicken, oreos])
        >>>> stuff.items
        [tomato, apple, chicken, oreos]
        """
        self.items = items

    def buy_item(self, name):
        """
        Part (b)

        A function that represents buying an item on the GroceryList

        To run tests just for this part run
            python3 ok -q b

        >>>> stuff = GroceryList([tomato, apple, chicken, oreos])
        >>>> stuff.buy_item("apple")
        >>>> stuff.items
        [tomato, chicken, oreos]
        """
        i = 0
        while i < len(self.items):
            item = self.items[i]
            if item.name == name:
                self.items.remove(item)
            i = i + 1

    def buy_cheapest(self):
        """
        Part (c)

        A function that represents buying the item on the GroceryList that
        is the least expensive. If two items have the same price, it
        should buy the first one.

        To run tests just for this and the previous part run
            python3 ok -q c

        >>>> stuff = GroceryList([tomato, apple, chicken, oreos])
        >>>> stuff.buy_cheapest()
        >>>> stuff.items
        [tomato, chicken, oreos]
        """
        cheapest = min(self.items, key = lambda item: item.price)
        self.items.remove(cheapest)

    def generate_list(self, dollars_available, types):
        """
        Part (d)

        A function that generates a list of items of specific types to
        buy given a certain amount of dollars_available. Note that this does not
        represent buying the items, it only generates a list of them. It
        should *generate* them in the order that they appear in self.items

        To run tests just for this part run
            python3 ok -q d

        >>>> [item for item in stuff.generate_list(10, ["meat"])]
        [chicken]
        >>>> grocery_list = stuff.generate_list(10, ["meat"])
        >>>> next(grocery_list)
        chicken
        """
        spent = 0
        i = 0
        while i < len(self.items) and spent < dollars_available and len(types) > 0:
            item = self.items[i]
            if item.type in types and spent + item.price <= dollars_available:
                spent = spent + item.price
                yield item
            i = i + 1

# ORIGINAL SKELETON FOLLOWS


# """
# This question is in 4 parts (a) - (d). If you want to run the tests for
#     later parts, you need to do the parts in order.

# NOTE: in all parts, you can assume that there are never two items with the same name

# """

# class Item:

#     def __init__(self, name, price, type):
#         """
#         An instance of the Item class has three attributes: the name of the
#         item, the price of the item, and the type of food that item is.
#         """
#         self.name = name
#         self.price = price
#         self.type = type

#     def __repr__(self):
#         """
#         The __repr__ method for the Item class. Defined for you so that the
#         output of GroceryList methods is easier to understand.

#         >>>> tomato = Item("tomato", 4, "vegetable")
#         >>>> tomato
#         tomato
#         """
#         return self.name

# class GroceryList:

#     def __init__(self, items):
#         """
#         Part (a)

#         A GroceryList is a class that represents a list of items that need to
#         be bought. Each item is represented with the Item class defined
#         above.

#         To run tests just for this part, run
#             python3 ok -q a

#         >>>> tomato = Item("tomato", 4, "vegetable")
#         >>>> apple = Item("apple", 2, "fruit")
#         >>>> chicken = Item("chicken", 3, "meat")
#         >>>> oreos = Item("oreos", 6, "junk_food")
#         >>>> stuff = GroceryList([tomato, apple, chicken, oreos])
#         >>>> stuff.items
#         [tomato, apple, chicken, oreos]
#         """
#         self.items = ______

#     def buy_item(self, name):
#         """
#         Part (b)

#         A function that represents buying an item on the GroceryList

#         To run tests just for this part run
#             python3 ok -q b

#         >>>> stuff = GroceryList([tomato, apple, chicken, oreos])
#         >>>> stuff.buy_item("apple")
#         >>>> stuff.items
#         [tomato, chicken, oreos]
#         """
#         i = ______
#         while ______:
#             item = ______
#             if ______:
#                 ______
#             ______

#     def buy_cheapest(self):
#         """
#         Part (c)

#         A function that represents buying the item on the GroceryList that
#         is the least expensive. If two items have the same price, it
#         should buy the first one.

#         To run tests just for this and the previous part run
#             python3 ok -q c

#         >>>> stuff = GroceryList([tomato, apple, chicken, oreos])
#         >>>> stuff.buy_cheapest()
#         >>>> stuff.items
#         [tomato, chicken, oreos]
#         """
#         cheapest = min(______, key = ______)
#         ______

#     def generate_list(self, dollars_available, types):
#         """
#         Part (d)

#         A function that generates a list of items of specific types to
#         buy given a certain amount of dollars_available. Note that this does not
#         represent buying the items, it only generates a list of them. It
#         should *generate* them in the order that they appear in self.items

#         To run tests just for this part run
#             python3 ok -q d

#         >>>> [item for item in stuff.generate_list(10, ["meat"])]
#         [chicken]
#         >>>> grocery_list = stuff.generate_list(10, ["meat"])
#         >>>> next(grocery_list)
#         chicken
#         """
#         spent = 0
#         i = 0
#         while ______ and ______:
#             item = ______
#             if ______ and ______:
#                 ______
#                 ______
#             ______
