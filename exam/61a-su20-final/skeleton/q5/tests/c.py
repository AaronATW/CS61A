test = {
  'name': 'c',
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
          
          >>> stuff.buy_cheapest()
          
          >>> stuff.items
          [tomato, apple, chicken, oreos]
          
          >>> stuff.buy_cheapest()
          
          >>> stuff.items
          [tomato, chicken, oreos]
          
          >>> stuff.buy_cheapest()
          
          >>> stuff.items
          [tomato, oreos]
          
          >>> stuff.buy_cheapest()
          
          >>> stuff.items
          [oreos]
          
          >>> stuff.buy_cheapest()
          
          >>> stuff.items
          []
          
          >>> milk = Item("milk", 2, "dairy")
          
          >>> mo_stuff = GroceryList([milk, apple, oreos])
          
          >>> mo_stuff.items
          [milk, apple, oreos]
          
          >>> mo_stuff.buy_cheapest()
          
          >>> mo_stuff.items
          [apple, oreos]
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
