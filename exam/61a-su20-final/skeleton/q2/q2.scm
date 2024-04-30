(define email "example_key")

;; This question is in two parts, implementing `ladder-locator` and
;; `studio-switch`. See the specifications above each definition
;; for details.
;;
;; NOTE: these parts are unrelated to each other, you can work on
;;    them in any order.

;; Part (a)
;; Implement `ladder-locator` which takes in a number `newspaper` and circles
;; all digits of value `8` in the number by returning a list of digits where all the
;; `8` digits are individually placed in a nested list.
;;
;; NOTE 1: Your function should be tail recursive
;; NOTE 2: You can use the `//` procedure defined below to perform floordiv
;; NOTE 3: You can use the builtin `modulo` procedure to perform modulo
;; NOTE 4: In all scheme/sql questions you can put a multi-line answer
;;    in a blank
;;
;; To run tests just for this part, run
;;      python3 ok -q a

(define (// numer denom) (floor (/ numer denom)))

;; scm> (ladder-locator 12)
;; (1 2)
;; scm> (ladder-locator 1881)
;; (1 (8) (8) 1)
;; scm> (ladder-locator 0) ; no digits
;; ()
;; scm> (ladder-locator 88888888)
;; ((8) (8) (8) (8) (8) (8) (8) (8))
;; scm> (ladder-locator 1128651)
;; (1 1 2 (8) 6 5 1)

(define (ladder-locator newspaper)
    (define (helper newspaper ladder)
        (define current-digit
            (modulo newspaper 10))
        (define value
            (if
                (= current-digit 8)
                '(8)
                current-digit))
        (if (= newspaper 0)
            ladder
            (helper
                (// newspaper 10)
                (cons value ladder))))
    (helper newspaper ()))

;; Part (b)
;; The `studio-switch` operation takes in two infinite streams `xv` and `yq`
;; and returns a new stream containing the non-guitar elements of each stream,
;; alternating from one stream to the other when encountering the symbol
;; `guitar`.
;;
;; Note: the symbol `guitar` should not appear in the final stream.
;;
;;
;; To run tests just for this part, run
;;      python3 ok -q b

;; the following function is defined for testing, and takes the first
;; k elements of a stream `s`, returning them as a list.
(define (take k s)
    (if (zero? k)
        nil
        (cons
            (car s)
            (take (- k 1) (cdr-stream s)))))

;; scm> (define just-guitar (cons-stream 'guitar just-guitar))
;; just-guitar
;; scm> (define two (cons-stream 1 (cons-stream 'guitar two)))
;; two
;; scm> (define three (cons-stream 'x (cons-stream 'y (cons-stream 'guitar three))))
;; three
;; scm> (take 10 two)
;; (1 guitar 1 guitar 1 guitar 1 guitar 1 guitar)
;; scm> (take 10 three)
;; (x y guitar x y guitar x y guitar x)
;; scm> (take 10 (studio-switch two three))
;; (1 x y 1 x y 1 x y 1)
;; scm> (take 10 (studio-switch two just-guitar))
;; (1 1 1 1 1 1 1 1 1 1)
;; scm> (take 10 (studio-switch three three))
;; (x y x y x y x y x y)

(define (studio-switch xv yq)
	(if (eq? (car xv) 'guitar)
		(studio-switch yq (cdr-stream xv))
		(cons-stream (car xv) (studio-switch (cdr-stream xv) yq))))


; ORIGINAL SKELETON FOLLOWS

; ;; This question is in two parts, implementing `ladder-locator` and
; ;; `studio-switch`. See the specifications above each definition
; ;; for details.
; ;;
; ;; NOTE: these parts are unrelated to each other, you can work on
; ;;    them in any order.

; ;; Part (a)
; ;; Implement `ladder-locator` which takes in a number `newspaper` and circles
; ;; all digits of value `8` in the number by returning a list of digits where all the
; ;; `8` digits are individually placed in a nested list.
; ;;
; ;; NOTE 1: Your function should be tail recursive
; ;; NOTE 2: You can use the `//` procedure defined below to perform floordiv
; ;; NOTE 3: You can use the builtin `modulo` procedure to perform modulo
; ;; NOTE 4: In all scheme/sql questions you can put a multi-line answer
; ;;    in a blank
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q a

; (define (// numer denom) (floor (/ numer denom)))

; ;; scm> (ladder-locator 12)
; ;; (1 2)
; ;; scm> (ladder-locator 1881)
; ;; (1 (8) (8) 1)
; ;; scm> (ladder-locator 0) ; no digits
; ;; ()
; ;; scm> (ladder-locator 88888888)
; ;; ((8) (8) (8) (8) (8) (8) (8) (8))
; ;; scm> (ladder-locator 1128651)
; ;; (1 1 2 (8) 6 5 1)

; (define (ladder-locator newspaper)
;     (define (helper newspaper ______)
;         (define current-digit
;             ______)
;         (define value
;             (if
;                 ______
;                 ______
;                 ______))
;         (if ______
;             ______
;             (helper
;                 ______
;                 (cons value ______))))
;     (helper ______ ______))

; ;; Part (b)
; ;; The `studio-switch` operation takes in two infinite streams `xv` and `yq`
; ;; and returns a new stream containing the non-guitar elements of each stream,
; ;; alternating from one stream to the other when encountering the symbol
; ;; `guitar`.
; ;;
; ;; Note: the symbol `guitar` should not appear in the final stream.
; ;;
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q b

; ;; the following function is defined for testing, and takes the first
; ;; k elements of a stream `s`, returning them as a list.
; (define (take k s)
;     (if (zero? k)
;         nil
;         (cons
;             (car s)
;             (take (- k 1) (cdr-stream s)))))

; ;; scm> (define just-guitar (cons-stream 'guitar just-guitar))
; ;; just-guitar
; ;; scm> (define two (cons-stream 1 (cons-stream 'guitar two)))
; ;; two
; ;; scm> (define three (cons-stream 'x (cons-stream 'y (cons-stream 'guitar three))))
; ;; three
; ;; scm> (take 10 two)
; ;; (1 guitar 1 guitar 1 guitar 1 guitar 1 guitar)
; ;; scm> (take 10 three)
; ;; (x y guitar x y guitar x y guitar x)
; ;; scm> (take 10 (studio-switch two three))
; ;; (1 x y 1 x y 1 x y 1)
; ;; scm> (take 10 (studio-switch two just-guitar))
; ;; (1 1 1 1 1 1 1 1 1 1)
; ;; scm> (take 10 (studio-switch three three))
; ;; (x y x y x y x y x y)

; (define (studio-switch xv yq)
; 	(if ______
; 		______
; 		(cons-stream ______ ______)))

