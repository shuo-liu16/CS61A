test = {
  'name': 'pairs',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM pairs;
          RSF and Wheeler together have 1600 seats
          Pimentel and RSF together have 1400 seats
          Li Ka Shing and RSF together have 1200 seats
          Pimentel and Wheeler together have 1200 seats
          RSF and Stanley together have 1200 seats
          Li Ka Shing and Wheeler together have 1000 seats
          Morgan and RSF together have 1000 seats
          Stanley and Wheeler together have 1000 seats
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
