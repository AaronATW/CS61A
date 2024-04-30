test = {
  'name': 'q6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> compress([1,1,1], [3])
          True
          
          >>> compress([1,1,1], [2])
          False
          
          >>> compress([1,1,1], [1])
          True
          
          >>> compress([1,2,3], [1,5])
          True
          
          >>> compress([1,2,3], [2])
          True
          
          >>> compress([], [1,2,3])
          False
          
          >>> compress([1,2,3], [])
          False
          
          >>> compress([], [])
          True
          
          >>> compress([1,4,2,8,3,9,4], [31])
          True
          
          >>> compress([1,4,2,8,3,9,4], [3,5,5])
          True
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q6 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> compress([1, 2, 3, 4, 5, 9], [0])
          True
          
          >>> compress([5], [0])
          False
          
          >>> compress([0], [0])
          True
          
          >>> compress([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
          True
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q6 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> compress([2, 3, 4, 3, 4, 7], [1])
          True
          
          >>> compress([5, 6, 7, 8], [0, 2, 3])
          False
          
          >>> compress([5], [5])
          True
          
          >>> compress([2, 3], [2, 3])
          True
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q6 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
