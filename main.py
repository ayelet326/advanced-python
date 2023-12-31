from datetime import datetime
from functools import wraps

def runTIMEdecorator(func):
   @wraps(func)
   def wrapper(*args,**kwargs):
       start=datetime.now()
       print("in decorator")
       func(*args,**kwargs)
       print(f"the run time func:{datetime.now()-start}")
   return wrapper

@runTIMEdecorator
def func1(*args,**kwargs):
    print("func 1")
    print(args)


@runTIMEdecorator
def func2(*args,**kwargs):
    print("func 2")
    print(args)
    for number in range(args[0]):
        print(number)
    print(args)
    print(kwargs)


def cache_decorator(func):
   @wraps(func)
   def wrapper(*args,**kwargs):
       if func.__name__ not in allFunc:
           allFunc.update({func.__name__:{args[0]:func(*args,**kwargs)}})
       elif args[0] not in allFunc[func.__name__]:
           allFunc[func.__name__].update({args[0]: func(*args, **kwargs)})
       return allFunc[func.__name__][args[0]]

   return wrapper

@cache_decorator
def fib(n):
    x=[]

    i=0

    a=0

    b=1

    while i<n:

        x.append(a)

        i +=1

        c=a+b

        a=b

        b=c
    return x

@cache_decorator
def func3(num):
    return num+6;





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    allFunc={}
    print("hi")
    func1(1,2,2,3,5,name="ghf")
    print("*******")
    func2(1000)
    print("ex2//**************************")
    print(fib(10))
    print(fib(5))
    print(fib(10))
    print(func3(10))
    print (allFunc)
