class FuelRule:
    """Check whether an aircraft has enough fuel."""

    def interpret(self, fuel: int) -> bool:
        return fuel >= 5000