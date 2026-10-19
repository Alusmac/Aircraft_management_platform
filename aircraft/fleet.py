class FleetComponent:
    """Define a common interface for fleet components."""

    def count_aircraft(self) -> int:
        raise NotImplementedError

    def total_value(self) -> float:
        raise NotImplementedError


class AircraftUnit(FleetComponent):
    """Represent a single aircraft."""

    def __init__(self, model: str, value: float) -> None:
        self.model = model
        self.value = value

    def count_aircraft(self) -> int:
        return 1

    def total_value(self) -> float:
        return self.value


class AircraftFleet(FleetComponent):
    """Represent a group of aircraft or nested fleets."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.children: list[FleetComponent] = []

    def add(self, component: FleetComponent) -> None:
        self.children.append(component)

    def count_aircraft(self) -> int:
        return sum(
            child.count_aircraft()
            for child in self.children
        )

    def total_value(self) -> float:
        return sum(
            child.total_value()
            for child in self.children
        )
