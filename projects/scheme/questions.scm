(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
    (if (null? rests)
        ()
        (cons (cons first (car rests)) (cons-all first (cdr rests)))
    )
)

(define (zip pairs)
  (if (null? pairs)
    '(() ())
    `(,(cons (caar pairs) (car (zip (cdr pairs)))) ,(cons (cadr (car pairs)) (cadr (zip (cdr pairs)))))
  )
)

;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
  (define (enumerate_helper index s) (if (null? s) () (cons `(,index ,(car s)) (enumerate_helper (+ 1 index) (cdr s)))))
  (enumerate_helper 0 s)
  )
  ; END PROBLEM 16

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 17
  (cond
      ((null? denoms) '(()))
      ((= total 0) '(()))
      ((< total (car denoms)) (list-change total (cdr denoms)))
      (else
        (define base-list (cons-all (car denoms) (list-change (- total (car denoms)) denoms)))
        (define temp-list (list-change total (cdr denoms)))
        (if (null? (car temp-list))
            base-list
            (append base-list temp-list)
        ))))
  ; END PROBLEM 17

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (append `(,form ,params) (map let-to-lambda body))
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (append `(,`(lambda ,(map car values) ,(let-to-lambda (car body)))) (map let-to-lambda (map cadr values)))
           ; END PROBLEM 18
           ))
        (else
         ; BEGIN PROBLEM 18
         (map let-to-lambda expr)
         ; END PROBLEM 18
         )))