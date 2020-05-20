class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
    
    def get(self, key:int)->int:
        return -1
    def put(self, key:int, value: int) -> None:
        

if __name__=='__main__':
    LRUCache cache = new LRUCache(2)
    cache.put(2, 2)
    cache.get(1)    #returns 1
    cache.put(3, 3) #evicts key 2
    cache.get(2)    #returns -1 (not found)
    cache.put(4, 4) #evicts key 1
    cache.get(1)    #returns -1 (not found)
    cache.get(3)    #returns 3
    cache.get(4)    #returns 4