test = {
  'name': 'curry-consume',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define three-curry (curry-cook '(x y z) '(+ x (* y z))))
          three-curry
          scm> three-curry
          (lambda (x) (lambda (y) (lambda (z) (+ x (* y z)))))
          scm> (define three-curry-fn (eval three-curry)) ; three-curry-fn is a lambda function derived from the program
          three-curry-fn
          scm> (define eat-two (curry-consume three-curry-fn '(1 2))) ; pass in only two arguments, return should be a one-arg lambda function!
          eat-two
          scm> eat-two
          (lambda (z) (+ x (* y z)))
          scm> (eat-two 3) ; pass in the last argument; 1 + (2 * 3)
          7
          scm> (curry-consume three-curry-fn '(1 2 3)) ; all three arguments at once!
          7
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
