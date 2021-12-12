import numpy as np
from algorithms.algorithm import Algorithm, Operator

class Quick(Algorithm):
    def __init__(self, nums: list[int]):
        super().__init__(nums)

    def sort(self) -> None:
        self.quick(0, len(self.nums) - 1)

    # Recursive function to run quick sort
    def quick(self, start: int, end: int) -> None:
        # Base case
        if (start >= end):
            self.frames.append((Operator.COMP, start, end))
            return
        elif (start < 0):
            return

        # For basic quicksort, choose last element as pivot
        pivot = self.nums[end]
        l_ptr, r_ptr = start, end

        # Put all numbers smaller than the pivot before it, and greater than 
        # after
        while (True):
            while (self.nums[l_ptr] < pivot and l_ptr <= end): 
                self.frames.append((Operator.COMP, l_ptr, end))
                l_ptr += 1
            while (self.nums[r_ptr] >= pivot and r_ptr >= 0): 
                self.frames.append((Operator.COMP, r_ptr, end))
                r_ptr -= 1

            if (l_ptr >= r_ptr): 
                self.frames.append((Operator.COMP, l_ptr, l_ptr))
                break

            self.nums[l_ptr], self.nums[r_ptr] = \
                    self.nums[r_ptr], self.nums[l_ptr]
            self.frames.append((Operator.SWAP, l_ptr, r_ptr))

        # Put the pivot in the right place and sort to the left and right of it
        self.nums[l_ptr], self.nums[end] = self.nums[end], self.nums[l_ptr]
        self.frames.append((Operator.SWAP, l_ptr, end))

        self.quick(start, l_ptr - 1)
        self.quick(l_ptr + 1, end)

