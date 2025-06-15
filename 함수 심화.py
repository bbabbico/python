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

