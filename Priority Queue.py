from math import inf
#Mriganka's priority queue implementation in Python
class priority_queue:
    def __init__(self):
        self.__queue = []
    def __str__(self):
        return "Class : Min Priority Queue Type"
    def add(self, val):
        self.__queue.append(val)
    def poll(self):
        c = inf
        minimum = 0
        try:
            for i in range(len(self.__queue)):
              if self.__queue[i] <= c:
                  c = self.__queue[i]
                  minimum = i
            return self.__queue.pop(minimum)
        except IndexError:
            return "Oppsss Too Bad you are trying to retrive from an empty priority queue"
            
A = priority_queue()
A.add(11)
A.add(2)
A.add(33)
A.add(-1)
A.add(5)
'''#1 function to change min priority queue to max priority queue, It accept a list as an
input and give the expected output for an max priority queue'''
def min_to_max_priority(queue):
    B = priority_queue()
    for i in queue:
        B.add(-1 * i)
    return [(-1 * B.poll()) for i in range(len(queue))]
print(min_to_max_priority([3,7,9,12,56,1]))
    
        
        
    

        
        
        
    
        
            
            
        
        



