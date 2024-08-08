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
          10c721bc82fdd7c9ec09ace56a4babb2
          # locked
          >>> B.x = 2
          >>> print(A.x, B.x, C.x)
          ddd4223b9fcb9aacc0698921d5b93822
          # locked
          >>> A.x += 1
          >>> print(A.x, B.x, C.x)
          ace02b4030564dff850161ec584a2b14
          # locked
          >>> obj = C()
          >>> obj.y = 1
          >>> C.y == obj.y
          a559f517e8f86de30b928d7e29ec2331
          # locked
          >>> A.y = obj.y
          >>> print(A.y, B.y, C.y, obj.y)
          cd186634874ca6ee490ac84564df8a7f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
