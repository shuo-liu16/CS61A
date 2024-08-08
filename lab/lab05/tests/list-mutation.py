test = {
  'name': 'List Mutation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If nothing would be output by Python, type Nothing
          >>> # If the code would error, type Error
          >>> s = [6, 7, 8]
          >>> print(s.append(6))
          None
          >>> s
          [6, 7, 8, 6]
          >>> s.insert(0, 9)
          >>> s
          [9, 6, 7, 8, 6]
          >>> x = s.pop(1)
          >>> s
          [9, 7, 8, 6]
          >>> s.remove(x)
          >>> s
          [9, 7, 8]
          >>> a, b = s, s[:]
          >>> a is s
          True
          >>> b == s
          True
          >>> b is s
          False
          >>> a.pop()
          8
          >>> a + b
          [9, 7, 9, 7, 8]
          >>> s = [3]
          >>> s.extend([4, 5])
          >>> s
          [3, 4, 5]
          >>> a
          [9, 7]
          >>> s.extend([s.append(9), s.append(10)])
          >>> s
          [3, 4, 5, 9, 10, None, None]
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
