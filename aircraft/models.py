class PassengerPlane:
    def fly(self) -> str:
        """function of flying passenger plane."""
        return "Passenger plane is flying"


class CargoPlane:
    def fly(self) -> str:
        """function of flying cargo plane."""
        return "Cargo plane is flying"


class RescuePlane:
    def fly(self) -> str:
        """function of flying rescue plane."""
        return "Rescue plane is flying"


class MedicalPlane:
    def fly(self) -> str:
        """function of flying medical plane."""
        return "Medical plane is flying"


class ConfigurableAircraft:
    def __init__(self) -> None:
        self.engine = None
        self.navigation = None
        self.communication = None
        self.passenger_capacity = None

    def show_configuration(self) -> None:
        """function of show configuration."""
        print(f"Engine: {self.engine}")
        print(f"Navigation: {self.navigation}")
        print(f"Communication: {self.communication}")
        print(f"Passenger capacity: {self.passenger_capacity}")


class AircraftBuilder:
    """Building Step ba Step"""

    def __init__(self) -> None:
        self.aircraft = ConfigurableAircraft()

    def set_engine(self, engine) -> AircraftBuilder:
        """engine is an instance of AircraftBuilder."""
        self.aircraft.engine = engine
        return self

    def set_navigation(self, navigation) -> AircraftBuilder:
        """navigation function."""
        self.aircraft.navigation = navigation
        return self

    def set_communication(self, communication) -> AircraftBuilder:
        """communication function """
        self.aircraft.communication = communication
        return self

    def set_passenger_capacity(self, passenger_capacity) -> AircraftBuilder:
        """ passenger_capacity """
        self.aircraft.passenger_capacity = passenger_capacity
        return self

    def build(self) -> ConfigurableAircraft:
        """Return the configured aircraft"""
        return self.aircraft
