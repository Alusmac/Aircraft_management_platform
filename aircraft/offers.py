import copy


class AdvertisingOffer:
    def __init__(self, title, route, price, services) -> None:
        self.title = title
        self.route = route
        self.price = price
        self.services = services

    def clone_shallow(self) -> "AdvertisingOffer":
        """clone advertising offer"""
        return copy.copy(self)

    def clone_deep(self) -> "AdvertisingOffer":
        """clone deep advertising offer"""
        return copy.deepcopy(self)
