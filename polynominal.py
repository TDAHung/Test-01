array_coefficient = []
n = int(input("Moi ban nhap so n = "))
for i in range(1, n + 1):
    print("Moi ban nhap he so a", end="")
    print(i, ": ", end="")
    array_coefficient.append(float(input()))

x = float(input("Moi ban nhap x0: "))
answer = 0.0
print
j = n - 1
while j >= 0:
    answer += array_coefficient[j - n] * pow(x, n - j)
    j = j - 1

print("f(x0) = ", end="")
print("f(", end="")
print(x, end="")
print(") = ", answer)
