input_data = open('input.txt', 'r')
data = input_data.read()
data = data.split()

a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])

ans_1 = []

for x in range(-100, 101):
    if a * (x ** 3) + b * (x ** 2) + c * x + d == 0:
        ans_1.append(str(x))



ans = ''

for el in ans_1:
    ans += el +' '


output_data = open('output.txt', 'w')
output_data.write(ans)

input_data.close()
output_data.close()