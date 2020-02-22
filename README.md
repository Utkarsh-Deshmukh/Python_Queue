# Python_Queue  
in python you can implement queue using various methods. This study is comparing the performance of these techniques  

We will take a look at two such methods: **Using List as a queue**  and  **using queue.Queue()**  

Implementation:  

### 1) Using List to implement a queue:  
L = []  
L.append(1)       --> Adding 1 to the queue  
L.append(2)       --> Adding 2 to the queue  
L.append(3)       --> Adding 3 to the queue  
  
L.pop(0)          --> Popping the element at 0 : ans will be 1  
L.pop(0)          --> Popping the element at 0 : ans will be 2  
L.pop(0)          --> Popping the element at 0 : ans will be 3  

### 2) Using queue.Queue()  
import queue  
Q = queue.Queue()  
Q.put(1)  
Q.put(2)  
Q.put(3)  
  
Q.get()           --> Popping the first element : ans will be 1  
Q.get()           --> Popping the first element : ans will be 2  
Q.get()           --> Popping the first element : ans will be 3  
  
  
  
#######  
We would like to see which implementation is more effective.  
  
Note: For this test, I am comparing the time for inserting elements in the queue, and removing them  
  
  
### **Results**:
![Result](https://user-images.githubusercontent.com/13918778/75099397-0cf36100-5576-11ea-8d66-1615ba0b1c8c.png)


### Conclusion:
The time needed to insert N elements using __queue.Queue()__ seems to increase w.r.t N, where as for the List implementation, the time is almost constant

The time needed to remove all N elements using __queue.Queue()__ seems to increase w.r.t N, where as for the List implementation, the time increases non linearly w.r.t N

