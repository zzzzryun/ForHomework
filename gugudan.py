i,dan = 0, 0

for dan in range(2,10):
    print(f"#  {dan}단  #", end="\t")
print()
for i in range(1,10):
    for dan in range(2,10):
        print(f"{dan}X{i:3.0f}={dan*i:3.0f}", end="\t")
    print()