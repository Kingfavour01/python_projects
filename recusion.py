

def walk(step):
    if step == 0:
        return
    walk(step - 1)
    print(f" you  have taken your ----{step}")

# finding factorial iteratively and recursively
#
def fac(n):
   if n == 1:
       return 1
   else:
       return n * fac(n -1)



#iteratively
def factorial(x):
    result = 1
    if x > 0:
        for y in range(1, x + 1):
            result *= y
        return result



print(fac(5))
print(factorial(5))