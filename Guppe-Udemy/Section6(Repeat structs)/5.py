#float('inf')/float('-inf') = This is a special value that is used to represent positive/negative infinity .
maxi = float('-inf')
mini = float('inf')

for i in range(10):

    num = float(input(f"{i+1}/10: "))

    if num > maxi:
        maxi = num

    if num < mini:
        mini = num

print(f'{maxi}, {mini}')
print(f'{maxi}, {mini}')