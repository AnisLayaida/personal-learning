from datetime import date

class OnlineProduct:
    def __init__(self, price: float, delivery_time: date, shipping_fee: float, insurance_policy: bool, stock_quantity: int):
        self.price = price
        self.deliveryTime = delivery_time
        self.shippingFee = shipping_fee
        self.insurancePolicy = insurance_policy
        self.stockQuantity = stock_quantity

    def product_definitions(self):
        return (f"The price of the broadband plan: £{self.price}\n"
                f"Delivery Time: {self.deliveryTime}"
                f"Shipping Fee: {self.shippingFee}\n"
                f"Insurance Policy selected? {'Yes' if self.insurancePolicy else 'No'}\n"
                f"Stock Quantity: {self.stockQuantity}\n")

    def __str__(self):
        return "Find out more information about your Online Product!"

class Broadband(OnlineProduct):
    def __init__(self, price: float, delivery_time: date, shipping_fee: float, insurance_policy: bool, stock_quantity: int, speed_of_internet: int, internet_service_provider: str, cyber_secured_wifi_plan: bool, broadband_type: str):
        super().__init__(price, delivery_time, shipping_fee, insurance_policy, stock_quantity)
        self.speedOfInternet = speed_of_internet
        self.internetServiceProvider = internet_service_provider
        self.cyberSecuredWifiPlan = cyber_secured_wifi_plan
        self.broadbandType = broadband_type

    def product_definitions(self):
        return (f"Customer Facing Service:\n"
                f"Here is some information about your Broadband:\n"
                f"The price of the broadband plan: £{self.price}\n"
                f"The Speed of the broadband plan selected: {self.speedOfInternet} Mbps\n"
                f"The selected internet service provider: {self.internetServiceProvider}\n"
                f"Cyber Secured Wifi Plan selected? {'Yes' if self.cyberSecuredWifiPlan else 'No'}\n"
                f"Insurance Policy selected? {'Yes' if self.insurancePolicy else 'No'}\n"
                f"------------------------------------------------------------------------------\n"
                f"Resource Facing Service:\n"
                f"Delivery Time: {self.deliveryTime}"
                f"Shipping Fee: {self.shippingFee}\n"
                f"Broadband Type: {self.broadbandType}\n"
                f"Stock Quantity: {self.stockQuantity}\n")

    def __str__(self) -> str:
        return "Find out more information about your Broadband!"


Skipping_Rope = OnlineProduct(10, date(2025, 4, 7), 14.99, False, 3)
EE = Broadband(30.0, date(2025, 9, 30), 15.99, True, 1, 100, "EE", True, "Family Broadband")

print(Skipping_Rope)
print(EE)
print(Skipping_Rope.product_definitions())
print(EE.product_definitions())