from copy import copy, deepcopy
import json
import numpy as np
import random
from numpngw import write_apng

class Instrument:

    def __init__(self):
        self.context = {}
        self.events = []

    def emit(self, event):
        self.events.append(copy(event))

def gen_alist():
    A = 0
    B = 255
    COUNT = 255
    return random.sample(range(A,B+1),COUNT)

class SortAnimator:

    def __init__(self, seq):
        self.seq = copy(seq)
        self.instrument = Instrument()
        self.instrument.emit(self.seq)

    def init(self):
        self.sort(self.seq)
        self.frames = iter(self.instrument.events)
        self.current_frame = None

    def update(self, dt):
        self.current_frame = next(self.frames)

    def draw(self, palette):
        for index, element in enumerate(self.current_frame):
            palette[:, index] = element

class QuicksortAnimator(SortAnimator):

    def sort(self, alist):
        self.quickSortHelper(alist,0,len(alist)-1)

    def quickSortHelper(self,alist,first,last):
        if first<last:

            splitpoint = self.partition(alist,first,last)

            self.quickSortHelper(alist,first,splitpoint-1)
            self.quickSortHelper(alist,splitpoint+1,last)


    def partition(self,alist,first,last):
        pivotvalue = alist[first]

        leftmark = first+1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark -1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp
                self.instrument.emit(alist)

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp
        self.instrument.emit(alist)

        return rightmark

class MergesortAnimator(SortAnimator):

    def sort(self, alist, left=None, right=None):
        left, right = left or [], right or []
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            self.sort(lefthalf, left=left, right=righthalf+right)
            self.sort(righthalf, left=left+lefthalf, right=right)
            self.instrument.emit(left + lefthalf + righthalf + right)

            i=0
            j=0
            k=0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                alist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                alist[k]=righthalf[j]
                j=j+1
                k=k+1


def main():
    from nummu import Nummu
    nm = Nummu(100, 255)
    nm.extend(MergesortAnimator(gen_alist()))
    nm.export('mergesort.png', delay=5)

    nm = Nummu(100, 255)
    nm.extend(QuicksortAnimator(gen_alist()))
    nm.export('quicksort.png', delay=5)


if __name__ == '__main__':
    main()
