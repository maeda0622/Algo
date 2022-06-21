import heapq

def heap(array):
    list = []
    i=0
    heapq.heapify(array)
    while len(array) == i:
        list.append(heapq.heappop(array))
        heapq.heapify(list)
        i = i+1
        
    return list
    
a = [7,5,9,4,8,1,3,2,0,4,5]
print(heap(a))