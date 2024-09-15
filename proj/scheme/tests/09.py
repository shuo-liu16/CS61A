test = {
  'name': 'Problem 9',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define square (lambda (x) (* x x)))
          square
          scm> square
          (lambda (x) (* x x))
          scm> (square 21)
          441
          scm> square ; check to make sure lambda body hasn't changed
          (lambda (x) (* x x))
          scm> (define square (lambda (x) (* x x)))
          square
          scm> (square (square 21))
          194481
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> ((lambda (x) (list x (list (quote quote) x))) (quote (lambda (x) (list x (list (quote quote) x))))) ; if you're failing this test case and have checked your implementation of Q9, you may want to check your Q5 solution
          ((lambda (x) (list x (list (quote quote) x))) (quote (lambda (x) (list x (list (quote quote) x)))))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define double (lambda (n) (* 2 n))) ; make double a LambdaProcedure that doubles a number
          double
          scm> (double 5)
          10
          scm> (define n 5)
          n
          scm> (double 7)
          14
          scm> (define add-n (lambda (x) (+ x n)))
          add-n
          scm> (add-n 6)
          11
          scm> (define x 10)
          x
          scm> (add-n 7)
          12
          scm> (define n 8)
          n
          scm> (add-n 7)
          15
          scm> x
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define do-twice (lambda (f x) (f (f x))))
          do-twice
          scm> (define double (lambda (x) (* 2 x)))
          double
          scm> (do-twice double 3)
          12
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define x 5)
          38ba916dc1f41eb239567ee41a251ecd
          # locked
          scm> (define outer (lambda (x)
          ....   (lambda () (print x))))
          71fe94b728b1cb1923a1c51c2533bcd8
          # locked
          scm> (define inner (outer 2))
          1e0787dce99b0bae31afaf95cb7dddff
          # locked
          scm> (inner) ;; which x is accessed? which frame is the parent?
          2b7cdec3904f986982cbd24a0bc12887
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define outer (lambda (x y)
          ....   (define inner (lambda (z x)
          ....     (+ x (* y 2) (* z 3))))
          ....   (inner x 10)))
          outer
          scm> (outer 1 2)
          17
          scm> (define outer-func (lambda (x y)
          ....   (define inner (lambda (z x)
          ....     (+ x (* y 2) (* z 3))))
          ....   inner))
          outer-func
          scm> ((outer-func 1 2) 1 10)
          17
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define square (lambda (x) (* x x)))
          square
          scm> (define sum-of-squares (lambda (x y) (+ (square x) (square y))))
          sum-of-squares
          scm> (sum-of-squares 3 4)
          25
          scm> (define double (lambda (x) (* 2 x)))
          double
          scm> (define compose (lambda (f g) (lambda (x) (f (g x)))))
          compose
          scm> (define apply-twice (lambda (f) (compose f f)))
          apply-twice
          scm> ((apply-twice double) 5)
          20
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
