from algorithms.algorithm import Algorithm, Operator

class Selection(Algorithm):
    def __init__(self, nums: list[int]):
        super().__init__(nums)

    def sort(self):
        '''
        Perform selection sort, appending all intermediate stages to list for
        visualization
        '''

        for i in range(len(self.nums) - 1):
            min = i
            
            for j in range(i + 1, len(self.nums)):
                self.frames.append((Operator.COMP, j, min))
                if (self.nums[j] < self.nums[min]): min = j

            if (min != i):
                self.nums[i], self.nums[min] = self.nums[min], self.nums[i]
                self.frames.append((Operator.SWAP, i, min))
