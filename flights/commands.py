class FlightPlan:
    """Manage the list of planned aircraft."""

    def __init__(self) -> None:
        self.aircraft: list[str] = []

    def add_aircraft(self, name: str) -> None:
        """Add an aircraft to the flight plan."""
        self.aircraft.append(name)

    def remove_aircraft(self, name: str) -> None:
        """Remove an aircraft from the flight plan."""
        self.aircraft.remove(name)


class Command:
    """Define the interface for flight plan commands."""

    def execute(self) -> None:
        raise NotImplementedError

    def undo(self) -> None:
        raise NotImplementedError

class AddAircraftCommand(Command):
    """Add an aircraft and support undo."""

    def __init__(
        self,
        flight_plan: FlightPlan,
        aircraft_name: str,
    ) -> None:
        self.flight_plan = flight_plan
        self.aircraft_name = aircraft_name

    def execute(self) -> None:
        self.flight_plan.add_aircraft(self.aircraft_name)

    def undo(self) -> None:
        self.flight_plan.remove_aircraft(self.aircraft_name)

class CommandManager:
    """Execute commands and maintain command history."""

    def __init__(self) -> None:
        self.history: list[Command] = []

    def execute(self, command: Command) -> None:
        command.execute()
        self.history.append(command)

    def undo_last(self) -> None:
        if self.history:
            command = self.history.pop()
            command.undo()
