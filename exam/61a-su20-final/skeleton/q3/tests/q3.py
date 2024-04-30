test = {
  'name': 'q3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t1 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])]), Tree(5)])
          
          >>> print(t1)
          1
              2
                  3
                      4
              5
          
          >>> same_length(t1, 2)
          
          >>> print(t1)
          1
              2
                  3
              5
                  hello
          
          >>> t2 = Tree(4, [Tree(5, [Tree(6), Tree(7)]), Tree(10), Tree(15, [Tree(16, [Tree(17, [Tree(18, [Tree(19)])])])])])
          
          >>> same_length(t2, 3)
          
          >>> print(t2)
          4
              5
                  6
                      hello
                  7
                      hello
              10
                  hello
                      hello
              15
                  16
                      17
          
          >>> t1 = Tree(1, [Tree(2, [Tree(3)]), Tree(5, [Tree("hello")])])
          
          >>> print(t1)
          1
              2
                  3
              5
                  hello
          
          >>> shortest_no_hello(t1)
          [1, 5]
          
          >>> t2 = Tree(4, [Tree(5, [Tree(6, [Tree("hello")]), Tree(7, [Tree("hello")])]), Tree(10, [Tree("hello", [Tree("hello")])]), Tree(15, [Tree(16, [Tree(17)])])])
          
          >>> print(t2)
          4
              5
                  6
                      hello
                  7
                      hello
              10
                  hello
                      hello
              15
                  16
                      17
          
          >>> shortest_no_hello(t2)
          [4, 10]
          
          >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
          
          >>> t.label
          3
          
          >>> t.branches[0].label
          2
          
          >>> t.branches[1].is_leaf()
          True
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
