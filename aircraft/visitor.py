class PassengerPlane:
    """Represent a passenger aircraft."""

    def accept(self, visitor) -> str:
        return visitor.visit_passenger_plane(self)


class CargoPlane:
    """Represent a cargo aircraft."""

    def accept(self, visitor) -> str:
        return visitor.visit_cargo_plane(self)


class MaintenanceCostVisitor:
    """Calculate maintenance costs for aircraft."""

    def visit_passenger_plane(self, plane: PassengerPlane) -> str:
        return f"Passenger plane maintenance: 5000 EUR"

    def visit_cargo_plane(self, plane: CargoPlane) -> str:
        return f"Cargo plane maintenance: 8000 EUR"
