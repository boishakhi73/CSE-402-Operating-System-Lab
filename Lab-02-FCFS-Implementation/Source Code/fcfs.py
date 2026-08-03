processes = [
    ["P0", 3, 1],
    ["P1", 5, 3],
    ["P2", 2, 2],
    ["P3", 1, 2], 
    ["P4", 6, 3]
]

processes.sort(key=lambda x: x[1])

time = 0
total_tat = 0
total_wt = 0

print("PID\tAT\tBT\tCT\tAT\tWT")

for pid, at, bt in processes:
    if time < at:
        time = at 

    time = time + bt
    ct = time

    tat = ct - at

    wt = tat - bt

    total_tat += tat
    total_wt += wt

    print(pid, "\t", at, "\t", bt, "\t", ct, "\t", tat, "\t", wt)

ava_tat = total_tat / len(processes)
ava_wt = total_wt / len(processes)

print("\nAverage TAT =", ava_tat)
print("Average WT =", ava_wt)
