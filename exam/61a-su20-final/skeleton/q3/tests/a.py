test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t3 = Tree(10, [Tree(20), Tree(30, [Tree(50)]), Tree(40, [Tree(70)])])
          
          >>> same_length(t3, 4)
          
          >>> print(t3)
          10
              20
                  hello
                      hello
                          hello
              30
                  50
                      hello
                          hello
              40
                  70
                      hello
                          hello
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q3 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
