(define (split-at lst n)
  (cond
	((= n 0) (cons () lst))
	((null? (cdr (split-at lst (- n 1)))) (cons lst ()))
	(else
		(define dp-split (split-at lst (- n 1)))
		(cons (append (car dp-split) (list (car (cdr dp-split)))) (cdr (cdr dp-split))))
  )
)


(define-macro (switch expr cases)
	(cons 'cond
		(map (lambda (case) (cons (eq? (eval expr) (car case)) (cdr case)))
    			cases))
)

