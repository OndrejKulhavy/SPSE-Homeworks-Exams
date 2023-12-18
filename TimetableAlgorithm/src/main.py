from src.generators.timetable_gen import TimeTablePermuteGenerator
from data import default_timetable
from src.timetable_module.days import Day
from itertools import permutations
import time

if __name__ == "__main__":
    default_timetable = default_timetable.get_timetable()

    monday = default_timetable[Day.MONDAY]
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    start = time.time()
    per_list = list(permutations(array))
    end = time.time()
    print("Permutace obyc listu: ", end - start)

    start = time.time()
    per_monday = list(permutations(monday))
    end = time.time()
    print("Permutace dataclass: ", end - start)
