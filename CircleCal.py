import math

radius = float(input("원의 반지름을 입력해주세요 : "))

circumferene = round(2 * math.pi * radius, 3)
area = round(math.pi * (radius ** 2), 3)

print(f"원의 둘레는 {circumferene}, 원의 넓이는 {area} 입니다")