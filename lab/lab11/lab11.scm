(define (if-program condition if-true if-false)
  `(if ,condition ,if-true ,if-false)
)

(define (square n) (* n n))

(define (pow-expr base exp) 
  (cond 
    ((= exp 0) 1)
    ((= base 0) 0)
    ((odd? exp) `(* ,base  ,(pow-expr base (- exp 1))))
    ((even? exp) `(square ,(pow-expr base (/ exp 2))))
    (else '(* base exp))
  )
)

(define-macro (repeat n expr)
  `(repeated-call ,n (lambda () ,expr))
)
; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1)
      (f)
      (begin 
        (f) 
        (repeated-call (- n 1) f)
      )
  )
)
