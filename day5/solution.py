def update_in_order(update, rules):
    ordered = True
    num_idx = dict()
    for i in range(len(update)):
        num_idx[update[i]] = i
        
    for rule in rules:
        if rule[0] in num_idx.keys() and rule[1] in num_idx.keys():
            if num_idx[rule[0]] > num_idx[rule[1]]:
                ordered = False
    return ordered

def order_update(update, rules):
    num_idx = dict()
    for i in range(len(update)):
        num_idx[update[i]] = i
    
    ordered = False
    
    while not ordered:
        for rule in rules:
            if rule[0] in num_idx.keys() and rule[1] in num_idx.keys():
                a_idx = num_idx[rule[0]]
                b_idx = num_idx[rule[1]]
                if a_idx > b_idx:
                    temp1 = update[a_idx]
                    update[a_idx] = update[b_idx]
                    update[b_idx] = temp1
                    # Reset num_idx with new update
                    num_idx = dict()
                    for i in range(len(update)):
                        num_idx[update[i]] = i
        
        if update_in_order(update, rules):
            ordered = True
    
    return update
            
with open("day5/input", "r") as f:
    rules = []
    updates = []
    # Get rules
    for line in f:
        if len(line) > 3:
            if line[2] == "|":
                rules.append([int(line[0:2]), int(line[3:-1])])
            else:
                updates.append([int(i) for i in line.strip().split(",")])
print(rules[0])

ok = []
af = []
for update in updates:
    m = update[int(len(update)/2)]
    if update_in_order(update, rules):
        ok.append(m)
    else:
        ordered = order_update(update, rules)
        m_after = ordered[int(len(update)/2)]
        af.append(m_after)
    
print(sum(af))
