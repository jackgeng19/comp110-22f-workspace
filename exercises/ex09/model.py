"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730433734"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, p1: Point) -> float:
        """Return the distance between two Points."""
        distance_x: float = self.x - p1.x
        distance_y: float = self.y - p1.y
        result: float = sqrt(distance_x ** 2 + distance_y ** 2)
        return result


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Reassign the object's location attribute the result of adding the self object's location with its direction."""
        self.location = self.location.add(self.direction)
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        if self.is_infected():
            self.sickness += 1
        

    # def color(self) -> str:
    #     """Return the color representation of a cell."""
    #     return "black"

    def contract_disease(self) -> None:
        """Assign the INFECTED constant to the sickness attribute of the Cell object."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Return True when the sickness attribute is equal to VULNERABLE and False otherwise."""
        return self.sickness == constants.VULNERABLE

    def is_infected(self) -> bool:
        """Return True when the sickness attribute is equal to INFECTED and False otherwise."""
        return self.sickness >= constants.INFECTED

    def color(self) -> str:
        """Return "gray" if the Cell is vulnerable, and red if the Cell is infected."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "green"
        else:
            return "black"

    def contact_with(self, another_cell: Cell) -> None:
        """If either of the Cell objects is infected and the other is vulnerable, then the other should become infected."""
        if self.is_infected() and another_cell.is_vulnerable():
            another_cell.contract_disease()
        elif another_cell.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(self) -> None:
        """Assign the constant IMMUNE to the sickness attribute of the Cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Return True when the Cell object's sickness attribute is equal to the IMMUNE constant."""
        return self.sickness == constants.IMMUNE


class Model:
    """The state of the simulation."""
    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immuned: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected >= cells or infected <= 0:
            raise ValueError("Cells infected must be less than total cell counts or cells infected can not less than or equal to 0!")
        if immuned >= cells or immuned < 0:
            raise ValueError("Cells immuned must be less than total cell counts or cells infected can not less than 0!")
        self.population = []
        for _ in range(cells - infected - immuned):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(infected):
            start_location_1: Point = self.random_location()
            start_direction_1: Point = self.random_direction(speed)
            cell_inf: Cell = Cell(start_location_1, start_direction_1)
            cell_inf.contract_disease()
            self.population.append(cell_inf)
        for _ in range(immuned):
            start_location_2: Point = self.random_location()
            start_direction_2: Point = self.random_direction(speed)
            cell_immuned: Cell = Cell(start_location_2, start_direction_2)
            cell_immuned.immunize()
            self.population.append(cell_immuned)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        result: bool = True
        for cell in self.population:
            if cell.is_infected():
                result = False
        return result

    def check_contacts(self) -> None:
        """If any distance between two Cells is less than the constant CELL_RADIUS, then call the Cell#contact_with method on one of the two Cell objects."""
        cell_list: list = self.population
        i: int = 0
        j: int = 1
        while i < len(cell_list):
            while j < len(cell_list):
                if cell_list[i].location.distance(cell_list[j].location) < constants.CELL_RADIUS:
                    cell_list[i].contact_with(cell_list[j])
                j += 1
            i += 1