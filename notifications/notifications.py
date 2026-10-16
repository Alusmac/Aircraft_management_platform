class EmailChannel:
    """Send notifications by email."""

    def send(self, message: str) -> None:
        print(f"Email: {message}")


class SMSChannel:
    """Send notifications by SMS."""

    def send(self, message: str) -> None:
        print(f"SMS: {message}")


class PushChannel:
    """Send notifications through push notifications."""

    def send(self, message: str) -> None:
        print(f"Push: {message}")


class Notification:
    """Represent a notification using a delivery channel."""

    def __init__(self, channel) -> None:
        self.channel = channel

    def notify(self) -> None:
        raise NotImplementedError


class OrderCreated(Notification):
    """Notify the user that an order was created."""

    def notify(self) -> None:
        self.channel.send("Your order has been created.")


class PaymentFailed(Notification):
    """Notify the user that a payment failed."""

    def notify(self) -> None:
        self.channel.send("Your payment has failed.")
