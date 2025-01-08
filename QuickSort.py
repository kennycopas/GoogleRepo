class QuickSort:
    def __init__(self, array):
        self.array = array
        self.size = len(array)
        self.iSort()

    # Iterative QuickSort method
    def iSort(self):
        # Simple Median of Three helper function, takes left and right indicies of an array that represents
        # a subarray and returns the median of the first, middle, and last elements
        def mot(l, r):
            m = int((r - l) / 2 + l)
            ll, mm, rr = self.array[l], self.array[m], self.array[r]
            if ll < mm < rr or ll > mm > rr:
                return m
            elif mm < ll < rr or mm > ll > rr:
                return l
            else:
                return r

        # This queue holds the left and right indicies of the array representing the subarrays that are
        # pushed to the queue during a BFS, initialized with the left and right bounds of the original array
        boundsQueue = [[0, self.size-1]]
        while boundsQueue:
            # Set the left and right bounds to the next coordinates in the queue
            l, r = boundsQueue[0]
            # Base case
            if (r - l) < 2:
                if self.array[l] > self.array[r]:
                    self.array[l], self.array[r] = self.array[r], self.array[l]
                boundsQueue.pop(0)
                continue
            # Find the median of the subarray
            median = mot(l, r)
            # Swap the selected pivot with the last element in the subarray and store the pivot value and index
            self.array[median], self.array[r] = self.array[r], self.array[median]
            pivot, pIndex = self.array[r], r
            # While bounds are not crossed, move the left and right pivots towards each other,
            # swapping elements when both conditions are met
            while l <= r:
                # While the left bound is in bounds, has not crossed the right bound, and is less than
                # the pivot value, move the left bound right
                while l <= r and l < self.size-1 and self.array[l] < pivot:
                    l += 1
                # While the right bound is in bounds, has not crossed the left bound, and is greater than
                # or equal to the pivot value, move the right bound left
                while r >= l and r > 0 and self.array[r] >= pivot:
                    r -= 1
                # If bounds have not crossed, swap the elements at each bound
                if l < r:
                    self.array[l], self.array[r] = self.array[r], self.array[l]
            # Once bounds have crossed, swap the pivot with the element at the right bound,
            # push the coordinates of the surrounding subarrays to the queue, and remove the current
            # coordinates from the queue
            self.array[pIndex], self.array[l] = self.array[l], self.array[pIndex]
            boundsQueue.append([boundsQueue[0][0], r])
            boundsQueue.append([l + 1, boundsQueue[0][1]])
            boundsQueue.pop(0)

    def printList(self):
        print(self.array)

testList = [7, 67, 69, 41, 39, 98, 6, 79, 33, 86]
sortedList = QuickSort(testList)
sortedList.printList()
