
sum = 0
avg = 0

lenght = int(input("Sum size: "))
for i in range(lenght):
    aux = int(input("Enter a number: "))
    if aux >= 0:
        sum += aux
    else:
        print("Invalid integer")
        break

avg = sum/lenght
print(f"Average equals {avg}")