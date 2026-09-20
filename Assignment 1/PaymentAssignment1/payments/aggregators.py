from abc import ABC, abstractmethod

from payment_factories import RazorpayFactory, StripeFactory


class Aggregator(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def call_get_payment_object(self, method_type, amount, **kwargs):
        pass


class RazorpayAggregator(Aggregator):

    def __init__(self):
        super().__init__("Razorpay")
        self.processing_fee = 2.0

    def call_get_payment_object(self, method_type, amount, **kwargs):

        payment = RazorpayFactory.get_payment_object(
            method_type,
            **kwargs
        )

        return payment.pay(amount)


class StripeAggregator(Aggregator):

    def __init__(self):
        super().__init__("Stripe")
        self.processing_fee = 2.9

    def call_get_payment_object(self, method_type, amount, **kwargs):

        payment = StripeFactory.get_payment_object(
            method_type,
            **kwargs
        )

        return payment.pay(amount)