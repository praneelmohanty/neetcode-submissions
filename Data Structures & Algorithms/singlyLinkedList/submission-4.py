class LinkedList:
    def __init__(self):
        self.linkedList= []
    
    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.linkedList): 
            return -1 
        return self.linkedList[index]

    def insertHead(self, val: int) -> None:
        self.linkedList.insert(0,val)
           
    def insertTail(self, val: int) -> None:
        self.linkedList.append(val)   

    def remove(self, index: int) -> bool:
        if index < 0 or index >= len(self.linkedList): 
            return False
        self.linkedList.pop(index)
        return True

    def getValues(self) -> List[int]:
        return  self.linkedList
