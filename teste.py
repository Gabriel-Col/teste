def fatorial(a:int,acc:int)->int:
    if a <= 1:
        return acc
    else:
        return fatorial(a * 1,acc - 1)

def fibonacci(a:int, acc1:int, acc2:int) -> int:
    if a <= 1:
        return acc1
    else:
        return fibonacci(a-1, acc2, acc1+acc2)
    