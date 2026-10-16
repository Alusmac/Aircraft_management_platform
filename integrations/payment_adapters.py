class InternalPaymentInterface:
    """Define the internal payment interface."""

    def pay(self, amount: float, currency: str) -> str:
        raise NotImplementedError


class FirstPaymentSDK:
    """Simulate a third-party payment SDK."""

    def execute_payment(self, total: float, currency_code: str, ) -> str:
        return f"Payment of {total} {currency_code} completed"


class FirstPaymentAdapter(InternalPaymentInterface):
    """Adapt the first payment SDK to the internal interface."""

    def __init__(self, sdk: FirstPaymentSDK) -> None:
        self.sdk = sdk

    def pay(self, amount: float, currency: str) -> str:
        return self.sdk.execute_payment(total=amount, currency_code=currency, )


class SecondPaymentSDK:
    """Simulate a second third-party payment SDK."""

    def make_transaction(self, amount_in_cents: int, currency: str) -> str:
        return (f"Transaction of {amount_in_cents} "f"cents in {currency} completed")


class SecondPaymentAdapter(InternalPaymentInterface):
    """Adapt the second payment SDK to the internal interface."""

    def __init__(self, sdk: SecondPaymentSDK) -> None:
        self.sdk = sdk

    def pay(self, amount: float, currency: str) -> str:
        amount_in_cents = round(amount * 100)

        return self.sdk.make_transaction(amount_in_cents=amount_in_cents, currency=currency, )
