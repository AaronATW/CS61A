(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond
    ((< num 0) -1)
    ((= num 0) 0)
    (else 1)
  )
)


(define (square x) (* x x))

(define (pow x y)
  (cond
    ((= y 1) x)
    ((even? y) (square (pow x (/ y 2))))
    (else (* x (square (pow x (/ (- y 1) 2)))))
  )
)


(define (unique s)
  (if (null? s)
    nil
    (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s))))
  )
)


(define (replicate x n)
  (define (replicate_helper x n result)
    (if (= n 0)
      result
      (replicate_helper x (- n 1) (cons x result))
    )
  )
  (replicate_helper x n ())
)


(define (accumulate combiner start n term)
  (define (accumulate_helper combiner start n term current_n)
    (if (> current_n n)
      start
      (accumulate_helper combiner (combiner start (term current_n)) n term (+ 1 current_n))
    )
  )
  (accumulate_helper combiner start n term 1)
)


(define (accumulate-tail combiner start n term)
  (define (accumulate_helper combiner start n term current_n)
    (if (> current_n n)
      start
      (accumulate_helper combiner (combiner start (term current_n)) n term (+ 1 current_n))
    )
  )
  (accumulate_helper combiner start n term 1)
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  (list 'map (list 'lambda (list var) map-expr) (list 'filter (list 'lambda (list var) filter-expr) lst))
)