from aircraft.factories import (PassengerPlaneFactory, CargoPlaneFactory, RescuePlaneFactory, MedicalPlaneFactory, )
from aircraft.systems import (CivilianSystemsFactory, MilitarySystemsFactory, AirlineConfig, )
from aircraft.models import AircraftBuilder
from aircraft.offers import AdvertisingOffer
from integrations.payment_adapters import (FirstPaymentSDK, FirstPaymentAdapter, SecondPaymentSDK,
                                           SecondPaymentAdapter, )
from notifications.notifications import (EmailChannel, SMSChannel, PushChannel, OrderCreated, PaymentFailed, )


# ======== Factory Method
def launch_aircraft(factory):
    """function of launching aircraft."""
    aircraft = factory.create_aircraft()
    print(aircraft.fly())


def demonstrate_factory_method():
    """function of creating demonstrate aircraft."""
    print("\n=== FACTORY METHOD ===")

    launch_aircraft(PassengerPlaneFactory())
    launch_aircraft(CargoPlaneFactory())
    launch_aircraft(RescuePlaneFactory())
    launch_aircraft(MedicalPlaneFactory())


# ========  ABSTRACT FACTORY
def configure_aircraft(factory):
    """function of configuring aircraft."""
    navigation = factory.create_navigation()
    communication = factory.create_communication()

    print(navigation.get_info())
    print(communication.get_info())


def demonstrate_abstract_factory():
    """function of creating abstract aircraft."""
    print("\n=== ABSTRACT FACTORY ===")

    print("Civilian aircraft:")
    configure_aircraft(CivilianSystemsFactory())

    print("\nMilitary aircraft:")
    configure_aircraft(MilitarySystemsFactory())


# ========  BUILDER
def demonstrate_builder():
    """function of demonstrating builder."""
    print("\n=== BUILDER ===")

    aircraft = (
        AircraftBuilder()
        .set_engine("Jet Engine")
        .set_navigation("GPS")
        .set_communication("Satellite")
        .set_passenger_capacity(180)
        .build()
    )

    aircraft.show_configuration()


# ========  PROTOTYPE
def demonstrate_prototype():
    """function of demonstrating a prototype."""
    print("\n=== PROTOTYPE ===")

    template = AdvertisingOffer(
        "Spring Travel",
        "Kyiv - Paris",
        250,
        ["Baggage", "Meal"],
    )

    shallow_offer = template.clone_shallow()
    deep_offer = template.clone_deep()

    shallow_offer.services.append("Lounge access")
    deep_offer.services.append("Priority boarding")

    print("Original services:", template.services)
    print("Shallow copy services:", shallow_offer.services)
    print("Deep copy services:", deep_offer.services)


# ========  SINGLETON
def demonstrate_singleton():
    """ function of demonstrating singleton """
    print("\n=== SINGLETON ===")

    config1 = AirlineConfig()
    config2 = AirlineConfig()

    print("Same instance:", config1 is config2)
    print("Company:", config1.company_name)
    print("Currency:", config1.currency)

    config1.currency = "USD"

    print("Currency through config2:", config2.currency)

# ======== Adapter
def demonstrate_adapter():
    """ function of demonstrating Adapter. """
    print("\n=== ADAPTER ===")

    first_provider = FirstPaymentAdapter(FirstPaymentSDK())
    second_provider = SecondPaymentAdapter(SecondPaymentSDK())

    print(first_provider.pay(12.50, "EUR"))
    print(second_provider.pay(12.50, "EUR"))


def demonstrate_notifications() -> None:
    """function of demonstrating notifications."""
    print("\n=== NOTIFICATIONS ===")

    order_notification = OrderCreated(EmailChannel())
    order_notification.notify()

    payment_notification = PaymentFailed(SMSChannel())
    payment_notification.notify()

    another_notification = OrderCreated(PushChannel())
    another_notification.notify()


def main():
    demonstrate_factory_method()
    demonstrate_abstract_factory()
    demonstrate_builder()
    demonstrate_prototype()
    demonstrate_singleton()
    demonstrate_adapter()
    demonstrate_notifications()


if __name__ == "__main__":
    main()
