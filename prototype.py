import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class A(Prototype):
    def __init__(self):
        self.value = 1

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    a = A()
    b = a.clone()
    a.value = 3
    print(b.value)  # 1
