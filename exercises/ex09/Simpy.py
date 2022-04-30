"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730518639"


class Simpy:
    """Defining the Simpy class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize the values attribute."""
        self.values = values
    
    def __str__(self) -> str:
        """Automagically called."""
        return f"Simpy({self.values})"
    
    def fill(self, filling_values: float, n: int) -> None:
        """Fills values n number of times."""
        i = 0
        self.values = []
        while i < n:
            self.values.append(filling_values)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in values attribute with range of values."""
        assert step != 0.0
        self.values = []
        while abs(start) < abs(stop):
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Computes and returns the sum of all items in the values attribute."""
        sum = 0.0
        for values in self.values:
            sum += values
        return sum

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Creates a new Simpy object, adds either two Simpy objects or Simpy and float."""
        result = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        elif isinstance(rhs, float):
            for item in self.values:
                result.values.append(item + rhs)
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds the ability to use the power operator."""
        result = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        elif isinstance(rhs, float):
            for item in self.values:
                result.values.append(item ** rhs)
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask or a list[bool] based on equality."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        elif isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask or a list[bool] based on greater than relationship."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        elif isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloads subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            i = 0
            result: Simpy = Simpy([])
            while i < len(self.values):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
            return result