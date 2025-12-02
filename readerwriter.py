import threading
import time
import random

condition = threading.Condition()
x = 0
reader_count = 0

def reader(i):
    global x
    global reader_count
    with condition:
        while reader_count == -1:
            condition.wait()
            print(f"Reader {i} is waiting")
        
    reader_count += 1 
    print(f"Reader {i} is now reading")
    print("Shared data is now: ",x)

    with condition:
        reader_count -= 1
        if reader_count == 0:
            print("No readers are reading")
            condition.notify()

def writer(i):
    global x
    global reader_count
    with condition:
        while reader_count>0:
            condition.wait()
            print(f"Writer {i} is Waiting")
    reader_count = -1
    print(f"Writer {i} is now writing")
    time.sleep(0.1)
    x += 1
    print(f"{i} Value of shared memory: ",x)

    with condition:
        reader_count = 0
        condition.notify()
        print(f"Writer {i} has finished writing!")


if __name__ == "__main__":
    val = 10
    readers = [threading.Thread(target = reader, args=(i,)) for i in range(val)]
    writers = [threading.Thread(target = writer, args=(i,)) for i in range(val)]

    total = readers+writers
    random.shuffle(total)

    for i in total:
        i.start()

    for i in total:
        i.join()
