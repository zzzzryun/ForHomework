CalcType = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합게 : "))

if CalcType == 1:
    StrFormula = input(" *** 수식을 입력하세요 : ")
    formula = eval(StrFormula)
    print(f"{StrFormula} 결과는 {formula:5.1f} 입니다." )

elif CalcType == 2:
    FirstNum = int(input("*** 첫 번째 숫자를 입력하세요 : "))
    siguma = FirstNum
    SecondNum = int(input("*** 두 번째 숫자를 입력해주세요 : "))
    for i in range(FirstNum, SecondNum+1):
        siguma = siguma + i
    print(f"{FirstNum}+...+{SecondNum}는 {siguma}입니다.")

else:
    print("잘못된 입력입니다.")