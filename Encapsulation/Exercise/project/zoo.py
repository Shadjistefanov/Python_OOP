class Zoo:
    def __init__(self,name,budget, animal_capacity, workers_capacity):
            self.__animal_capacity = animal_capacity
            self.__workers_capacity = workers_capacity
            self.__budget = budget
            self.name = name
            self.animals = []
            self.workers = []

    def add_animal(self,animal, price):
        if self.__budget>=price and len(self.animals)<self.__animal_capacity:
            self.animals.append(animal)
            self.__budget-=price
            type_animal=type(animal).__name__
            return f"{animal.name} the {type_animal} added to the zoo"
        elif self.__budget<price and len(self.animals)<self.__animal_capacity:
            return "Not enough budget"
        else:
            return f"Not enough space for animal"

    def hire_worker(self,worker):
        if len(self.workers)<self.__workers_capacity:
            self.workers.append(worker)
            type_worker = type(worker).__name__
            return f"{worker.name} the {type_worker} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self,worker_name):
        for worker in self.workers:
            if worker.name==worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries=sum([worker.salary for worker in self.workers])
        if salaries<=self.__budget:
            self.__budget-=salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending_cost=sum([animal.get_needs() for animal in self.animals])
        if tending_cost<=self.__budget:
            self.__budget-=tending_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self,amount):
        self.__budget+=amount

    def animals_status(self):
        lions=[]
        tigers=[]
        cheetahs=[]
        for animal in self.animals:
            if type(animal).__name__=='Cheetah':
                cheetahs.append(animal)
            elif type(animal).__name__=='Lion':
                lions.append(animal)
            elif type(animal).__name__ == 'Tiger':
                tigers.append(animal)
        output=f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n"
        for lion in lions:
            output+=f"{lion}\n"
        output+=f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            output+=f"{tiger}\n"
        output += f"----- {len(tigers)} Cheetahs:\n"
        for cheetah in cheetahs:
            output += f"{cheetah}\n"
        return output[:-1]

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if type(worker).__name__ == 'Keeper':
                keepers.append(worker)
            elif type(worker).__name__ == 'Caretaker':
                caretakers.append(worker)
            elif type(worker).__name__ == 'Vet':
                vets.append(worker)
        output = f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            output += f"{keeper}\n"
        output += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            output += f"{caretaker}\n"
        output += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            output += f"{vet}\n"
            return output[:-1]



