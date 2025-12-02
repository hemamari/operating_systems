process_list=[[6,2,"p1"],[2,5,"p2"],[8,1,"p3"],[3,0,"p4"],[4,4,"p5"]]#SJF (Non pre-emptive)
# Process: [burst_time, arrival_time, pid]


t = 0
gantt = []
completed ={}

while process_list != []:
    available = []
    for p in process_list:
        if p[1] <= t:
            available.append(p)
    #No processes available
    if available == []:
        t += 1
        gantt.append("Idle")
        continue
    else:
        available.sort()
        process = available[0]
        #Service the process
        burst_time = process[0]
        pid = process[2]
        arrival_time = process[1]
        t += burst_time
        gantt.append(pid)
        ct = t
        tt = ct - arrival_time
        wt = tt - burst_time
        process_list.remove(process)
        completed[pid] = [ct,tt,wt]
print("The order of execution of the processes : ")
print(gantt)
print("The completion time, turnaround time and waiting time of each process : ")
print(completed)
