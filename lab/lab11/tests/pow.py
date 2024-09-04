test = {
  'name': 'pow',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (pow-expr 2 0)
          1
          scm> (pow-expr 2 1)
          (* 2 1)
          scm> (pow-expr 2 5)
          (* 2 (square (square (* 2 1))))
          scm> (pow-expr 2 15)
          (* 2 (square (* 2 (square (* 2 (square (* 2 1)))))))
          scm> (pow-expr 2 16)
          (square (square (square (square (* 2 1)))))
          scm> (eval (pow-expr 2 16))
          65536
          scm> (pow-expr 3 9)
          (* 3 (square (square (square (* 3 1)))))
          scm> (eval (pow-expr 3 9))
          19683
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
