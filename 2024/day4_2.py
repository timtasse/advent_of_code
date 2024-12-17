# -*- coding: utf-8 -*-

class Field:
    value: str
    right: "Field" = None
    left: "Field" = None
    up: "Field" = None
    down: "Field" = None
    leftup: "Field" = None
    rightup: "Field" = None
    leftdown: "Field" = None
    rightdown: "Field" = None

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value

    def print(self):
        return (f"Field[{self.value}, r={self.right}, l={self.left}, u={self.up}, d={self.down}, "
                f"lu={self.leftup}, ld={self.leftdown}, ru={self.rightup}, rd={self.rightdown}]")

    def find_neighbors(self, letter: str) -> list[str]:
        names = []
        if self.right and letter == self.right.value:
            names.append("right")
        if self.left and letter == self.left.value:
            names.append("left")
        if self.up and letter == self.up.value:
            names.append("up")
        if self.down and letter == self.down.value:
            names.append("down")
        if self.leftup and letter == self.leftup.value:
            names.append("leftup")
        if self.leftdown and letter == self.leftdown.value:
            names.append("leftdown")
        if self.rightup and letter == self.rightup.value:
            names.append("rightup")
        if self.rightdown and letter == self.rightdown.value:
            names.append("rightdown")
        return names

    def get_diagonals(self):
        return [self.leftup, self.leftdown, self.rightup, self.rightdown]

    def find_neighbor_and_opposite(self, letter: str, opposing_letter: str) -> bool:
        if not self.rightup or not self.rightdown or not self.leftup or not self.leftdown:
            return False
        if sum([1 for i in self.get_diagonals() if i.value == letter]) == 2 and \
            sum([1 for i in self.get_diagonals() if i.value == opposing_letter]) == 2:
            if self.leftup.value == letter and self.rightdown.value == opposing_letter:
                return True
            if self.rightup.value == letter and self.leftdown.value == opposing_letter:
                return True
            if self.leftdown.value == letter and self.rightup.value == opposing_letter:
                return True
            if self.rightdown.value == letter and self.leftup.value == opposing_letter:
                return True
        return False



class Fields:
    fields: list[list[Field]]

    def __init__(self):
        self.fields = []

    def add_line(self, line: list[Field]):
        self.fields.append(line)

    def __repr__(self):
        return f"Fields[{''.join([repr(i) for i in self.fields])}]"

sample = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

all = Fields()
#for line in sample.splitlines():
#    all.add_line([Field(i) for i in line])
with open("day4_input.txt") as fd:
    for line in fd:
        all.add_line([Field(i) for i in line])
for i, line in enumerate(all.fields):
    for j, field in enumerate(line):
        field.right = line[j+1] if len(line) -1 > j else None
        field.left = line[j-1] if j > 0 else None
        field.up = all.fields[i-1][j] if i > 0 else None
        field.down = all.fields[i+1][j] if len(all.fields) -1 > i else None
        field.leftup = all.fields[i-1][j-1] if i > 0 and j > 0 else None
        field.leftdown = all.fields[i+1][j-1] if len(all.fields) -1 > i and j > 0 else None
        field.rightup = all.fields[i-1][j+1] if i > 0 and len(line) -1 > j else None
        field.rightdown = all.fields[i+1][j+1] if len(all.fields) -1 > i and len(line) -1 > j else None

print("parsed")

def follow_direction(field: Field, direction: str, letters: list[str]) -> bool:
    letter = letters.pop(0)
    #print(f"letter: {letter}")
    new_field = getattr(field, direction)
    if new_field and new_field.value == letter:
        #print(f"new_field value: {new_field.value}")
        if len(letters):
            #print(f"letters: {letters}")
            return follow_direction(new_field, direction, letters)
        return True
    return False

summ = 0
for line in all.fields:
    #print("Line:")
    for field in line:
        #print(field.print())
        if field.value == "A":
            if field.find_neighbor_and_opposite("M", "S"):
                summ += 1
            #for direction in field.find_neighbors("M"):
            #    erg = follow_direction(field, direction, list("MAS"))
            #    if erg:
            #        summ += 1

print(summ)
