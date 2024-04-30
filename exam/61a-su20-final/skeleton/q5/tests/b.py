test = {
  'name': 'b',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> tomato = Item("tomato", 4, "vegetable")
          
          >>> kale = Item("kale", 1, "vegetable")
          
          >>> apple = Item("apple", 2, "fruit")
          
          >>> chicken = Item("chicken", 3, "meat")
          
          >>> oreos = Item("oreos", 6, "junk_food")
          
          >>> stuff = GroceryList([tomato, kale, apple, chicken, oreos])
          
          >>> stuff.items
          [tomato, kale, apple, chicken, oreos]
          
          >>> stuff.buy_item("chicken")
          
          >>> stuff.items
          [tomato, kale, apple, oreos]
          
          >>> stuff.buy_item("kale")
          
          >>> stuff.items
          [tomato, apple, oreos]
          
          >>> stuff.buy_item("tomato")
          
          >>> stuff.items
          [apple, oreos]
          
          >>> stuff.buy_item("apple")
          
          >>> stuff.items
          [oreos]
          
          >>> stuff.buy_item("oreos")
          
          >>> stuff.items
          []
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
