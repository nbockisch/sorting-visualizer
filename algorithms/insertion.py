from algorithms.algorithm import Algorithm, Operator

class Insertion(Algorithm):
    def __init__(self, nums: list[int]):
        super().__init__(nums)

    def sort(self):
        '''
        Perform insertion sort, appending all intermediate stages to list for
        visualization
        '''

        for i in range(1, len(self.nums)):
            j = i
            while (j > 0 and self.nums[j - 1] > self.nums[j]):
                self.frames.append((Operator.COMP, j, j - 1))
                self.nums[j], self.nums[j - 1] = self.nums[j - 1], self.nums[j]
                self.frames.append((Operator.SWAP, j, j - 1))
                j -= 1
