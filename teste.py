def fatorial(a:int,acc:int)->int:
    if a <= 1:
        return acc
    else:
        return fatorial(a - 1,acc - a)

def fibonacci():
    pass