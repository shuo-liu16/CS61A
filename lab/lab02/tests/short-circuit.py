test = {
  'name': 'The Truth Will Prevail',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> True and 13
          13
          >>> False or 0
          0
          >>> not 10
          False
          >>> not None
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> True and 1 / 0  # If this errors, just type Error.
          Error
          >>> True or 1 / 0  # If this errors, just type Error.
          True
          >>> -1 and 1 > 0 # If this errors, just type Error.
          True
          >>> -1 or 5
          -1
          >>> (1 + 1) and 1  # If this errors, just type Error. If this is blank, just type Nothing.
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> print(3) or ""
          3
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def f(x):
          ...     if x == 0:
          ...         return "zero"
          ...     elif x > 0:
          ...         return "positive"
          ...     else:
          ...         return ""
          >>> 0 or f(1)
          'positive'
          >>> f(0) or f(-1)
          'zero'
          >>> f(0) and f(-1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
