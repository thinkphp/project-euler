(defun solution (&optional (n 1000))
  (loop for x from 0 below n
        when (or (= 0 (mod x 3)) (= 0 (mod x 5)))
        sum x))

(solution)
