import re

total = 0
with open("day3/input", "r") as f:
    all = []
    for l in f.readlines():
        print(l)
        all.append(l)
    
    data = "".join(all)
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    tups = re.findall(pattern, data)
    
    do = True
    for match in tups:
        if match == "don't()":
            do = False
        if match == "do()":
            do = True
        
        if do:
            if match[0] == "m":
                nums = match[4:-1].split(",")
                total += int(nums[0]) * int(nums[1])

print(total)
    