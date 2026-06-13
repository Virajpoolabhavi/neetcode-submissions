class MyHashSet:

    def __init__(self):
        self.set_value = set()
        

    def add(self, key: int) -> None:
        self.set_value.add(key)
        

    def remove(self, key: int) -> None:
        self.set_value.discard(key)
        

    def contains(self, key: int) -> bool:
        return key in self.set_value
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)