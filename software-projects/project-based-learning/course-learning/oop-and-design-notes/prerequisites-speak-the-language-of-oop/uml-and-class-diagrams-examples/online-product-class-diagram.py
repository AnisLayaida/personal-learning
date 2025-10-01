from datetime import date

class OnlineProduct:
    def __init__(self, price: float, delivery_time: date, shipping_fee: float, insurance_policy: bool, stock_quantity: int):
        self.price = price
        self.deliveryTime = delivery_time
        self.shippingFee = shipping_fee
        self.insurancePolicy = insurance_policy
        self.stockQuantity = stock_quantity

    def __str__(self) -> str:
        return (f"OnlineProduct(price={self.price}, "
                f"delivery_time={self.deliveryTime}, "
                f"shipping_fee={self.shippingFee}, "
                f"insurance_policy={self.insurancePolicy}, "
                f"stock_quantity={self.stockQuantity})")

    def get_price(self)-> float:
        return self.price

    def set_price(self, price: float):
        self.price = price

    def get_delivery_time(self)-> date:
        return self.deliveryTime

    def set_delivery_time(self, delivery_time: date):
        self.deliveryTime = delivery_time

    def get_shipping_fee(self)-> float:
        return self.shippingFee

    def set_shipping_fee(self, shipping_fee: float):
        self.shippingFee = shipping_fee

    def get_insurance_policy(self) -> bool:
        return self.insurancePolicy

    def set_insurance_policy(self, insurance_policy: bool):
        self.insurancePolicy = insurance_policy

    def get_stock_quantity(self) -> int:
        return self.stockQuantity

    def set_stock_quantity(self, stock_quantity: int):
        self.stockQuantity = stock_quantity

iPhone = OnlineProduct(1999.99, date(2025, 12, 24), 29.99, True, 1)

print(iPhone)