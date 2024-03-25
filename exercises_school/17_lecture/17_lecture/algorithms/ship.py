class Ship:
    def __init__(self, p):
        self.positions = p

    def get_num_of_positions(self):
        return len(self.positions)