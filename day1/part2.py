first = []
second = []

with open('day1/input', 'r') as file:
    for line in file: 
        arr = line.split("   ")
        arr[-1] =arr[-1].strip("\n")
        first.append(arr[0])
        second.append(arr[-1])
        
        
total = 0
pairs = {}

for f in first:
    for s in second:
        if f == s:
            if f in pairs.keys():
                pairs[f] = pairs[f] + 1
            else:
                pairs[f] = 1

print(pairs)    
for num, occ in pairs.items():
    print(f"Adding {num} * {occ} to total")
    total += int(num) * occ 
    
print(total)