test = {
  'name': 'What Would Scheme Display?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (- 10 4)
          aae76aca9259a704209b44193fad5f6a
          # locked
          scm> (* 7 6)
          127a9b44ce2a083fdab8c098b2f3ea29
          # locked
          scm> (+ 1 2 3 4)
          6ed2911f88b2fb526846619209f10214
          # locked
          scm> (/ 8 2 2)
          32cd207d18df99546ca7a56bc36ed715
          # locked
          scm> (quotient 29 5)
          8d3d95b1350833ea7b81c9454d1af611
          # locked
          scm> (modulo 29 5)
          a1e11865670a42d05e20b9a3455dc457
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (= 1 3)                    ; Scheme uses '=' instead of '==' for comparison
          2e53237de2e8eedffd8b1b7f96c2a14a
          # locked
          scm> (< 1 3)
          1a7ba87ca42a7e60de7365380a43df24
          # locked
          scm> (or 1 #t)                  ; or special form short circuits
          7cd20da6435c318b417f99ab831ac85e
          # locked
          scm> (and #t #f (/ 1 0))
          2e53237de2e8eedffd8b1b7f96c2a14a
          # locked
          scm> (not #t)
          2e53237de2e8eedffd8b1b7f96c2a14a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define x 3)
          71bd4043aeb5651e40436f3a0545f0c0
          # locked
          scm> x
          7cce957d5689f75737e35919f54283e1
          # locked
          scm> (define y (+ x 4))
          d64f11d53640e18d8feb73613f094889
          # locked
          scm> y
          54038328fa76561333de39372fc08510
          # locked
          scm> (define x (lambda (y) (* y 2)))
          71bd4043aeb5651e40436f3a0545f0c0
          # locked
          scm> (x y)
          455809c20da34dabebe151ebd26d6e5c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (if (not (print 1)) (print 2) (print 3))
          7cd20da6435c318b417f99ab831ac85e
          7cce957d5689f75737e35919f54283e1
          # locked
          scm> (* (if (> 3 2) 1 2) (+ 4 5))
          24501e5e22e5149e7702cb00bdfc079c
          # locked
          scm> (define foo (lambda (x y z) (if x y z)))
          3e851fde76db9adca3992a718e67604f
          # locked
          scm> (foo 1 2 (print 'hi))
          f680f73ca4860683e81a0df41e8f5106
          32cd207d18df99546ca7a56bc36ed715
          # locked
          scm> ((lambda (a) (print 'a)) 100)
          bd3f05fa4cb9864ae23adf7936df4482
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
