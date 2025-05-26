N = int(input())

A = [0]*N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    
    stk = A[i]
    if stk >= num:
        while stk >= num:
            stack.append(num)
            num += 1
            answer += "+\n" # print + and space
        stack.pop()
        answer += "-\n"

    # else.. 현재값 < Ascending 자연수
    # 만약 pop()의 값이 현재 수열의 값 stk[i] 가 아니라면, 그 순간 이미 수열을 완성 할 수 없음 
    # stk < num .. pop()을 여러번 실행해서하도 현재 stk[i] < num  을 꺼내줌
    # 단, if pop() 의 결과값 > 주어진 수열의 수 : NO;




    else :
        stack.pop()

       

        