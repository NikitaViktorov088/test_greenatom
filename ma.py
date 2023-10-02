class Parent:
    pass


class First:
    def isFirst(self) -> int:
        return 1


class A(First, Parent):
    def __init__(self) -> None:
        self.i: int = 3
        self._second: int = 0

    def fnc(self, num: int) -> int:
        if not isinstance(num, int):
            raise TypeError("Argument 'num' must be an integer")

        if num > 2:
            raise MyError()
        return num * num * self.i

    @property
    def isSecond(self) -> int:
        return self._second


class MyError(Exception):
    def __init__(self) -> None:
        self.message: str = "Error text"

    def __str__(self) -> str:
        return self.message
