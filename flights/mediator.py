class PaymentService:
    """Handle flight payments."""

    def pay(self) -> str:
        return "Payment completed"


class MaintenanceService:
    """Check aircraft maintenance status."""

    def check(self) -> str:
        return "Aircraft is ready"


class NotificationService:
    """Send flight notifications."""

    def send(self, message: str) -> str:
        return f"Notification: {message}"


class FlightMediator:
    """Coordinate flight preparation services."""

    def __init__(self) -> None:
        self.payment = PaymentService()
        self.maintenance = MaintenanceService()
        self.notification = NotificationService()

    def prepare_flight(self) -> str:
        payment_result = self.payment.pay()
        maintenance_result = self.maintenance.check()

        self.notification.send("Flight preparation completed")

        return f"{payment_result}; {maintenance_result}"
