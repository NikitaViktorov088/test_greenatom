from ma import Parent


class Second:
    @property
    def isSecond(self) -> int:
        return 1


class B(Second, Parent):
    def __init__(self, value: int) -> None:
        self.value: int = value

    def fnc(self, num_1: int, num_2: int) -> int:
        return num_1 * num_2 * self.value

    def isFirst(self) -> int:
        return 0
