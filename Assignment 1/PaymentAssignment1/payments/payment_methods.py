from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


class RazorpayCardPayment(PaymentMethod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return "Razorpay Card Payment"

    def pay(self, amount):
        print("\nProcessing Razorpay card payment...")
        print("Amount:", amount)
        print("Payment successful!")
        return True


class RazorpayUPIPayment(PaymentMethod):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return "Razorpay UPI Payment"

    def pay(self, amount):
        print("\nProcessing Razorpay UPI payment...")
        print("UPI ID:", self.upi_id)
        print("Amount:", amount)
        print("Payment successful!")
        return True


class StripeCardPayment(PaymentMethod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return "Stripe Card Payment"

    def pay(self, amount):
        print("\nProcessing Stripe card payment...")
        print("Amount:", amount)
        print("Payment successful!")
        return True


class StripeUPIPayment(PaymentMethod):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return "Stripe UPI Payment"

    def pay(self, amount):
        print("\nProcessing Stripe UPI payment...")
        print("UPI ID:", self.upi_id)
        print("Amount:", amount)
        print("Payment successful!")
        return True