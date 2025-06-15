# 컨텍스트 매니저, {with 컨텍스트 매니저 객체 as 변수} 형태로, 블록을 벗어나는 순간에 리소스(파일 할당 , 네트워크)를 자동으로 초기화함.
with open('test.txt', 'r') as f:
	sen = f.readline()
	print(f'컨텍스트 매니저\n{sen}\n')

#삼항 연산자 [참일때 실행] if 조건문 else [거짓일때 실행]
print('111') if 1>1000 else print(f'삼항연산자 0000\n')

#클로저
def outer():
    num = 1 #LEGB 규칙에 따라 Enclosed function locals 에 저장됨.
    def inner():
        print(f'클로저 : {num}');
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
    print('데코레이터 qweqweqweqwe')

# 일반적인 방식
ppp = deco(test)
ppp()

# 간단한 방식
@deco
def test2():
    print('데코레이터 222decodeco')

test2()

#이터레이터
class Season:
    def __init__(self):
        self.data = ["봄", "여름", "가을", "겨울"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            cur_season = self.data[self.index]
            self.index += 1
            return cur_season
        else:
            raise StopIteration
        
for i in Season():
    print(f'이터레이터 {i}')

#제너레이터
def num_gen():
    for i in range(3):
        yield i


g = num_gen()       # 제너레이터 객체 생성 
h = num_gen()       # 따로 생성하면 다른 객체가 됨.

num1 = next(g)
num2 = next(g)
num3 = next(g)

print('\n제너레이터')
print(num1, num2, num3)

for i in h:
    print(f'\n제너레이터 {i}')

def num_gen1():
    yield 1
    yield 2
    yield 3

ppq = num_gen1()
print(f'제너레이터 {ppq}') # 제너레이터 함수는 호출시 정지된 상태부터 시작함.
print(f'제너레이터 {next(ppq)}')
print(f'제너레이터 {next(ppq)}')
print(f'제너레이터 {next(ppq)}')

#가변 인자

#위치 가변인자
def foo(*args):
    print(f'가변인자 {args}')

foo(1, 2, 3)

#키워드 가변인자
def foo1(**kwargs):
    print(f'가변인자 {kwargs}')


foo1(a=1, b=2, c=3)

# 가변인자 섞어쓰기

def foo2(*args, **kwargs):
    print(f'가변인자 {args}')
    print(f'가변인자 {kwargs}')

foo2(1, 2, 3, a=1, b=1, c=2)

# 여러 데이터 가변인자로 간단히 보내기
def foo3(a, b, c):
    print('\n가변인자')
    print(a, b, c)


data = [1, 2, 3]
foo3(*data)