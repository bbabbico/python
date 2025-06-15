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
    print(i)

#제너레이터
def num_gen():
    for i in range(3):
        yield i


g = num_gen()       # 제너레이터 객체 생성 
h = num_gen()       # 따로 생성하면 다른 객체가 됨.

num1 = next(g)
num2 = next(g)
num3 = next(g)

print(num1, num2, num3)

for i in h:
    print(i)

def num_gen1():
    yield 1
    yield 2
    yield 3

ppq = num_gen1()
print(ppq) # 제너레이터 함수는 호출시 정지된 상태부터 시작함.
print(next(ppq))
print(next(ppq))
print(next(ppq))