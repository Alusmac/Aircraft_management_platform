class Flight:
    """Represent a flight and notify observers about status changes."""

    def __init__(self) -> None:
        self.observers = []

    def subscribe(self, observer) -> None:
        """Subscribe an observer."""
        self.observers.append(observer)

    def change_status(self, status: str) -> None:
        """Change flight status and notify observers."""
        print(f"Flight status changed to: {status}")

        for observer in self.observers:
            observer.update(status)


class PassengerNotification:
    """Notify passengers about flight status changes."""

    def update(self, status: str) -> None:
        print(f"Passenger notification: {status}")


class FlightLogger:
    """Record flight status changes."""

    def update(self, status: str) -> None:
        print(f"Log: Flight status is {status}")
