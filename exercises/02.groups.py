
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f'unsupported operation')
        return Person(name=self.name, surname= other.surname)

    def __repr__(self):
        return self.name + ' ' + self.surname


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group("TODO", people=self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __str__(self):
        all_names = ', '.join(map(str, self.people))
        return f'Group {self.name} with members {all_names}'

    def __getitem__(self, item):
        return f'Person {item}: {self.people[item]}'


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group
#
# print(len(first_group))
# print(second_group)
# print(third_group[0])
#
# for person in third_group:
#     print(person)

import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("Stefan", "Hadjistefanov")

    def test_repr(self):
        result = repr(self.person_1)
        self.assertIn("Stefan", result)
        self.assertEqual(result, "Person 0: Stefan Hadjistefanov")