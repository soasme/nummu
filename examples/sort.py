import sys
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


class SelectionsortAnimator(SortAnimator):

    def sort(self, seq):
        for i in range(len(seq)):

            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i+1, len(seq)):
                if seq[min_idx] > seq[j]:
                    min_idx = j

            # Swap the found minimum element with
            # the first element
            seq[i], seq[min_idx] = seq[min_idx], seq[i]
            self.instrument.emit(seq)

class BubblesortAnimator(SortAnimator):

    def sort(self, arr):
        n = len(arr)
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n-i-1):
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            self.instrument.emit(arr)

class InsertionsortAnimator(SortAnimator):

    def sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
            self.instrument.emit(arr)


class HeapsortAnimator(SortAnimator):
    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
        # Change root, if needed
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]  # swap
            # Heapify the root.
            self.heapify(arr, n, largest)
    # The main function to sort an array of given size
    def sort(self, arr):
        n = len(arr)
        # Build a maxheap.
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)
        # One by one extract elements
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]   # swap
            self.heapify(arr, i, 0)
            self.instrument.emit(arr)


class ShellsortAnimator(SortAnimator):

    def sort(self, arr):

        # Start with a big gap, then reduce the gap
        n = len(arr)
        gap = int(n/2)

        # Do a gapped insertion sort for this gap size.
        # The first gap elements a[0..gap-1] are already in gapped
        # order keep adding one more element until the entire array
        # is gap sorted
        while gap > 0:

            for i in range(gap,n):

                # add a[i] to the elements that have been gap sorted
                # save a[i] in temp and make a hole at position i
                temp = arr[i]

                # shift earlier gap-sorted elements up until the correct
                # location for a[i] is found
                j = i
                while  j >= gap and arr[j-gap] >temp:
                    arr[j] = arr[j-gap]
                    j -= gap

                # put temp (the original a[i]) in its correct location
                arr[j] = temp
                if i % 10:
                    self.instrument.emit(arr)
            gap = int(gap / 2)
            self.instrument.emit(arr)


class CombsortAnimator(SortAnimator):

    def getNextGap(self, gap):

        # Shrink gap by Shrink factor
        gap = (gap * 10)/13
        if gap < 1:
            return 1
        return int(gap)

    # Function to sort arr[] using Comb Sort
    def sort(self, arr):
        n = len(arr)

        # Initialize gap
        gap = n

        # Initialize swapped as true to make sure that
        # loop runs
        swapped = True

        # Keep running while gap is more than 1 and last
        # iteration caused a swap
        while gap !=1 or swapped == 1:

            # Find next gap
            gap = self.getNextGap(gap)

            # Initialize swapped as false so that we can
            # check if swap happened or not
            swapped = False

            # Compare all elements with current gap
            for i in range(0, n-gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap]=arr[i + gap], arr[i]
                    swapped = True
                    self.instrument.emit(arr)

class CountsortAnimator(SortAnimator):

    def sort(self, array, maxval=255):
        """in-place counting sort"""
        n = len(array)
        m = maxval + 1
        count = [0] * m               # init with zeros
        for a in array:
            count[a] += 1             # count occurences
        i = 0
        for a in range(m):            # emit
            for c in range(count[a]): # - emit 'count[a]' copies of 'a'
                array[i] = a
                i += 1
                self.instrument.emit(array)
        return array

def main(sortname):

    from nummu import Nummu
    try:
        clz = globals()[f'{sortname.title()}Animator']
    except KeyError:
        print('unknown sort: %s' % sortname)
        sys.exit(1)
    filename = f'{sortname}.png'
    nm = Nummu(100, 255)
    nm.extend(clz(gen_alist()))
    nm.export(filename, delay=5)


if __name__ == '__main__':
    sortname = sys.argv[1]
    main(sortname)
