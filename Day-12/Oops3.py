#Problem 1
class CreditCardPayment:
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class PayPalPayment:
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")


def execute_payment(payment_object, amount):
    payment_object.process_payment(amount)


# Test
credit = CreditCardPayment()
paypal = PayPalPayment()

execute_payment(credit, 100)
execute_payment(paypal, 250)

#Problem 2
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("Car engine roaring to life!")


class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine revving!")


# Test
car = Car()
bike = Motorcycle()

car.start_engine()
bike.start_engine()

# Attempt to instantiate abstract class
vehicle = Vehicle()