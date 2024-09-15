test = {
  'name': 'Problem 7',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (lambda (x y) (+ x y)) ;; An lambda procedure is displayed exactly as it is written
          1456de84c3edf333b6f7aee0c0624b20
          # locked
          scm> (lambda (x)) ; type SchemeError if you think this causes an error
          ec908af60f03727428c7ee3f22ec3cd8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (lambda (x) (+ x) (+ x x))
          (lambda (x) (+ x) (+ x x))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (lambda () 2)
          (lambda () 2)
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
          >>> env = create_global_frame()
          >>> lambda_line = read_line("(lambda (a b c) (+ a b c))")
          >>> lambda_proc = do_lambda_form(lambda_line.rest, env)
          >>> lambda_proc.formals # use single quotes ' around strings in your answer
          d106bb7be6b014a9d16d74410be4a8a5
          # locked
          # choice: Pair('a', Pair('b', Pair('c', nil)))
          # choice: Pair('+', Pair('a', Pair('b', Pair('c', nil))))
          # choice: Pair(Pair('a', Pair('b', Pair('c', nil))))
          >>> lambda_proc.body # the body is a *Scheme list* of expressions! Make sure your answer is a properly nested Pair.
          0ef147cfe5caf670e985d95d923f4b06
          # locked
          # choice: Pair(Pair('+', Pair('a', Pair('b', Pair('c', nil)))), nil)
          # choice: Pair('+', Pair('a', Pair('b', Pair('c', nil))))
          # choice: Pair('+', 'a', 'b', 'c')
          # choice: Pair('a', Pair('b', Pair('c')))
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> lambda_line = read_line("(lambda (x y) x)")
          >>> lambda_proc = do_lambda_form(lambda_line.rest, env)
          >>> isinstance(lambda_proc, LambdaProcedure)
          True
          >>> lambda_proc.env is env
          True
          >>> lambda_proc
          LambdaProcedure(Pair('x', Pair('y', nil)), Pair('x', nil), <Global Frame>)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
