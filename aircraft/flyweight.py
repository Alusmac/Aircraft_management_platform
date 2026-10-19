class AircraftModel:
    """Store shared aircraft model information."""

    def __init__(self, manufacturer: str, model: str, engine_type: str, ) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.engine_type = engine_type


class AircraftModelFactory:
    """Create and reuse shared aircraft models."""

    def __init__(self) -> None:
        self._models: dict[tuple[str, str, str], AircraftModel] = {}

    def get_model(self, manufacturer: str, model: str, engine_type: str, ) -> AircraftModel:
        key = (manufacturer, model, engine_type)

        if key not in self._models:
            self._models[key] = AircraftModel(manufacturer, model, engine_type, )

        return self._models[key]


class Aircraft:
    """Represent an individual aircraft in the fleet."""

    def __init__(self, registration: str, status: str, flight_hours: int, model: AircraftModel, ) -> None:
        self.registration = registration
        self.status = status
        self.flight_hours = flight_hours
        self.model = model
