class AircraftCatalog:
    """Define the aircraft catalog interface."""

    def get_aircraft(self, registration: str) -> str:
        raise NotImplementedError


class RemoteAircraftCatalog(AircraftCatalog):
    """Represent a remote aircraft catalog."""

    def get_aircraft(self, registration: str) -> str:
        print("Loading data from remote catalog...")
        return f"Aircraft data for {registration}"


class AircraftCatalogProxy(AircraftCatalog):
    """Cache results from the remote aircraft catalog."""

    def __init__(self, catalog: AircraftCatalog) -> None:
        self.catalog = catalog
        self.cache: dict[str, str] = {}

    def get_aircraft(self, registration: str) -> str:
        if registration not in self.cache:
            self.cache[registration] = (self.catalog.get_aircraft(registration))

        return self.cache[registration]
