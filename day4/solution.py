def count_xmas(m, i, j):
    count = 0
    if j+3 < len(m[0]):
        if m[i][j + 1] == "M" and m[i][j + 2] == "A" and m[i][j + 3] == "S":
            count += 1
    if j-3 >= 0:
        if m[i][j - 1] == "M" and m[i][j - 2] == "A" and m[i][j - 3] == "S":
            count += 1
    if i+3 < len(m):
        if m[i + 1][j] == "M" and m[i + 2][j] == "A" and m[i + 3][j] == "S":
            count += 1
    if i-3 >= 0:
        if m[i - 1][j] == "M" and m[i - 2][j] == "A" and m[i - 3][j] == "S":
            count += 1
    
    if j+3 < len(m[0]) and i+3 < len(m):
        if m[i + 1][j + 1] == "M" and m[i + 2][j + 2] == "A" and m[i + 3][j + 3] == "S":
            count += 1

    if j-3 >= 0 and i+3 < len(m):
        if m[i + 1][j - 1] == "M" and m[i + 2][j - 2] == "A" and m[i + 3][j - 3] == "S":
            count += 1
            
    if j-3 >= 0 and i-3 >= 0:
        if m[i - 1][j - 1] == "M" and m[i - 2][j - 2] == "A" and m[i - 3][j - 3] == "S":
            count += 1
    
    if j+3 < len(m[0]) and i-3 >= 0:
        if m[i - 1][j + 1] == "M" and m[i - 2][j + 2] == "A" and m[i - 3][j + 3] == "S":
            count += 1
    return count
    


m = []
total = 0
with open("day4/input", "r") as f:
    for line in f.readlines():
        m.append(line.strip("\n"))
        
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "X":
            total += count_xmas(m, i, j)
print(total)