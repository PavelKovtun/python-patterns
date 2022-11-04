import enum
from abc import ABC, abstractmethod


class RobotTypes(enum.Enum):
    MAN = 1
    WOMAN = 2


class Robot(ABC):
    @abstractmethod
    def greet(self):
        pass


class RobotMan(Robot):
    def greet(self):
        print('Hello, i am Robot Man')


class RobotWoman(Robot):
    def greet(self):
        print('Hello, i am Robot Woman')


class RobotSystem:
    @staticmethod
    def create_robot(robot_type: RobotTypes) -> Robot:
        match robot_type:
            case RobotTypes.MAN:
                return RobotMan()
            case RobotTypes.WOMAN:
                return RobotWoman()


if __name__ == '__main__':
    system = RobotSystem()
    robot_man = system.create_robot(RobotTypes.MAN)
    robot_woman = system.create_robot(RobotTypes.WOMAN)
    robot_man.greet()
    robot_woman.greet()
