n = int(input())           
data = [input() for _ in range(n)]

count = 0
for i in range(n - 1):
    if data[i] != data[i + 1]:
        count += 1

print(count + 1)
