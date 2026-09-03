num1 = [1, 2, 2, 1]
num2 = [2, 2]

seen = set(num1)
res = []

for n in num2:
    if n in seen:
        res.append(n)
        seen.remove(n)

print(res)    