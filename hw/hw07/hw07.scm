(define (square n) (* n n))

(define (pow base exp) 
  (cond 
    ((= exp 0) 1)
    ((= exp 1) base)
    ((even? exp) (square (pow base (/ exp 2)))) ;减少时间复杂度，避免超时
    (else (* base (pow base (- exp 1)))))
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))
