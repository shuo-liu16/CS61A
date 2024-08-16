test = {
  'name': 'ascending?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (ascending? '(1 2 3 4 5))  ; #t or #f
          #t
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(1 5 2 4 3))  ; #t or #f
          #f
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(2 2))  ; #t or #f
          #t
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(1 2 2 4 3))  ; #t or #f
          #f
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '())  ; #t or #f
          #t
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
