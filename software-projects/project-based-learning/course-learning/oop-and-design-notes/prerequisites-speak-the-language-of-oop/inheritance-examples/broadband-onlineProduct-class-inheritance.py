from datetime import date

class OnlineProduct:
    def __init__(self, price: float, delivery_time: date, shipping_fee: float, insurance_policy: bool, stock_quantity: int):
        self.price = price
        self.deliveryTime = delivery_time
        self.shippingFee = shipping_fee
        self.insurancePolicy = insurance_policy
        self.stockQuantity = stock_quantity

class Broadband(OnlineProduct):
    def __init__(self, price: float, delivery_time: date, shipping_fee: float, insurance_policy: bool, stock_quantity: int, speed_of_internet: int, internet_service_provider: str, cyber_secured_wifi_plan: bool, broadband_type: str):
        super().__init__(price, delivery_time, shipping_fee, insurance_policy, stock_quantity)
        self.speedOfInternet = speed_of_internet
        self.internetServiceProvider = internet_service_provider
        self.cyberSecuredWifiPlan = cyber_secured_wifi_plan
        self.broadbandType = broadband_type

    def __str__(self) -> str:
        return (f"Broadband Plan -> Provider: {self.internetServiceProvider}, "
                f"Type: {self.broadbandType}, "
                f"Speed: {self.speedOfInternet} Mbps, "
                f"Price: £{self.price}, "
                f"Delivery Date: {self.deliveryTime}, "
                f"Shipping Fee: £{self.shippingFee}, "
                f"Insurance: {self.insurancePolicy}, "
                f"Stock: {self.stockQuantity}, "
                f"Cyber Secured Plan: {self.cyberSecuredWifiPlan}")

EE = Broadband(30.0, date(2025, 9, 30), 15.99, True, 1, 100, "EE", True, "Family Broadband")