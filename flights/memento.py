class MementoFlight:
    """Represent a flight and its status."""

    def __init__(self, status: str) -> None:
        self.status = status

    def save(self) -> str:
        """Save the current flight status."""
        return self.status

    def restore(self, saved_status: str) -> None:
        """Restore a previously saved flight status."""
        self.status = saved_status
