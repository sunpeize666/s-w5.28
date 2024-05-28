'''
2024년05월28일
202195057 손패택
'''
def print_3_time() :
    print("안녕하세요.")
    print("손패택입니다.")
    print("오늘은 화요일입니다.")

print("함수호출 1")
print_3_time()

print()

'''
함수의 매개 변수 
함수를 호출할 때 값을 가지고 호출하는 경우
그 값이 저장된 변수를 실 매개 변수라고 한다.
 (전달하는 값) 
 함수가 호출 당하면 함수가 전해 받은 값을
   저장하는 변수를  매개 변수라고 한다.
(전달받는 값)
'''
print("매개 번수로 값을 전달하여 함수에서 결과 출력")

def print_n_time(value,n) :
    for i in range(n):
        print(i,":",value)

print("함수 호출 2")
print_n_time('손패택',5)

print()

'''
함수의 값 반환
return 문을 사용하여 함수를 종료하고, 결과를 돌려준다.
return이 없으면 반환되는 값이 없다. 
원의 넓이를 구하는 프로그램 작성.
원의 넓이를 계산하는 영역을 함수로 작성한다. 
함수는 원의 넓이를 계산하고 그 결과를 돌려준다.

'''
print("원의 넓이 구하기")

def area(r):
    result = r* r * 3.14
    return result
r = int(input("반지름을 입력하시호:"))

result = area(r)

print(f"반지름이(r)인 원의 넓이: {result:.1f}")

print(f"반지름이(r)인 원의 넓이: {area(r):.1f}")




