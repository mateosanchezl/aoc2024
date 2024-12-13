m = []
with open("day6/input.txt", "r") as f:
    for line in f:
        m.append(list(line.strip()))

def move(m, i, j):
    if not i-1 >= 0 or not j+1 < len(m[i]) or not i+1 < len(m) or not j-1 >= 0:
        
        
        
        return False, (i, j)
    
    elif m[i][j] == "^":
        seen = (i, j)

        if i-1 >= 0:
            if m[i - 1][j] == "#":
                m[i][j] = ">"
            else:
                m[i - 1][j] = "^"      
                m[i][j] = "X"
    
    elif m[i][j] == ">":
        seen = (i, j)

        if j+1 < len(m[i]):
            if m[i][j + 1] == "#":
                m[i][j] = "↓"
            else:
                m[i][j + 1] = ">"         
                m[i][j] = "X"
                
    elif m[i][j] == "↓":
        seen = (i, j)
        
        if i+1 < len(m):
            if m[i + 1][j] == "#":
                m[i][j] = "<"
            else:
                m[i + 1][j] = "↓"     
                m[i][j] = "X"
    
    elif m[i][j] == "<":
        seen = (i, j)
        
        if j-1 >= 0:
            if m[i][j - 1] == "#":
                m[i][j] = "^"
            else:
                m[i][j - 1] = "<"
                m[i][j] = "X"
                
    return True, seen

moves = set()
could_move = True
while could_move:
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "^" or m[i][j] == ">" or m[i][j] == "↓" or m[i][j] == "<":
                
                could_move, seen = move(m, i, j)
                moves.add(seen)           
                

r = []
for line in m:
    ls = "".join(line)
    print(ls)  

print(len(moves))


    

