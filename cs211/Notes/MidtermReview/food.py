"""Let's do food. Food is good."""


class Food(object):
    """Abstract base class"""
    def calories(self) -> int:
        """How many calories in the food, per portion"""
        raise NotImplementedError("Hey, you need to override this")


class AtomicFood(Food):
    def __init__(self, calories):
        self.calories_per_portion = calories

    def calories(self):
        return self.calories_per_portion


class ComposedFood(Food):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def calories(self):
        total = 0
        for food in self.ingredients:
            total += food.calories()
        return total


noodles = AtomicFood(100)
cheese = AtomicFood(150)
mac_n_cheese = ComposedFood([noodles, cheese])
dough = AtomicFood(45)
sauce = AtomicFood(50)
mac_n_cheese_pizza = ComposedFood([dough, sauce, cheese, mac_n_cheese])

print(mac_n_cheese_pizza.calories())
