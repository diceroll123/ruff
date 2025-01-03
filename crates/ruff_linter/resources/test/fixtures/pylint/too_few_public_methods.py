from __future__ import annotations

from dataclasses import dataclass


class Point:  # PLR0903
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Rectangle:  # OK
    def __init__(self, top_left: Point, bottom_right: Point) -> None:
        ...

    def area(self) -> float:
        ...


@dataclass
class Circle:  # OK
    center: Point
    radius: float

    def area(self) -> float:
        ...


class CustomException(Exception):  # OK
    ...


class A:
    class B:
        ...
    
    def __init__(self):
        ...

class C:
    c: int
    def __init__(self,d:list):...

class D:
    """This class has a docstring."""
    # this next method is an init
    def __init__(self,e:dict):...
