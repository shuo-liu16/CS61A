test = {
  'name': 'repeat',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define (square x) (* x x))
          square
          scm> ((repeat square 2) 5) ; (square (square 5))
          625
          scm> ((repeat square 3) 3) ; (square (square (square 3)))
          6561
          scm> ((repeat square 1) 7) ; (square 7)
          49
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (increment x) (+ x 1))
          increment
          scm> ((repeat increment 4) 2) ; (increment (increment (increment (increment 2))))
          6
          scm> ((repeat increment 10) 51)
          61
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
