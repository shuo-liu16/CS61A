test = {
  'name': 'switch-to-cond',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (switch-to-cond `(switch (+ 1 1) ((1 2)
          ....                                   (2 4)
          ....                                   (3 6))))
          (cond ((equal? (+ 1 1) 1) 2) ((equal? (+ 1 1) 2) 4) ((equal? (+ 1 1) 3) 6))
          scm> (switch 1 ((1 (print 'a))
          ....            (2 (print 'b))
          ....            (3 (print 'c))))
          a
          scm> (switch (+ 1 1) ((1 (print 'a))
          ....                  (2 (print 'b))
          ....                  (3 (print 'c))))
          b
          scm> (define x 'b)
          x
          scm> (switch x (('a (print 1))
          ....            ('b (print 2))
          ....            ('c (print 3))))
          2
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
