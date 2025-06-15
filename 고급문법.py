# 컨텍스트 매니저, {with 컨텍스트 매니저 객체 as 변수} 형태로, 블록을 벗어나는 순간에 리소스(파일 할당 , 네트워크)를 자동으로 초기화함.
with open('test.txt', 'r') as f:
	sen = f.readline()
	print(sen)

#삼항 연산자 [참일때 실행] if 조건문 else [거짓일때 실행]
print('111') if 1>1000 else print('0000')