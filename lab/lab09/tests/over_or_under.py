test = {
  'name': 'over-or-under',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (over-or-under 5 5)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (over-or-under 5 4)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (over-or-under 3 5)
          -1
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
