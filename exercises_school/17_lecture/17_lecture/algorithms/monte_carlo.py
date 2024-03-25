import random


class boat_monte_carlo:
    def __init__(self, s):
        self.ship = s
        self.permutations = []
        self.permutate(self.ship.positions, 1000)
        self.evaluate()

    def permutate(self, positions, num_of_try):
        for i in range(num_of_try):
            cp_positions = positions.copy()
            random.shuffle(cp_positions)
            self.permutations.append(cp_positions)

    def evaluate(self):
        i = 0
        cp_per = self.permutations.copy()
        self.permutations.clear()
        for p in cp_per:
            evaluation = p[self.ship.get_num_of_positions() - 1] - p[0]
            self.permutations.insert(i, (p, evaluation))
            i += 1

    def take_beast(self):
        cp_per = self.permutations.copy()
        list_of_best_indexes = [0]
        for i in range(len(cp_per)):
            points = cp_per[i][1]
            if points < 0:
                points *= -1
            for b in list_of_best_indexes:
                beast_points = cp_per[b][1]
                if beast_points < 0:
                    beast_points *= -1
                if points == beast_points and b != i:
                    list_of_best_indexes.append(i)
                if points < beast_points:
                    list_of_best_indexes.clear()
                    list_of_best_indexes.append(i)
        end = "best: "
        for beast in list_of_best_indexes:
            end += str(cp_per[beast][0]) + ", "
        return end[0:len(end) - 2]
