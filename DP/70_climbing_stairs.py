
n=3

steps=[1,2]


for i in range(2,n):
    steps.append(steps[i-1]+steps[i-2])
    print(steps)

