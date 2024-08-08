test = {
  'name': 'Iterators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Enter StopIteration if StopIteration exception occurs, Error for other errors
          >>> # Enter Iterator if the output is an iterator object.
          >>> s = [1, 2, 3, 4]
          >>> t = iter(s)
          >>> next(s)
          Error
          >>> next(t)
          1
          >>> next(t)
          2
          >>> next(iter(s))
          1
          >>> next(iter(s))
          1
          >>> next(t)
          3
          >>> next(t)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> r = range(6)
          >>> r_iter = iter(r)
          >>> next(r_iter)
          0
          >>> [x + 1 for x in r]
          [1, 2, 3, 4, 5, 6]
          >>> [x + 1 for x in r_iter]
          [2, 3, 4, 5, 6]
          >>> next(r_iter)
          StopIteration
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> map_iter = map(lambda x : x + 10, range(5))
          >>> next(map_iter)
          10
          >>> next(map_iter)
          11
          >>> list(map_iter)
          [12, 13, 14]
          >>> for e in filter(lambda x : x % 4 == 0, range(1000, 1008)):
          ...     print(e)
          1000
          1004
          >>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
          [5, 7, 9]
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
