(define (over-or-under num1 num2) 
  (cond
  ((< num1 num2) -1)
  ((= num1 num2) 0)
  (else 1)
  )
)

(define (make-adder num) 
(lambda (inc) (+ num inc))
)

(define (composed f g) 
(lambda (x) (f (g x)))
)

(define (repeat f n) 
(if (< n 1)
    (lambda (x) x)
    (composed f (repeat f (- n 1)))
)
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
(cond
  ((zero? a) b) ;检查基础情况 a 为 0 则返回 b 作为 gcd，反之亦然
  ((zero? b) a)
  ; 如果 max(a, b) 能被 min(a, b) 整除，返回较小的数
  ((= (modulo (max a b) (min a b)) 0) (min a b))
  ;否则递归调用 gcd 函数
  (else (gcd (min a b) (modulo (max a b) (min a b))))
)
)
