def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().strip()


class Game:

    def __init__(self, input_data: str):
        self.input_data = [int(i) for i in input_data.strip().split(',')]
        self.history = dict()
        self.turn_no = 1
        self.next_number = 0
        for i in self.input_data:
            self.add_to_history(i)

    def add_to_history(self, number: int):
        next_number = 0
        if number in self.history.keys():
            next_number = self.turn_no - self.history[number]
        self.history[number] = self.turn_no
        self.turn_no += 1
        self.next_number = next_number

    def part1(self) -> int:
        while self.turn_no < 2020:
            self.add_to_history(self.next_number)
        return self.next_number

    def part2(self) -> int:
        while self.turn_no < 30000000:
            self.add_to_history(self.next_number)
        return self.next_number


def main():
    g1 = Game(read_file('input'))
    g2 = Game(read_file('input'))
    print('Part 1: ', g1.part1())
    print('Part 2: ', g2.part2())


if __name__ == '__main__':
    main()
