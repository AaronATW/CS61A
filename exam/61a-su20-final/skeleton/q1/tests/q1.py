test = {
  'name': 'q1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cabinet-filter '(1 (2) (2 3)) (lambda (x) (and (number? x) (even? x))))
          (1 () (3))
          
          scm> (cabinet-filter '(1 (2) (2 3) 4 5 6) list?)
          (1 4 5 6)
          
          scm> (cabinet-filter '(1 2 3 4) list?)
          (1 2 3 4)
          
          scm> (cabinet-filter '(i accidentally broke my computer) (lambda (x) (equal? x 'broke)))
          (i accidentally my computer)
          
          scm> (cabinet-filter '(a (a) ((a)) (((a)))) (lambda (x) (equal? x 'a)))
          (() (()) ((())))
          
          scm> (remove-comments ((comment-starts-here hi) + 2 3))
          5
          
          scm> (remove-comments '(this is (comment-starts-here even-when-quoted) a list))
          (this is a list)
          
          scm> (remove-comments '((this is not a comment comment-starts-here)))
          ((this is not a comment comment-starts-here))
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'scm> (load-all ".")',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (remove-comments (if #f 1 (comment-starts-here this is a comment) 2))
          2
          
          scm> (remove-comments '((comment-starts-here this is a comment)))
          ()
          
          scm> (remove-comments '((this is not a comment comment-starts-here)))
          ((this is not a comment comment-starts-here))
          
          scm> (remove-comments (comment-starts-here cannot delete the entire thing so this is an error))
          SchemeError
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'scm> (load-all ".")',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
