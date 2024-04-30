test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cabinet-filter '(1 2 3) (lambda (x) (= x 2)))
          (1 3)
          
          scm> (cabinet-filter '(1 2 3) (lambda (x) (list? x)))
          (1 2 3)
          
          scm> (cabinet-filter '(1 (2 3)) (lambda (x) (list? x)))
          (1)
          
          scm> (cabinet-filter '((1) (2 3)) (lambda (x) (list? x)))
          ()
          
          scm> (cabinet-filter '((1) (2 3)) (lambda (x) (and (list? x) (equal? (car x) 2))))
          ((1))
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
