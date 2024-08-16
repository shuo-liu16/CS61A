test = {
  'name': 'gcd',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (gcd 24 60)
          12
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (gcd 1071 462)
          21
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
