#SRTF / SJF Pre-emptive

# Process: [burst_time, arrival_time, pid]
"""Interrupt
Check the lowest burst time
"""

process_list=[[6,2,"p1"],[2,5,"p2"],[8,1,"p3"],[3,0,"p4"],[4,4,"p5"]]


gantt = []
burst_times = {}
for i in process_list:
    burst_times[i[2]] = i[0]
completion = {}
t = 0
while process_list != []:
    
    available = []
    for p in process_list:
        if p[1] <= t:
            available.append(p)
    
    if available == []:
        t += 1
        gantt.append("Idle")
        continue
    else:
        available.sort()
        process = available[0]
        copy_process = available.pop(0)
        t += 1
        gantt.append(process[2])
        #updating the burst time of the process
        process[0] -= 1
        process_list.remove(copy_process)
        if process[0] == 0:
            #this is where we have to note down our completion times
            process_name = process[2]
            arrival_time = process[1]
            burst_time = burst_times[process_name]
            ct = t
            tt = ct - process[1]
            wt = tt - burst_time
            completion[process_name] = [ct,tt,wt]
            continue
        else:
            process_list.append(process)

print("The order of execution of the processes : ")
print(gantt)
print("The completion time, turnaround time and waiting time of each process : ")
print(completion)
