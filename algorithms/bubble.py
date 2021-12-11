from algorithms.algorithm import Algorithm, Operator

class Bubble(Algorithm):
    def __init__(self, nums: list[int]):
        super().__init__(nums)

    def sort(self, *args):
        '''
        Perform bubble sort, appending all intermediate stages to list for
        visualization
        '''

        for i in range(len(self.nums)):
            for j in range(len(self.nums) - i - 1):
                # Show the comparison
                self.frames.append((Operator.COMP, j, j + 1))

                if self.nums[j] > self.nums[j + 1]:
                    # Show the swap
                    self.frames.append((Operator.SWAP, j, j + 1))
                    self.nums[j], self.nums[j + 1] = self.nums[j + 1], self.nums[j]

        # self.result.append(copy(self.nums))

        # for i in range(len(self.nums)):
        #     for j in range(len(self.nums) - i - 1):
        #         if self.nums[j] > self.nums[j + 1]:
        #             self.nums[j], self.nums[j + 1] = self.nums[j + 1], self.nums[j]
        #             self.result.append(copy(self.nums))
