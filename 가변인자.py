#가변 인자는 (일반변수 , *args , **kwargs) 순 으로만 작성되야한다.

#위치 가변인자
def foo(*args):
    print(args)

foo(1, 2, 3)

#키워드 가변인자
def foo1(**kwargs):
    print(kwargs)


foo1(a=1, b=2, c=3)

# 가변인자 섞어쓰기

def foo2(*args, **kwargs):
    print(args)
    print(kwargs)

foo2(1, 2, 3, a=1, b=1, c=2)

# 여러 데이터 가변인자로 간단히 보내기
def foo3(a, b, c):
    print(a, b, c)


data = [1, 2, 3]
foo3(*data)