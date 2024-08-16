test = {
  'name': 'interleave',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (interleave (list 1 3 5) (list 2 4))
          (1 2 3 4 5)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave (list 2 4) (list 1 3 5))
          (2 1 4 3 5)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave (list 1 2) (list 1 2))
          (1 1 2 2)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave '(1 2 3 4 5 6) '(7 8))
          (1 7 2 8 3 4 5 6)
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
          scm> (interleave (list 1 3 5) (list 2 4 6))
          (1 2 3 4 5 6)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave (list 1 3 5) nil)
          (1 3 5)
          scm> (interleave nil (list 1 3 5))
          (1 3 5)
          scm> (interleave nil nil)
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
    }
  ]
}
