class PizzaDelivery:
    def __init__(self, name, price, ingredients):
            self.name = name
            self.price = price
            self.ingredients = ingredients

    ordered=False

    def add_extra(self,ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += ingredient_price*quantity

    def remove_ingredient(self,ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if self.ingredients[ingredient]<quantity:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient]-= quantity
        self.price-=ingredient_price*quantity

    def pizza_ordered(self):
        self.ordered=True
        output= f"You've ordered pizza {self.name} prepared with "
        output+=f"{self.ingredients}".replace("{","").replace("}","").replace("'","")
        output+=f" and the price will be {self.price}lv."
        return output

Margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
Margarita.add_extra('mozzarella', 1, 0.5)
Margarita.add_extra('cheese', 1, 1)
Margarita.remove_ingredient('cheese', 1, 1)
print(Margarita.remove_ingredient('bacon', 1, 2.5))
print(Margarita.remove_ingredient('tomatoes', 2, 0.5))
Margarita.remove_ingredient('cheese', 2, 1)
print(Margarita.pizza_ordered())
print(Margarita.add_extra('cheese', 1, 1))
