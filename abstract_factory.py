from abc import ABC, abstractmethod


class Controller(ABC):
    @abstractmethod
    def control(self, robot):
        pass


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


class ManRobotController(Controller):
    def control(self, robot: Robot):
        print(f'Robot Man {robot} is under control')


class WomanRobotController(Controller):
    def control(self, robot: Robot):
        print(f'Robot Woman {robot} is under control')


class RobotFactory(ABC):
    @abstractmethod
    def create_robot(self) -> Robot:
        pass

    @abstractmethod
    def create_controller(self) -> Controller:
        pass


class WomanRobotFactory(RobotFactory):
    def create_robot(self) -> RobotWoman:
        return RobotWoman()

    def create_controller(self) -> WomanRobotController:
        return WomanRobotController()


class ManRobotFactory(RobotFactory):
    def create_robot(self) -> RobotMan:
        return RobotMan()

    def create_controller(self) -> ManRobotController:
        return ManRobotController()


def create_and_control_robot(factory: RobotFactory):
    robot = factory.create_robot()
    robot_controller = factory.create_controller()
    robot.greet()
    robot_controller.control(robot)


if __name__ == '__main__':
    man_fabric = ManRobotFactory()
    woman_fabric = WomanRobotFactory()
    create_and_control_robot(man_fabric)
    create_and_control_robot(woman_fabric)
