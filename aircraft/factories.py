from aircraft.models import PassengerPlane, CargoPlane, RescuePlane, MedicalPlane


class AircraftFactory:
    """ the class informs that a different aircraft Subclass
    must implement create_aircraft()"""

    def create_aircraft(self):
        """function of creating aircraft."""
        raise NotImplementedError


class PassengerPlaneFactory(AircraftFactory):
    def create_aircraft(self):
        """create passenger plane."""
        return PassengerPlane()


class CargoPlaneFactory(AircraftFactory):
    def create_aircraft(self):
        """create cargo plane."""
        return CargoPlane()


class RescuePlaneFactory(AircraftFactory):
    def create_aircraft(self):
        """create rescue plane."""
        return RescuePlane()


class MedicalPlaneFactory(AircraftFactory):
    def create_aircraft(self):
        """create medical plane."""
        return MedicalPlane()
