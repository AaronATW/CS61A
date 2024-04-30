test = {
  'name': 'b',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM partb;
          ***|2
          *****|3
          """,
          'hidden': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': 'sqlite> .read q7.sql',
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
