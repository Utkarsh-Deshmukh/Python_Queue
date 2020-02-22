import queue
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    Queue_PopulatingTime = []
    Queue_ClearingTime = []

    List_PopulatingTime = []
    List_ClearingTime = []

    numberOfElements = [];

    for numElems in range(1,30000,100):
        numberOfElements.append(numElems)
        # Check timing for the queue.Queue implementation
        Q = queue.Queue()
        QueueTimeStart = time.time()
        for i in range(numElems):
            Q.put(i)
        QueueTimeEnd = time.time()
        timeForAddingElementsToQueue = QueueTimeEnd - QueueTimeStart
        Queue_PopulatingTime.append(timeForAddingElementsToQueue)

        QueueTimeStart = time.time()
        while (not Q.empty()):
            element = Q.get()
        QueueTimeEnd = time.time()
        timeForRemovingElementsFromQueue = QueueTimeEnd - QueueTimeStart
        Queue_ClearingTime.append(timeForRemovingElementsFromQueue)

        # Check timing for the List implementation of queue
        L = [];
        ListTimeStart = time.time()
        for i in range(numElems):
            L.append(i)
        ListTimeEnd = time.time()
        timeForAddingElementsToList = ListTimeEnd - ListTimeStart
        List_PopulatingTime.append(timeForAddingElementsToList)

        ListTimeStart = time.time()
        while (len(L) > 0):
            element = L.pop(0)
        ListTimeEnd = time.time()
        timeForRemovingElementsFromList = ListTimeEnd - ListTimeStart
        List_ClearingTime.append(timeForRemovingElementsFromList)

    # Plot Results
    plt.subplot(1, 2, 1)
    plt.plot(numberOfElements, Queue_PopulatingTime, label = "insertion time - queue.Queue()")
    plt.plot(numberOfElements, List_PopulatingTime, label="insertion time - using List")
    plt.legend(["insertion time - queue.Queue()", "insertion time - using List"])
    plt.grid(color='k', linestyle='-', linewidth=0.1)
    plt.xlabel('Number of elements in queue')
    plt.ylabel('Time needed to populate the queue')
    plt.ylim([0, 0.11])

    plt.subplot(1, 2, 2)
    plt.plot(numberOfElements, Queue_ClearingTime, label="removal time - queue.Queue()")
    plt.plot(numberOfElements, List_ClearingTime, label="removal time - using List")
    plt.legend(["removal time - queue.Queue()", "removal time - using List"])
    plt.grid(color='k', linestyle='-', linewidth=0.1)
    plt.xlabel('Number of elements in queue')
    plt.ylabel('Time needed to remove all the elements')
    plt.ylim([0, 0.11])
    plt.show()
