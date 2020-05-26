#완전수 구하기
def getDivisor(num):
    sum = 1
    divisor = [] #약수를 저장하기 위한 배열
    isVisit = [0] * num #계산 여부 표시를 위해 만든 배열

    divisor.append(1)

    # 2 ~ num -1 까지 돌면서 약수를 계산
    for i in range(2, num):
        if isVisit[i] != 1:
            if num % i == 0 :
                val = int(num / i)

                sum += (i + val)

                divisor.append(i)
                divisor.append(val)

                isVisit[i] = 1
                isVisit[val] = 1

    # 숫자를 오름차순으로 만듦
    divisor.sort()
    return (sum, divisor)


#입력을 받음
num = int(input())

while num != -1:
    sum, divisor = getDivisor(num)

    if sum == num:
        print(str(num)+" = ", end='')
        size = len(divisor)

        for i in range(size):
            if i!= size - 1:
                print(divisor[i], end=" + ")
            else:
                print(divisor[i])
    else:
        print(str(num) + " is NOT perfect.")

    num = int(input())

