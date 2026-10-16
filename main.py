from aircraft.factories import (PassengerPlaneFactory, CargoPlaneFactory, RescuePlaneFactory, MedicalPlaneFactory, )
from aircraft.systems import (CivilianSystemsFactory, MilitarySystemsFactory, AirlineConfig, )
from aircraft.models import AircraftBuilder
from aircraft.offers import AdvertisingOffer
from integrations.payment_adapters import (FirstPaymentSDK, FirstPaymentAdapter, SecondPaymentSDK,
                                           SecondPaymentAdapter, )
from notifications.notifications import (EmailChannel, SMSChannel, PushChannel, OrderCreated, PaymentFailed, )
from aircraft.fleet import AircraftUnit, AircraftFleet
from aircraft.decorators import BasicInspection, EngineInspection, AvionicsInspection
from flights.facade import FlightOperationsFacade
from aircraft.flyweight import Aircraft, AircraftModelFactory
from aircraft.proxy import RemoteAircraftCatalog, AircraftCatalogProxy


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


# ======= Composite
def demonstrate_composite() -> None:
    """function of demonstrating composite."""
    print("\n=== COMPOSITE ===")

    aircraft_fleet = AircraftFleet("Main Fleet")
    passenger_fleet = AircraftFleet("Passenger Fleet")
    cargo_fleet = AircraftFleet("Cargo Fleet")

    passenger_fleet.add(
        AircraftUnit("Boeing 737", 100_000_000)
    )
    passenger_fleet.add(
        AircraftUnit("Airbus A320", 110_000_000)
    )

    cargo_fleet.add(
        AircraftUnit("Boeing 777F", 150_000_000)
    )

    aircraft_fleet.add(passenger_fleet)
    aircraft_fleet.add(cargo_fleet)

    print("Aircraft count:", aircraft_fleet.count_aircraft())
    print("Fleet value:", aircraft_fleet.total_value())


# ====== Decorator
def demonstrate_decorator() -> None:
    """function of demonstrating decorator."""
    print("\n=== DECORATOR ===")

    inspection = BasicInspection()
    inspection = EngineInspection(inspection)
    inspection = AvionicsInspection(inspection)

    print(inspection.inspect())


# ======== Facade
def demonstrate_facade() -> None:
    """function of demonstrating facade."""
    print("\n=== FACADE ===")

    facade = FlightOperationsFacade()

    results = facade.prepare_flight(aircraft="Boeing 737", amount=1500.0, )

    for result in results:
        print(result)


# ====== Flyweight
def demonstrate_flyweight() -> None:
    """function of demonstrating flyweight."""
    print("\n=== FLYWEIGHT ===")

    factory = AircraftModelFactory()

    model_1 = factory.get_model(
        "Boeing",
        "737",
        "turbofan",
    )

    model_2 = factory.get_model(
        "Boeing",
        "737",
        "turbofan",
    )

    aircraft_1 = Aircraft(
        "N101AA", "Active", 1200, model_1
    )

    aircraft_2 = Aircraft(
        "N102AA", "Maintenance", 2400, model_2
    )

    print(aircraft_1.model is aircraft_2.model)
    print(aircraft_1.registration)
    print(aircraft_2.registration)
    print("Unique models:", len(factory._models))


# ====== Proxy
def demonstrate_proxy() -> None:
    """function of demonstrating proxy."""
    print("\n=== PROXY ===")

    remote_catalog = RemoteAircraftCatalog()
    catalog = AircraftCatalogProxy(remote_catalog)

    print(catalog.get_aircraft("N101AA"))
    print(catalog.get_aircraft("N101AA"))
    print(catalog.get_aircraft("N202BB"))


def main():
    demonstrate_factory_method()
    demonstrate_abstract_factory()
    demonstrate_builder()
    demonstrate_prototype()
    demonstrate_singleton()
    demonstrate_adapter()
    demonstrate_notifications()
    demonstrate_composite()
    demonstrate_decorator()
    demonstrate_facade()
    demonstrate_flyweight()
    demonstrate_proxy()


if __name__ == "__main__":
    main()
