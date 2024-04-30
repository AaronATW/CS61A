test = {
  'name': 'q2',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> storeroom(1234, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 > 3 * 1
          True
          
          >>> storeroom(11111111111112, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1 * 1 * ... * 1
          True
          
          >>> storeroom(11111111111112, lambda x,y: x+y, lambda x,y: x+y) # 2 <= 1 + 1 + ... + 1
          False
          
          >>> storeroom(12, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1
          True
          
          >>> storeroom(12345, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 <= 1 * 3 * 5
          False
          
          >>> storeroom(18383, lambda x,y: x-y, lambda x,y: x-y) # 8 - 8 > 3 - 3 - 1
          True
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q2 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
