x = int(input())
y = int(input())

result = str(x+y)
print(result)

length = len(result)

new_x = ""
new_y = ""
new_result = ""

for i in range(0, length):
    if result[i] != '0':
        new_result += result[i]

for i in range(0, length):
    if result[i] != '0':
        new_result += result[i]

print(new_result)