#클로저
def outer():
    num = 1 #LEGB 규칙에 따라 Enclosed function locals 에 저장됨.
    def inner():
        print(num);
    return inner

i = outer() #변수에 함수를 할당
i()

#데코레이터
def deco(f):
    def qqq():
        print('----'*5)
        f()
        print('----'*5)
    return qqq

def test():
    print('qweqweqweqwe')

# 일반적인 방식
ppp = deco(test)
ppp()

# 간단한 방식
@deco
def test2():
    print('222decodeco')

test2()

# 클래스 데코레이터
class decoratorExample:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kargs):
        print("Start", self.func.__name__)
        self.func(*args, **kargs)
        print("End", self.func.__name__)

@decoratorExample
def test(a, b, c):
    print("Variables :", a,b,c)

test("1", 2, c="345")
