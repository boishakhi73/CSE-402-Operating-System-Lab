process = ["P1","P2", "P3", "P4", "P5", "P6"]

AT = [0, 1, 2, 3, 4 ,4]
BT = [7, 4, 15, 11, 20, 9]

n = len(process)
quantam = 5

remaining = BT.copy()
CT = [0] * n

time = 0
queue = []
visited = [False] * n

queue.append(0)
visited[0] = True

while queue:
    p = queue.pop(0)

    if remaining[p] > quantam:
        time += quantam
        remaining[p] -= quantam
    else:
        time += remaining[p]
        remaining[p] = 0
        CT[p] = time


    for i in range(n):

        if AT[i] <= time and not visited[i]:
            queue.append(i)
            visited[i] = True


    if remaining[p] > 0:
        queue.append(p)


TAT = [0] * n
WT = [0] * n

for i in range(n):
    TAT[i] = CT[i] - AT[i]
    WT[i] = TAT[i] - BT[i]


print("Process\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(process[i], "\t", AT[i], "\t", BT[i], "\t", CT[i], "\t", TAT[i], "\t", WT[i])



rr_ava_tat = sum(TAT) / len(process)
rr_ava_wt = sum(WT) / len(process)

print("\nAverage TAT =", rr_ava_tat)
print("Average WT =", rr_ava_wt)





# SJF Non - Preemptive

process = ["p1", "p2", "p3", "p4", "p5"]
at = [0, 1, 2, 3, 4, 4]
bt = [7, 4, 15, 11, 20, 9]

n = len(process)

ct = [0] * n
wt = [0] * n
done = [0] * n
tat = [0] * n

time = 0
completed = 0

while completed < n:

    x = -1

    for i in range(n):

        if at[i] <= time and done[i] == 0:

            if x == -1 or bt[i] < bt[x]:
                x = i

    if x == -1:
        time += 1

    else:
        time = time + bt[x]

        ct[x] = time
        done[x] = 1
        completed += 1


for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]


print("Process\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(process[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])


print("\nAverage TAT =", sum(tat)/n)
print("Average WT =", sum(wt)/n)


print("\n")

# FCFS
processes = [
    ["P1", 3, 3],
    ["P2", 2, 5],
    ["P3", 5, 5],
    ["P4", 1, 3], 
    ["P5", 6, 2]
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
