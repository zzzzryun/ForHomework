NumberType = int(input('입력 진수 결정(16/10/8/2) : '))

if NumberType == 16:
    InputNumber =  int(input('값 입력 : '),16)

if NumberType == 10:
    InputNumber = int(input('값 입력 : '),10)

if NumberType == 8:
    InputNumber =  int(input('값 입력 : '),8)

if NumberType == 2:
    InputNumber = int(input('값 입력 : '),2)

print('16진수 ==> ', hex(InputNumber))
print('10진수 ==> ', InputNumber)
print(' 8진수 ==> ', oct(InputNumber))
print(' 2진수 ==> ', bin(InputNumber))
