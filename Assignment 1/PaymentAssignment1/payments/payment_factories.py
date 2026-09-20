from abc import ABC

from payment_methods import (
    PaymentMethod,
    RazorpayCardPayment,
    RazorpayUPIPayment,
    StripeCardPayment,
    StripeUPIPayment
)


class FactoryPaymentMethod(ABC):

    factory = {}

    @classmethod
    def get_payment_object(cls, method_type, **kwargs):

        if method_type not in cls.factory:
            raise ValueError("Invalid payment method.")

        return cls.factory[method_type](**kwargs)


class RazorpayFactory(FactoryPaymentMethod):

    factory = {
        "card": RazorpayCardPayment,
        "upi": RazorpayUPIPayment
    }


class StripeFactory(FactoryPaymentMethod):

    factory = {
        "card": StripeCardPayment,
        "upi": StripeUPIPayment
    }