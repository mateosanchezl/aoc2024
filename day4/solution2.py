def count_x_mas(m, i, j):
    count = 0
    if i-1 >= 0 and i+1 < len(m) and j-1 >= 0 and j+1 < len(m[0]):
        if m[i - 1][j - 1] == "M" and m[i + 1][j + 1] == "S" or m[i - 1][j - 1] == "S" and m[i + 1][j + 1] == "M":
            if m[i + 1][j - 1] == "M" and m[i - 1][j + 1] == "S" or m[i + 1][j - 1] == "S" and m[i - 1][j + 1] == "M":
                count += 1


    return count

m = []
total = 0

with open("day4/input", "r") as f:
    for line in f.readlines():
        m.append(line.strip("\n"))
        
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "A":
            total += count_x_mas(m, i, j)

print(total)
