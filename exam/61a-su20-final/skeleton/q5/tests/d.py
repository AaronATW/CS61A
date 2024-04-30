test = {
  'name': 'd',
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
          
          >>> [i for i in stuff.generate_list(1, ["vegetable"])]
          [kale]
          
          >>> [i for i in stuff.generate_list(1, ["fruit"])]
          []
          
          >>> [i for i in stuff.generate_list(10, ["vegetable", "fruit", "junk_food"])]
          [tomato, kale, apple]
          
          >>> [i for i in stuff.generate_list(50, ["vegetable", "fruit", "junk_food", "meat"])]
          [tomato, kale, apple, chicken, oreos]
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
