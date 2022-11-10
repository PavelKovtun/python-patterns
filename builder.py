from abc import ABC, abstractmethod
import enum


class SubwaySandwich:
    def __init__(self):
        self.bread = None
        self.filling = []
        self.sauce = None


class Breads(enum.Enum):
    WHEATEN = 1,
    RYE = 2,
    GARLIC = 3
    NON_GLUTEN_BREAD = 4


class Fillings(enum.Enum):
    SALAD = 1,
    CUCUMBER = 2,
    OLIVES = 3,
    CHICKEN = 4,
    TOMATO = 5,
    PEPPER = 6,
    CHEESE = 7,
    BACON = 8


class Sauces(enum.Enum):
    SPICY = 1,
    KETCHUP = 2,
    MAYONNAISE = 3,
    GARLIC = 4


class SandwichBuilder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_bread(self):
        pass

    @abstractmethod
    def add_bread_without_gluten(self):
        pass

    @abstractmethod
    def add_meat_filling(self):
        pass

    @abstractmethod
    def add_vegetable_filling(self):
        pass


class SubwayMeltBuilder(SandwichBuilder):
    def __init__(self):
        self.sandwich = SubwaySandwich()

    @property
    def product(self) -> SubwaySandwich:
        return self.sandwich

    def add_bread(self):
        self.sandwich.bread = Breads.GARLIC

    def add_bread_without_gluten(self):
        self.sandwich.bread = Breads.NON_GLUTEN_BREAD

    def add_vegetable_filling(self):
        melt_vegetables = [Fillings.SALAD, Fillings.OLIVES, Fillings.PEPPER]
        for ingredient in melt_vegetables:
            self.sandwich.filling.append(ingredient)

    def add_meat_filling(self):
        melt_meat = [Fillings.CHICKEN, Fillings.BACON]
        for ingredient in melt_meat:
            self.sandwich.filling.append(ingredient)

    def add_sauce(self):
        self.sandwich.sauce = Sauces.SPICY


class Director:
    def __init__(self, builder: SandwichBuilder):
        self.builder = builder

    def create_sandwich(self) -> SubwaySandwich:
        self.builder.add_bread()
        self.builder.add_vegetable_filling()
        self.builder.add_meat_filling()
        self.builder.add_sauce()
        return self.builder.product

    def create_sandwich_without_gluten(self) -> SubwaySandwich:
        self.builder.add_bread_without_gluten()
        self.builder.add_vegetable_filling()
        self.builder.add_meat_filling()
        self.builder.add_sauce()
        return self.builder.product


if __name__ == '__main__':
    melt_recipe = SubwayMeltBuilder()
    director = Director(melt_recipe)
    subway_melt_without_gluten = director.create_sandwich()