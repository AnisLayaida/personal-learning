from datetime import date

class OnlineProduct:
    def __init__(self, price: float, delivery_time: date, shipping_fee: float, insurance_policy: bool, stock_quantity: int):
        self.price = price
        self._deliveryTime = delivery_time
        self._shippingFee = shipping_fee
        self.__insurancePolicy = insurance_policy
        self.__stockQuantity = stock_quantity

    def get_delivery_time(self) -> date:
        return self._deliveryTime

    def set_delivery_time(self, delivery_time: date):
        self._deliveryTime = delivery_time

    def get_shipping_fee(self) -> float:
        return self._shippingFee

    def set_shipping_fee(self, shipping_fee: float):
        self._shippingFee = shipping_fee

    def get_insurance_policy(self) -> bool:
        return self.__insurancePolicy

    def set_insurance_policy(self, insurance_policy: bool):
        self.__insurancePolicy = insurance_policy

    def get_stock_quantity(self) -> int:
        return self.__stockQuantity

    def set_stock_quantity(self, stock_quantity: int):
        self.__stockQuantity = stock_quantity

    def product_definitions(self):
        return (f"The price of the broadband plan: £{self.price}\n"
                f"Delivery Time: {self.get_delivery_time()}"
                f"Shipping Fee: {self.get_shipping_fee()}\n"
                f"Insurance Policy selected? {'Yes' if self.get_insurance_policy() else 'No'}\n"
                f"Stock Quantity: {self.get_stock_quantity()}\n")

    def __str__(self):
        return "Find out more information about your Online Product!"

class Broadband(OnlineProduct):
    def __init__(self, price: float, delivery_time: date, shipping_fee: float, insurance_policy: bool, stock_quantity: int, speed_of_internet: int, internet_service_provider: str, cyber_secured_wifi_plan: bool, broadband_type: str):
        super().__init__(price, delivery_time, shipping_fee, insurance_policy, stock_quantity)
        self.speedOfInternet = speed_of_internet
        self._internetServiceProvider = internet_service_provider
        self.__cyberSecuredWifiPlan = cyber_secured_wifi_plan
        self.__broadbandType = broadband_type

    def get_internet_service_provider(self) -> str:
        return self._internetServiceProvider

    def set_internet_service_provider(self, internet_service_provider: str):
        self._internetServiceProvider = internet_service_provider

    def get_cyber_secured_wifi_plan(self) -> bool:
        return self.__cyberSecuredWifiPlan

    def set_cyber_secured_wifi_plan(self, cyber_secured_wifi_plan: bool):
        self.__cyberSecuredWifiPlan = cyber_secured_wifi_plan

    def get_broadband_type(self) -> str:
        return self.__broadbandType

    def set_broadband_type(self, broadband_type: str):
        self.__broadbandType = broadband_type

    def product_definitions(self):
        return (f"Customer Facing Service:\n"
                f"Here is some information about your Broadband:\n"
                f"The price of the broadband plan: £{self.price}\n"
                f"The Speed of the broadband plan selected: {self.speedOfInternet} Mbps\n"
                f"The selected internet service provider: {self.get_internet_service_provider()}\n"
                f"Cyber Secured Wifi Plan selected? {'Yes' if self.get_cyber_secured_wifi_plan() else 'No'}\n"
                f"Insurance Policy selected? {'Yes' if self.get_insurance_policy() else 'No'}\n"
                f"------------------------------------------------------------------------------\n"
                f"Resource Facing Service:\n"
                f"Delivery Time: {self.get_delivery_time()}"
                f"Shipping Fee: {self.get_shipping_fee()}\n"
                f"Broadband Type: {self.get_broadband_type()}\n"
                f"Stock Quantity: {self.get_stock_quantity()}\n")

    def __str__(self) -> str:
        return "Find out more information about your Broadband!"


Skipping_Rope = OnlineProduct(10, date(2025, 4, 7), 14.99, False, 3)
EE = Broadband(30.0, date(2025, 9, 30), 15.99, True, 1, 100, "EE", True, "Family Broadband")

print(Skipping_Rope)
print(EE)
print(Skipping_Rope.product_definitions())
print(EE.product_definitions())