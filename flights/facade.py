class FlightPlanner:
    """Handle flight planning."""

    def plan_flight(self, aircraft: str) -> str:
        return f"Flight planned for {aircraft}"


class MaintenanceService:
    """Check aircraft readiness."""

    def check_readiness(self, aircraft: str) -> str:
        return f"{aircraft} is ready for inspection approval"


class PaymentService:
    """Process payment for aviation services."""

    def process_payment(self, amount: float) -> str:
        return f"Payment of {amount} EUR completed"


class NotificationService:
    """Send flight operation notifications."""

    def send_notification(self, message: str) -> str:
        return f"Notification sent: {message}"


class FlightOperationsFacade:
    """Coordinate flight preparation services."""

    def __init__(self) -> None:
        self.planner = FlightPlanner()
        self.maintenance = MaintenanceService()
        self.payment = PaymentService()
        self.notifications = NotificationService()

    def prepare_flight(self, aircraft: str, amount: float, ) -> list[str]:
        results = []

        results.append(self.planner.plan_flight(aircraft))
        results.append(self.maintenance.check_readiness(aircraft))
        results.append(self.payment.process_payment(amount))
        results.append(self.notifications.send_notification(f"{aircraft} flight preparation completed"))

        return results
