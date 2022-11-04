class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class DatabaseConnector(Singleton):
    pass


if __name__ == '__main__':
    first_instance = DatabaseConnector()
    second_instance = DatabaseConnector()
    print(id(first_instance), id(second_instance))
