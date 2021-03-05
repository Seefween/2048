## @file SetOfInt.py
#  @author Safwan Hossain, Hossam18, 400252391
#  @brief Set of integers
#  @date 03/04/2021

class SetOfInt:

    def __init__(self, x):
        self.s = {a for a in x}

    def set_to_seq(self, s):
        return [x for x in s]

    def complement(self, A):
        return {x for x in A}

    def is_member(self, x):
        for a in self.s:
            if a == x:
                return True
        return False

    def to_seq(self):
        return self.set_to_seq(self.s)

    def union(self, t):
        return SetOfInt(self.to_seq() + t.to_seq())

    def diff(self, t):
        intersec = self.s.intersection(self.complement(t))
        return SetOfInt(self.set_to_seq(intersec))

    def size(self):
        return len(self.s)

    def empty(self):
        return self.size() == 0

    def equals(self, t):
        for x in t.to_seq():
            if self.is_member(x):
                return True
        return False
