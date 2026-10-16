class CivilianNavigation:
    def get_info(self) -> str:
        """navigation system info"""
        return "Civilian navigation system"


class MilitaryNavigation:
    def get_info(self) -> str:
        """getting military navigation system"""
        return "Military navigation system"


class CivilianCommunication:
    def get_info(self) -> str:
        """communication system info"""
        return "Civilian communication system"


class MilitaryCommunication:
    def get_info(self) -> str:
        """getting military communication system"""
        return "Military communication system"


class AircraftSystemsFactory:
    def create_navigation(self) -> CivilianNavigation:
        """create navigation system"""
        raise NotImplementedError

    def create_communication(self) -> CivilianCommunication:
        """create communication system"""
        raise NotImplementedError


class CivilianSystemsFactory(AircraftSystemsFactory):
    def create_navigation(self) -> CivilianNavigation:
        """create civilian navigation system"""
        return CivilianNavigation()

    def create_communication(self) -> CivilianCommunication:
        """create civilian communication system"""
        return CivilianCommunication()


class MilitarySystemsFactory(AircraftSystemsFactory):
    def create_navigation(self) -> MilitaryNavigation:
        """create military navigation system"""
        return MilitaryNavigation()

    def create_communication(self) -> MilitaryCommunication:
        """create military communication system"""
        return MilitaryCommunication()


class AirlineConfig:
    _instance = None

    def __new__(cls) -> "AirlineConfig":
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, "initialized"):
            self.company_name = "Sky Airlines"
            self.currency = "EUR"
            self.initialized = True
