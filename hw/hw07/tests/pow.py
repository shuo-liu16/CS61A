test = {
  'name': 'pow',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (pow 2 5)
          32
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (pow 10 3)
          1000
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (pow 3 3)
          27
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (pow 1 100000000000000) ; make sure this doesn't run forever!
          1
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
