class AircraftReport:
    """Define the template for generating aircraft reports."""

    def generate(self) -> str:
        """Run the report generation steps."""
        aircraft = self.get_aircraft()
        return self.format_report(aircraft)

    def get_aircraft(self) -> list[str]:
        """Return aircraft data."""
        return ["Boeing 737", "Airbus A320"]

    def format_report(self, aircraft: list[str]) -> str:
        """Format the aircraft data."""
        raise NotImplementedError


class TextReport(AircraftReport):
    """Generate a plain text report."""

    def format_report(self, aircraft: list[str]) -> str:
        return ", ".join(aircraft)


class CSVReport(AircraftReport):
    """Generate a CSV-style report."""

    def format_report(self, aircraft: list[str]) -> str:
        return "\n".join(aircraft)
