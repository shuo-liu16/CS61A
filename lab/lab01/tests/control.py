test = {
  'name': 'Control',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def xk(c, d):
          ...     if c == 4:
          ...         return 6
          ...     elif d >= 4:
          ...         return 6 + 7 + c
          ...     else:
          ...         return 25
          >>> xk(10, 10)
          23
          >>> xk(10, 6)
          23
          >>> xk(4, 6)
          6
          >>> xk(0, 0)
          25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> def how_big(x):
          ...     if x > 10:
          ...         print('huge')
          ...     elif x > 5:
          ...         return 'big'
          ...     if x > 0:
          ...         print('positive')
          ...     else:
          ...         print(0)
          >>> how_big(7)  # Be careful with quotation marks!
          'big'
          >>> print(how_big(7))  # Be careful with quotation marks!
          big
          >>> how_big(12)
          huge
          positive
          >>> print(how_big(12))
          huge
          positive
          None
          >>> print(how_big(1), how_big(0))
          positive
          0
          None None
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
          >>> n = 3
          >>> while n >= 0:  # If this loops forever, just type Infinite Loop
          ...     n -= 1
          ...     print(n)
          2
          1
          0
          -1
          """,
          'hidden': False,
          'locked': False,
          'multiline': True
        },
        {
          'code': r"""
          >>> negative = -12
          >>> while negative: # If this loops forever, just type Infinite Loop
          ...    if negative + 6:
          ...        print(negative)
          ...    negative += 3
          -12
          -9
          -3
          """,
          'hidden': False,
          'locked': False,
          'multiline': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
