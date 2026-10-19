class FlightCheckHandler:
    """Define a base handler for flight checks."""

    def __init__(self) -> None:
        self.next_handler = None

    def set_next(self, handler: "FlightCheckHandler", ) -> "FlightCheckHandler":
        """Set the next handler and return it."""
        self.next_handler = handler
        return handler

    def handle(self, aircraft: dict) -> str:
        """Pass the request to the next handler."""
        if self.next_handler is not None:
            return self.next_handler.handle(aircraft)

        return "All flight checks passed"


class TechnicalCheck(FlightCheckHandler):
    """Check whether the aircraft is technically ready."""

    def handle(self, aircraft: dict) -> str:
        if not aircraft["technical_ready"]:
            return "Rejected: technical check failed"

        if self.next_handler is not None:
            return self.next_handler.handle(aircraft)

        return "All flight checks passed"


class DocumentCheck(FlightCheckHandler):
    """Check whether aircraft documents are valid."""

    def handle(self, aircraft: dict) -> str:
        if not aircraft["documents_valid"]:
            return "Rejected: documents are invalid"

        if self.next_handler is not None:
            return self.next_handler.handle(aircraft)

        return "All flight checks passed"


class CrewCheck(FlightCheckHandler):
    """Check whether the required crew is available."""

    def handle(self, aircraft: dict) -> str:
        if not aircraft["crew_available"]:
            return "Rejected: crew is unavailable"

        if self.next_handler is not None:
            return self.next_handler.handle(aircraft)

        return "All flight checks passed"


class WeatherCheck(FlightCheckHandler):
    """Check whether weather conditions are suitable."""

    def handle(self, aircraft: dict) -> str:
        if not aircraft["weather_suitable"]:
            return "Rejected: weather conditions are unsuitable"

        if self.next_handler is not None:
            return self.next_handler.handle(aircraft)

        return "All flight checks passed"
