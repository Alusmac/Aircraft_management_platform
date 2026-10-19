class StateFlight:
    """Represent a flight with different states."""

    def __init__(self) -> None:
        self.status = "Scheduled"

    def board(self) -> str:
        """Start boarding if the flight is scheduled."""
        if self.status == "Scheduled":
            self.status = "Boarding"
            return "Boarding started"

        return "Boarding is not allowed"

    def take_off(self) -> str:
        """Start the flight if boarding is complete."""
        if self.status == "Boarding":
            self.status = "In Flight"
            return "Aircraft took off"

        return "Take-off is not allowed"
