class Flower:
    is_happy=False
    def __init__(self,name,water_requirments):
        self.water_requirements=water_requirments
        self.name=name

    def water(self,quantity):
        if quantity>=self.water_requirements:
            self.is_happy=True

    def status(self):
        if self.is_happy:
            return format(f'{self.name} is happy')
        else:
            return format(f'{self.name} is not happy')

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())