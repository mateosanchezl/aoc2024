def check_report_safe(report):
    safe = True
    if sorted(report) == report or sorted(report, reverse=True) == report:      
        for i in range(len(report) - 1):
            diff = abs(report[i]- report[i+1])
            if diff <= 0 or diff >= 4:
               safe = False
                    
    else:
        safe = False
    return safe

with open("day2/input", "r") as f:
    safe_count = 0
    for report in f:
        report = report.split(" ")
        report[-1] = report[-1].strip("\n")
        report = list(map(int, report))

        if check_report_safe(report):
            safe_count += 1
        else:
            safe = False
            for i in range(len(report)):
                sliced = report[:i] + report[i+1:]
                if check_report_safe(sliced):
                    safe = True
            if safe == True:
                safe_count += 1

    print(safe_count)
