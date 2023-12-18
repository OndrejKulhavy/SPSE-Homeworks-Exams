from src.generators.permutation import DayPermutationGenerator
from src.timetable_module.timetable import Timetable


class TimeTablePermuteGenerator:
    def __init__(self, default_time_table: Timetable):
        self.default_timetable = default_time_table

    def generate(self):
        generators = []
        for day in self.default_timetable.subjects:
            generators.append(DayPermutationGenerator(day))
        for generator in generators:
            generator.start()

        for generator in generators:
            generator.join()
