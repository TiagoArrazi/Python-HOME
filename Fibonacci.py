def main():
    n = int(input("Insira um número > 1 "))
    print('Fibonacci Recursivo - ' + str(FibonacciRec(n)))
    print('Fibonacci Iterativo - ' + str(Fibonacci(n)))

def Fibonacci(n):

    if n <= 1: return n

    fib = 1
    fibPrev = 1

    for i in range(2,n):
        
        temp = fib
        fib += fibPrev
        fibPrev = temp


    return fib

def FibonacciRec(n):

    if n <= 1: return n

    else: return FibonacciRec(n - 1) + FibonacciRec(n - 2)

main()














