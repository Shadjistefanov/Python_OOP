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

import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person_one = Person("Stefan", "Hadjistefanov")

    def test_repr(self):
        result = repr(self.person_one)
        self.assertIn("Stefan", result)
        self.assertEqual(result, "Stefan Hadjistefanov")

    def test_custom_add(self):
        person_2 = Person("Test","Testov")
        person_3 = self.person_one + person_2
        self.assertEqual(person_3.name,"Stefan")
        self.assertEqual(person_3.surname, "Testov")

class TestGroup(unittest.TestCase):
    def setUp(self):
        self.group = Group("name", ["Stefan Hadjistefanov", "Test Testov"])

    def test_custom_len(self):

       # people = len(self.group[1])
        self.assertEqual(len(self.group), 2)

    def test_custom_add(self):
        group_two = Group("Ivo", ["Ivan Ivanov", "Ico Icov"])
        group_three = self.group + group_two
        self.assertEqual(len(group_three), 4)

    def test_get_item(self):
        result = self.group[1]
        self.assertIn('Test', result)
        self.assertEqual(result, "Person 1: Test Testov")

    def test_custom_geit_item_invalid_index(self):
        with self.assertRaises(IndexError):
            result = self.group[2]

if __name__ == '__main__':
    unittest.main()
