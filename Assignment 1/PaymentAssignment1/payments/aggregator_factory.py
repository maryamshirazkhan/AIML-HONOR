from aggregators import RazorpayAggregator, StripeAggregator


class AggregatorFactory:

    factory = {
        "stripe": StripeAggregator,
        "razorpay": RazorpayAggregator
    }

    @classmethod
    def get_aggregator_object(cls, aggregator_name):

        if aggregator_name not in cls.factory:
            raise ValueError("Invalid payment gateway.")

        return cls.factory[aggregator_name]()