(define (square n) (* n n))

(define (pow base exp) 
(cond ((= exp 0) 1); 如果指数是 0，返回 1（任何数的 0 次幂都是 1）
      ((even? exp) (square (pow base (/ exp 2)))); 如果 exp 是偶数，先计算 base^(exp/2)，然后对结果平方
      (else (* base (pow base (- exp 1)))); 如果是奇数，递归计算 base^(exp-1)，平方后再乘以 base
)
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let 
        ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))


(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr(cdr s))))
