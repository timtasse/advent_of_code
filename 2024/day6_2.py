# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class Field:
    x: int
    y: int
    val: str
    visit_counter: int
    visited: bool
    first_run: bool = True

    def __init__(self, x: int, y: int, val: str):
        self.x = x
        self.y = y
        self.val = val
        self.visited = False
        self.visit_counter = 0

    def is_blocked(self):
        return self.val == "#"

    def visit(self):
        self.visit_counter += 1
        if self.first_run:
            self.visited = True

    def is_visited(self):
        return 1 if self.visited else 0

@dataclass
class Game:
    fields: list[Field]
    pos_x: int
    pos_y: int
    max_x: int
    max_y: int
    init_x: int
    init_y: int
    direction: str
    init_dir: str

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
            self.init_x = x
            self.init_y = y
            self.direction = val
            self.init_dir = val

    def reset(self):
        self.pos_y = self.init_y
        self.pos_x = self.init_x
        self.direction = self.init_dir
        for field in self.fields:
            field.visit_counter = 0
            field.first_run = False

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
            elif field.visit_counter > 100:
                raise Exception("loop detected")
            else:
                field.visit()
                self.pos_x = x
                self.pos_y = y
            return False
        else:
            #print("finished")
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
    try:
        counter = 0
        max_counter = 1000
        while counter < max_counter:
            counter += 1
            if game.run():
                break
        print(f"counter: {counter}")
    except:
        pass
    print(f"final field: {game.pos_x}, {game.pos_y}")
    print(f"{game.count_visited()} fields visited")
    game.reset()
    run_test2(game)

def run_test2(game: Game):
    #print(game)
    counter = 0
    for x in range(game.max_x+1):
        for y in range(game.max_y+1):
            if x == 7 and y == 9:
                print("here")
            if test(game, x, y):
                counter += 1
            game.reset()
    print(counter)

def test(game: Game, x: int, y: int):
    #if x == 7 and y == 9:
    #    debug = True
    #else:
    #    debug = False
    field = game.get_field(x, y)
    if field.is_blocked() or not field.is_visited():
        return False
    field.val = "#"
    try:
        counter = 0
        while True:
            counter += 1
            #print(f"position: {game.pos_x}, {game.pos_y}") if debug else None
            if game.run():
                break
        print(f"counter: {counter}")
    except:
        field.val = "."
        print(f"loop found at field: {x}, {y}")
        return True
    field.val = "."
    return False

def run():
    with open("day6_input.txt") as fd:
        game = Game.parse(fd.read())
    while not game.run():
        pass
    print(f"final field: {game.pos_x}, {game.pos_y}")
    print(f"{game.count_visited()} fields visited")
    game.reset()
    run_test2(game)


if __name__ == '__main__':
    run_test()
