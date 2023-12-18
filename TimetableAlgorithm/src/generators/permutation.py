import multiprocessing
from itertools import permutations


class DayPermutationGenerator(multiprocessing.Process):
    def __init__(self, subjects: []):
        super().__init__()
        self.subjects = subjects

    def run(self):
        return permutations(self.subjects)
