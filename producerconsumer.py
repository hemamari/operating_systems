import threading
import time

BUFFER_SIZE = 5
buffer = [0] * BUFFER_SIZE
in_index = 0
out_index = 0

empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)           
mutex = threading.Lock()                

def producer():
    global in_index
    for item in range(1, 11): 
        empty.acquire()       

        with mutex:           
            buffer[in_index] = item
            print(f"Producer produced item {item} at buffer index {in_index}")
            in_index = (in_index + 1) % BUFFER_SIZE

        full.release()        
        time.sleep(1)         

def consumer():
    global out_index
    for i in range(1, 11):   
        full.acquire()       

        with mutex:          
            item = buffer[out_index]
            print(f"Consumer consumed item {item} from buffer index {out_index}")
            out_index = (out_index + 1) % BUFFER_SIZE  

        empty.release()        
        time.sleep(2)          

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("\nAll items produced and consumed successfully!")
