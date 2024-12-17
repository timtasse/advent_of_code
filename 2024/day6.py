# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class Field:
    x: int
    y: int
    val: str

    def is_blocked(self):
        return self.val == "#"

    def visit(self):
        self.val = "X"

    def is_visited(self):
        return 1 if self.val == "X" else 0

@dataclass
class Game:
    fields: list[Field]
    pos_x: int
    pos_y: int
    max_x: int
    max_y: int
    direction: str

    def __init__(self):
        self.fields = list()
        self.pos_x = 0
        self.pos_y = 0

    def add_field(self, val: str, x: int, y: int):
        if val == "." or val == "#":
            self.fields.append(Field(x, y, val))
        elif val in ("^", "v", "<", ">"):
            self.fields.append(Field(x, y, "X"))
            self.pos_x = x
            self.pos_y = y
            self.direction = val

    def get_direction_change(self) -> Callable:
        match self.direction:
            case "<":
                return lambda x, y: (x-1, y)
            case ">":
                return lambda x, y: (x+1, y)
            case "^":
                return lambda x, y: (x, y-1)
            case "v":
                return lambda x, y: (x, y+1)

    def rotate(self):
        match self.direction:
            case '^':
                self.direction = ">"
            case ">":
                self.direction = "v"
            case "v":
                self.direction = "<"
            case "<":
                self.direction = "^"

    def get_field(self, x: int, y: int) -> Optional[Field]:
        for field in self.fields:
            if field.x == x and field.y == y:
                return field

    def count_visited(self) -> int:
        summ = 0
        for field in self.fields:
            if field.is_visited():
                summ += 1
        return summ

    def run(self) -> bool:
        x, y = self.get_direction_change()(self.pos_x, self.pos_y)
        if (0 <= x <= self.max_x) and (0 <= y <= self.max_y):
            #print(f"valid: {x}, {y}")
            field = self.get_field(x, y)
            if field.is_blocked():
                self.rotate()
            else:
                field.visit()
                self.pos_x = x
                self.pos_y = y
            return False
        else:
            print("finished")
            return True

    @staticmethod
    def parse(data: str) -> "Game":
        game = Game()
        for y, line in enumerate(data.splitlines()):
            for x, char in enumerate(list(line)):
                game.add_field(char, x, y)
        game.max_x = x
        game.max_y = y
        return game


TEST = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

def run_test():
    game = Game.parse(TEST)
    #print(game)
    while not game.run():
        pass
    print(f"final field: {game.pos_x}, {game.pos_y}")
    print(f"{game.count_visited()} fields visited")

def run():
    with open("day6_input.txt") as fd:
        game = Game.parse(fd.read())
    while not game.run():
        pass
    print(f"final field: {game.pos_x}, {game.pos_y}")
    print(f"{game.count_visited()} fields visited")


if __name__ == '__main__':
    run()
