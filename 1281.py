def  sumofpro(n): 
    sum_ = 0
    while n > 0:
            #  extarcting last digit
            i = n % 10  
            sum_ += i
            pro *= i

            n = n // 10
    return pro-sum_

print(sumofpro(35))
