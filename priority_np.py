
#Process : [Priority, pid, bursttime, arrival time]

process_list = [[5,"p1",6,2],[4,"p2",2,5],[1,"p3",8,1],[2,"p4",3,0],[3,"p5",4,4]]

gantt = []
t = 0
completed = {}
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
        process_list.remove(process)
        pid = process[1]
        gantt.append(pid)
        burst_time = process[2]
        t += burst_time
        ct = t
        arrival_time = process[3]
        tt = ct - arrival_time
        wt = tt - burst_time
        completed[pid] = [ct,tt,wt]

print("Priority Non Pre-emptive Scheduling")
print("The order of execution of the processes : ")
print(gantt)
print("The completion time, turnaround time and waiting time of each process : ")
print(completed)
