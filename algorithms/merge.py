import numpy as np
from algorithms.algorithm import Algorithm, Operator

class Merge(Algorithm):
    def __init__(self, nums: list[int]):
        super().__init__(nums)

    def sort(self) -> None:
        self.merge(0, len(self.nums) - 1)

    # Recursive function to run merge sort
    def merge(self, start: int, end: int) -> None:
        # Base case
        if (start >= end):
            self.frames.append((Operator.COMP, start, end))
            return

        # Sort left and right sides
        mid = (start + end) // 2
        self.merge(start, mid)
        self.merge(mid + 1, end)

        # Merge step
        l_part = np.copy(self.nums[start : mid + 1])
        r_part = np.copy(self.nums[mid + 1 : end + 1])
        l_ptr, r_ptr = 0, 0


        for num_ptr in range(start, end + 1):
            if (l_ptr < len(l_part) and r_ptr < len(r_part)):
                if (l_part[l_ptr] <= r_part[r_ptr]):
                    self.nums[num_ptr] = l_part[l_ptr]
                    self.frames.append((Operator.INS, num_ptr, l_part[l_ptr]))
                    l_ptr += 1
                else:
                    self.nums[num_ptr] = r_part[r_ptr]
                    self.frames.append((Operator.INS, num_ptr, r_part[r_ptr]))
                    r_ptr += 1
            elif (l_ptr < len(l_part)):
                self.nums[num_ptr] = l_part[l_ptr]
                self.frames.append((Operator.INS, num_ptr, l_part[l_ptr]))
                l_ptr += 1
            else:
                self.nums[num_ptr] = r_part[r_ptr]
                self.frames.append((Operator.INS, num_ptr, r_part[r_ptr]))
                r_ptr += 1
