first = []
second = []

with open('input', 'r') as file:
    for line in file: 
        arr = line.split("   ")
        arr[-1] =arr[-1].strip("\n")
        first.append(arr[0])
        second.append(arr[-1])
        
first = sorted(first)
second = sorted(second)

total_diff = 0
for i, j in zip(first, second):
    total_diff += abs(int(i) - int(j))

print(total_diff)