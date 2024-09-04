test = {
  'name': 'curry-cook',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (curry-cook '(a) 'a)
          (lambda (a) a)
          scm> (curry-cook '(x y) '(+ x y))
          (lambda (x) (lambda (y) (+ x y)))
          scm> (define adder (curry-cook '(x y) '(+ x y)))
          adder
          scm> (eval adder)
          (lambda (x) (lambda (y) (+ x y)))
          scm> (((eval adder) 2) 3)
          5
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
