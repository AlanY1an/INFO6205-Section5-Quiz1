from typing import List


class InsertionSort:
    def __init__(self, array):
        self.array = array

    def sort(self) -> List:
        """Sorts the array using Insertion Sort."""
        for i in range(1, len(self.array)):
            self.insert(i)
        return self.array

    def insert(self, i):
        """Inserts the 'Transition element' into its correct position in the sorted portion of the array."""
        for j in range(i, 0, -1):  # Loop while j > 0
            if self.array[j] < self.array[j - 1]:
                self.swap(j, j - 1)
            else:
                break

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]



