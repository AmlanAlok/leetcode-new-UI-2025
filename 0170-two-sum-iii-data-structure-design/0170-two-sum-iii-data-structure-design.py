class TwoSum:

    def __init__(self):
        self.d = {}

    def add(self, number: int) -> None:
        self.d[number] = self.d.get(number, 0) + 1
        
    def find(self, value: int) -> bool:

        nums = self.d.keys()

        for n in nums:
            comp = value - n

            if comp != n:
                if comp in self.d:
                    return True
            else:
                if self.d[n] >= 2:
                    return True
            
        return False


        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)