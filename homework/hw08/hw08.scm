(define (rle s)
  (cond 
    ((null? s) ())
    ((null? (cdr-stream s)) (cons-stream `(,(car s) 1) nil))
    ((not (eq? (car s) (car (car (rle (cdr-stream s)))))) (cons-stream `(,(car s) 1) (rle (cdr-stream s))))
    (else (cons-stream `(,(car s) ,(+ 1 (car (cdr (car (rle (cdr-stream s))))))) (cdr-stream (rle (cdr-stream s)))))
  )
)



(define (group-by-nondecreasing s)
  (cond
    ((null? s) ())
    ((null? (cdr-stream s)) (cons-stream `(,(car s)) nil))
    ((> (car s) (car (cdr-stream s))) (cons-stream `(,(car s)) (group-by-nondecreasing (cdr-stream s))))
    (else (cons-stream (cons (car s) (car (group-by-nondecreasing (cdr-stream s)))) (cdr-stream (group-by-nondecreasing (cdr-stream s)))))
  )
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

