(define email "example_key")

;; This question is in two parts, implementing `cabinet-filter` and
;; `remove-comments`. See the specifications above each definition
;; for details.

;; You need to do part (a) to run the tests for part (b).

;; NOTE: In all scheme/sql questions you can put a multi-line answer
;;    in a blank


;; Part (a)
;; A cabinet-filter is similar to a normal `filter` operation, except that
;; it involves deeply filtering the given list by removing all elements
;; that *do* match the predicate.
;;
;; NOTE 1: If the entire input matches the predicate, you should not delete it
;; NOTE 2: You can assume that `pred` can be called on an element of any type
;;
;; To run tests just for this part, run
;;      python3 ok -q a
;;
;; scm> (cabinet-filter '(1 (2) (2 3)) (lambda (x) (and (number? x) (even? x))))
;; (1 () (3))
;; scm> (cabinet-filter '(1 (2) (2 3) 4 5 6) list?)
;; (1 4 5 6)
;; scm> (cabinet-filter '(1 2 3 4) list?)
;; (1 2 3 4)
;; scm> (cabinet-filter '(i accidentally broke my computer) (lambda (x) (equal? x 'broke)))
;; (i accidentally my computer)
;; scm> (cabinet-filter '(a (a) ((a)) (((a)))) (lambda (x) (equal? x 'a)))
;; (() (()) ((())))

(define (cabinet-filter lst pred)
    (cond
        ((or (not (list? lst)) (null? lst))
            lst)
        ((pred (car lst))
            (cabinet-filter (cdr lst) pred))
        (else
            (cons
                (cabinet-filter (car lst) pred)
                (cabinet-filter (cdr lst) pred)))))

;; Part (b)
;; Now implement the macro `remove-comments`, that takes in a piece of code
;; and evaluates it, ignoring the 'comments' within it.
;;
;; Comments are tagged lists that begin with the tag `comment-starts-here`
;;
;; scm> (remove-comments ((comment-starts-here hi) + 2 3))
;; 5
;; scm> (remove-comments '(this is (comment-starts-here even-when-quoted) a list))
;; (this is a list)
;; scm> (remove-comments '((this is not a comment comment-starts-here)))
;; ((this is not a comment comment-starts-here))

(define-macro (remove-comments code)
    (define (helper x)
        (and (list? x) (eq? 'comment-starts-here (car x))))
    (cabinet-filter code helper))

; ORIGINAL SKELETON FOLLOWS

; ;; This question is in two parts, implementing `cabinet-filter` and
; ;; `remove-comments`. See the specifications above each definition
; ;; for details.

; ;; You need to do part (a) to run the tests for part (b).

; ;; NOTE: In all scheme/sql questions you can put a multi-line answer
; ;;    in a blank


; ;; Part (a)
; ;; A cabinet-filter is similar to a normal `filter` operation, except that
; ;; it involves deeply filtering the given list by removing all elements
; ;; that *do* match the predicate.
; ;;
; ;; NOTE 1: If the entire input matches the predicate, you should not delete it
; ;; NOTE 2: You can assume that `pred` can be called on an element of any type
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q a
; ;;
; ;; scm> (cabinet-filter '(1 (2) (2 3)) (lambda (x) (and (number? x) (even? x))))
; ;; (1 () (3))
; ;; scm> (cabinet-filter '(1 (2) (2 3) 4 5 6) list?)
; ;; (1 4 5 6)
; ;; scm> (cabinet-filter '(1 2 3 4) list?)
; ;; (1 2 3 4)
; ;; scm> (cabinet-filter '(i accidentally broke my computer) (lambda (x) (equal? x 'broke)))
; ;; (i accidentally my computer)
; ;; scm> (cabinet-filter '(a (a) ((a)) (((a)))) (lambda (x) (equal? x 'a)))
; ;; (() (()) ((())))

; (define (cabinet-filter lst pred)
;     (cond
;         ((or (not (list? lst)) (null? lst))
;             ______)
;         ((pred ______)
;             (cabinet-filter ______ ______))
;         (else
;             (cons
;                 ______
;                 ______))))

; ;; Part (b)
; ;; Now implement the macro `remove-comments`, that takes in a piece of code
; ;; and evaluates it, ignoring the 'comments' within it.
; ;;
; ;; Comments are tagged lists that begin with the tag `comment-starts-here`
; ;;
; ;; scm> (remove-comments ((comment-starts-here hi) + 2 3))
; ;; 5
; ;; scm> (remove-comments '(this is (comment-starts-here even-when-quoted) a list))
; ;; (this is a list)
; ;; scm> (remove-comments '((this is not a comment comment-starts-here)))
; ;; ((this is not a comment comment-starts-here))

; (define-macro (remove-comments code)
;     (define (helper x)
;         ______)
;     (cabinet-filter ______ ______))
