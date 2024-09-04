test = {
  'name': 'repeat-lambda',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (repeat (+ 2 3) (print 1))
          1
          1
          1
          1
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (repeat 2 (repeat 2 (print 'four)))
          four
          four
          four
          four
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
