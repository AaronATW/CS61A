test = {
  'name': 'b',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t3 = Tree(10, [Tree(20, [Tree("hello", [Tree("hello", [Tree("hello")])])]), Tree(30, [Tree(50, [Tree("hello", [Tree("hello")])])]), Tree(40, [Tree(70, [Tree("hello", [Tree("hello")])])])])
          
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
          
          >>> shortest_no_hello(t3)
          [10, 20]
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
