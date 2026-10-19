class AircraftInspection:
    """Define the interface for aircraft inspections."""

    def inspect(self) -> str:
        raise NotImplementedError


class BasicInspection(AircraftInspection):
    """Perform a basic aircraft inspection."""

    def inspect(self) -> str:
        return "Basic aircraft inspection completed"


class InspectionDecorator(AircraftInspection):
    """Base decorator for additional inspections."""

    def __init__(self, inspection: AircraftInspection) -> None:
        self.inspection = inspection


class EngineInspection(InspectionDecorator):
    """Add an engine inspection."""

    def inspect(self) -> str:
        result = self.inspection.inspect()
        return result + ", engine inspection completed"


class AvionicsInspection(InspectionDecorator):
    """Add an avionics inspection."""

    def inspect(self) -> str:
        result = self.inspection.inspect()
        return result + ", avionics inspection completed"
