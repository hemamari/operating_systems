
# Process = [priority, pid, burst_time, arrival_time]

process_list = [[5,"p1",6,2],[2,"p2",2,5],[4,"p3",8,1],[1,"p4",3,0],[3,"p5",4,4]]

t = 0
gantt = []
completed = {}
burst_times = {}
for p in process_list:
    burst_times[p[1]] = p[2]
while process_list != []:
    available = []
    for p in process_list:
        arrival_time = p[3]
        if arrival_time <= t:
            available.append(p)
    if available == []:
        gantt.append("Idle")
        t += 1
        continue
    else:
        available.sort()
        process = available[0]
        gantt.append(process[1])
        t += 1
        process_list.remove(process)
        process[2] -= 1
        if process[2] == 0:
            pid = process[1]
            arrival_time = process[3]
            burst_time = burst_times[pid]
            ct = t
            tt = ct - arrival_time
            wt = tt - burst_time
            completed[pid] = [ct,tt,wt]
            continue
        else:
            process_list.append(process)

print("Priority Pre-emptive Scheduling")
print("The order of execution of the processes : ")     
print(gantt)
print("The completion time, turnaround time and waiting time of each process : ")
print(completed)