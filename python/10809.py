# python 키보드 input 읽어오기
value = input()

for i in range(26):

    #find() 함수는 주어진 글자 내 있는 첫 번째 글자 위치를 찾아냄
    print(value.find(chr(i + ord('a'))))