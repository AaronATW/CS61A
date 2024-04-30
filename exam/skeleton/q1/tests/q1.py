test = {
  'name': 'q1',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> put1 = kv()
          
          >>> get2, put2 = put1('cat', 'animal')
          
          >>> get3, put3 = put2('table', 'furniture')
          
          >>> get4, put4 = put3('cup', 'utensil')
          
          >>> get5, put5 = put4('thesis', 'paper')
          
          >>> get5('thesis')
          'paper'
          
          >>> get5('cup')
          'utensil'
          
          >>> get5('table')
          'furniture'
          
          >>> get5('cat')
          'animal'
          
          >>> get3('cup')
          0
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q1 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
