from enum import Enum

class Operator(Enum):
    COMP = 1
    SWAP = 2
    INS = 3
    NONE = 4

class Algorithm:
    def __init__(self, nums: list[int]):
        self.nums = nums

        '''The steps of the sort, a tuple with whether it's a comparison or swap,
        and the indexes of the values'''
        self.frames = []
