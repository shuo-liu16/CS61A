(define (ascending? s) 
    (cond 
        ((or (null? s) (null? (cdr s)))  #t)
        ((> (car s) (car (cdr s)))  #f)
        (else (ascending? (cdr s)))
    )
)

(define (my-filter pred s) 
    (cond
        ((null? s)  '())
        ((pred (car s))   
            (cons (car s) (my-filter pred (cdr s))))  
        (else   
            (my-filter pred (cdr s)))
    )
)

(define (interleave lst1 lst2) 
    (cond
        ((and (null? lst1) (null? lst2)) '())
        ((null? lst1) 
            (cons (car lst2) (interleave lst1 (cdr lst2))))
        ((null? lst2) 
            (cons (car lst1) (interleave (cdr lst1) lst2)))
        (else
            (cons (car lst1) (interleave lst2 (cdr lst1))))
    )
)

(define (no-repeats s) 
    (cond 
        ((null? s) '())
        (else
            (cons (car s) (no-repeats (filter (lambda (x) (not(= (car s) x))) (cdr s))))
        )
    )

)
