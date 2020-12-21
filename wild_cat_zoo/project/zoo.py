from wild_cat_zoo.project.caretaker import Caretaker
from wild_cat_zoo.project.cheetah import Cheetah
from wild_cat_zoo.project.keeper import Keeper
from wild_cat_zoo.project.lion import Lion
from wild_cat_zoo.project.tiger import Tiger
from wild_cat_zoo.project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        price_needed = price + animal.get_needs()
        if price > self.__budget:
            return "Not enough budget"
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        # if self.__budget >= price and self.__animal_capacity > len(self.animals):
        #     self.animals.append(animal)
        #     self.__budget -= price
        #     return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        # if self.__budget < price:
        #     return "Not enough budget"
        # return "Not enough space for animal"


    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            workers = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(workers)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"


    def pay_workers(self):
        money_needed = sum([s.salary for s in self.workers])
        if self.__budget >= money_needed:
            self.__budget -= money_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_money_need = sum([a.get_needs() for a in self.animals])
        if animals_money_need > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= animals_money_need
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [l for l in self.animals if l.__class__.__name__ == 'Lion']
        tigers = [t for t in self.animals if t.__class__.__name__ == 'Tiger']
        cheetahs = [c for c in self.animals if c.__class__.__name__ == 'Cheetah']

        result = f'You have {len(self.animals)} animals\n'
        result += f'----- {len(lions)} Lions:\n'
        result += '\n'.join(l.__repr__() for l in lions) + "\n"
        result += f'----- {len(tigers)} Tigers:\n'
        result += '\n'.join(t.__repr__() for t in tigers) + "\n"
        result += f'----- {len(cheetahs)} Cheetahs:\n'
        result += '\n'.join(ch.__repr__() for ch in  cheetahs)
        return result


    def workers_status(self):
        keeperss = [k for k in self.workers if k.__class__.__name__ == 'Keeper']
        caretakers = [c for c in self.workers if c.__class__.__name__ == 'Caretaker']
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]
        result = f'You have {len(self.workers)} workers\n'
        result += f'----- {len(keeperss)} Keepers:\n'
        result += "\n".join(k.__repr__() for k in keeperss) + '\n'
        result += f'----- {len(caretakers)} Caretakers:\n'
        result += "\n".join(k.__repr__() for k in caretakers) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += "\n".join(k.__repr__() for k in vets)
        return result



zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
