test = {
  'name': 'q5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> tomato = Item("tomato", 4, "vegetable")
          
          >>> tomato
          tomato
          
          >>> tomato = Item("tomato", 4, "vegetable")
          
          >>> apple = Item("apple", 2, "fruit")
          
          >>> chicken = Item("chicken", 3, "meat")
          
          >>> oreos = Item("oreos", 6, "junk_food")
          
          >>> stuff = GroceryList([tomato, apple, chicken, oreos])
          
          >>> stuff.items
          [tomato, apple, chicken, oreos]
          
          >>> stuff = GroceryList([tomato, apple, chicken, oreos])
          
          >>> stuff.buy_cheapest()
          
          >>> stuff.items
          [tomato, chicken, oreos]
          
          >>> stuff = GroceryList([tomato, apple, chicken, oreos])
          
          >>> stuff.buy_item("apple")
          
          >>> stuff.items
          [tomato, chicken, oreos]
          
          >>> [item for item in stuff.generate_list(10, ["meat"])]
          [chicken]
          
          >>> grocery_list = stuff.generate_list(10, ["meat"])
          
          >>> next(grocery_list)
          chicken
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q5 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
