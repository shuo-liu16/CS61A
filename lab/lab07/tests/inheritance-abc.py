test = {
  'name': 'Inheritance ABCs',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class A:
          ...   x, y = 0, 0
          ...   def __init__(self):
          ...         return
          >>> class B(A):
          ...   def __init__(self):
          ...         return
          >>> class C(A):
          ...   def __init__(self):
          ...         return
          >>> print(A.x, B.x, C.x)
          0 0 0
          >>> B.x = 2
          >>> print(A.x, B.x, C.x)
          0 2 0
          >>> A.x += 1
          >>> print(A.x, B.x, C.x)
          1 2 1
          >>> obj = C()
          >>> obj.y = 1
          >>> C.y == obj.y
          False
          >>> A.y = obj.y
          >>> print(A.y, B.y, C.y, obj.y)
          1 1 1 1
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
