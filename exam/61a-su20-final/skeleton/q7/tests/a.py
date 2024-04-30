test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM parta;
          DVD f
          DVD c
          DVD d
          """,
          'hidden': False
        }
      ],
      'ordered': True,
      'scored': True,
      'setup': 'sqlite> .read q7.sql',
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
