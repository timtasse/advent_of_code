# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass
class Ordering:
    rules: list[tuple[int, int]]

    def add_rule(self, rule: list[int]):
        self.rules.append((rule[0], rule[1]))

    def find_rule(self, x, y) -> Optional[tuple[int, int]]:
        if (rule:= (x, y)) in self.rules:
            return rule
        elif (rule:= (y, x)) in self.rules:
            return rule
        return None

@dataclass
class Value:
    ordering: Ordering
    val: int

    def __lt__(self, other: 'Value') -> bool:
        rule = self.ordering.find_rule(self.val, other.val)
        if rule and rule[0] == self.val:
            return True
        return False

    def __repr__(self):
        return f"Value:[val={self.val}]"


def check_line(line: str, ordering: Ordering) -> int:
    line_splitted = [int(i) for i in line.split(',')]
    converted = [Value(ordering, i) for i in line_splitted]
    converted.sort()
    print(f"original: {line_splitted}")
    new_sorted_line = [i.val for i in converted]
    print(f"sorted: {new_sorted_line}")
    if line_splitted == new_sorted_line:
        return 0
    else:
        print(f"line has uncorrect ordering: {line_splitted}")
        middle_value = int(len(line_splitted) / 2)
        print(f"middle value is: {new_sorted_line[middle_value]}")
        return new_sorted_line[middle_value]


rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

test = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def run_test():
    ordering = Ordering(rules=list())

    for line in rules.splitlines():
        ordering.add_rule([int(i) for i in line.split('|')])

    result = 0

    for line in test.splitlines():
        result += check_line(line, ordering)

    print(f"final result: {result}")

def run():
    ordering = Ordering(rules = list())
    result = 0
    with open('day5_input.txt') as fd:
        for line in fd:
            line = line.strip()
            if not line:
                continue
            if "|" in line:
                ordering.add_rule([int(i) for i in line.split('|')])
            if "," in line:
                result += check_line(line, ordering)
    print(f"final result: {result}")

if __name__ == '__main__':
    run()
    #run_test()
