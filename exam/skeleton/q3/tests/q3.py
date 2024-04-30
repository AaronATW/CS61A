test = {
  'name': 'q3',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> maxkd(1234, 1)
          4
          
          >>> maxkd(32749, 2)
          79
          
          >>> maxkd(1917, 2)
          97
          
          >>> maxkd(32749, 18)
          32749
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q3 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
