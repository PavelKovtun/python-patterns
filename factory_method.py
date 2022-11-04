from abc import ABC, abstractmethod


class Robot(ABC):
    @abstractmethod
    def greet(self):
        pass


class RobotMan(Robot):
    def greet(self):
        print(f'Hello, i am Robot Man {self}')


class RobotWoman(Robot):
    def greet(self):
        print(f'Hello, i am Robot Woman {self}')


class RobotFactory(ABC):
    @abstractmethod
    def create_robot(self) -> Robot:
        pass


class WomanRobotFactory(RobotFactory):
    def create_robot(self) -> RobotWoman:
        return RobotWoman()


class ManRobotFactory(RobotFactory):
    def create_robot(self) -> RobotMan:
        return RobotMan()


if __name__ == '__main__':
    man_fabric = ManRobotFactory()
    woman_fabric = WomanRobotFactory()
    man_robot = man_fabric.create_robot()
    woman_robot = woman_fabric.create_robot()
    man_robot.greet()
    woman_robot.greet()


