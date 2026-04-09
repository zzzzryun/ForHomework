import random

def getNumber():
    return random.randrange(1,46)

print("** 로또 추첨을 시작합니다. **\n")

lotto = []

while len(lotto) < 6:
    ball = getNumber()
    if ball not in lotto:
        lotto.append(ball)


print("추첨된 로또 번호 ==> ", end = '')
lotto.sort()
for i in range(0,6):
    print(f"{lotto[i]}", end =' ')