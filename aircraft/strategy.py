class PassengerCapacityStrategy:
    """Select an aircraft based on passenger capacity."""

    def select(self, aircraft: list[dict]) -> str:
        suitable = [
            plane for plane in aircraft
            if plane["capacity"] >= 150
        ]
        return suitable[0]["model"]


class CargoCapacityStrategy:
    """Select an aircraft based on cargo capacity."""

    def select(self, aircraft: list[dict]) -> str:
        suitable = [
            plane for plane in aircraft
            if plane["cargo_capacity"] >= 10
        ]
        return suitable[0]["model"]


class AircraftSelector:
    """Select an aircraft using a chosen strategy."""

    def __init__(self, strategy) -> None:
        self.strategy = strategy

    def select_aircraft(self, aircraft: list[dict]) -> str:
        return self.strategy.select(aircraft)
