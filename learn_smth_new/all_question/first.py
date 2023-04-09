# проверка, я вляется ли класс хешируемым

import typing


class A:
    def __init__(self, id: int, name: str, l: list):
        self.id = id
        self.name = name
        self.li = l


a = A(1, "One", [1,2,3])

print(isinstance(a, typing.Hashable))

# да, всегда является