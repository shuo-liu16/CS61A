test = {
  'name': 'my-filter',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (my-filter even? '(1 2 3 4))
          (2 4)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter odd? '(1 3 5))
          (1 3 5)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter odd? '(2 4 6 1))
          (1)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter even? '(3))
          ()
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter odd? nil)
          ()
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
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (my-filter even? '(1 2 3 4)) ; checks you dont use builtin filter
          (2 4)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (define filter nil)
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
