class AircraftIterator:
    """Iterate through aircraft one by one."""

    def __init__(self, aircraft: list[str]) -> None:
        self.aircraft = aircraft
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.index >= len(self.aircraft):
            raise StopIteration

        aircraft = self.aircraft[self.index]
        self.index += 1
        return aircraft


class AircraftCatalog:
    """Store aircraft and provide an iterator."""

    def __init__(self) -> None:
        self._aircraft = [
            "Boeing 737",
            "Airbus A320",
            "Boeing 777F",
        ]

    def __iter__(self):
        return AircraftIterator(self._aircraft)
