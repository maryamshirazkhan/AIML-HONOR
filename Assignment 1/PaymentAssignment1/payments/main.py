from aggregator_factory import AggregatorFactory
def main():
    print("================================")
    print("      PAYMENT PROCESSING")
    print("================================")

    # Select payment gateway
    print("\nSelect Payment Gateway:")
    print("1. Stripe")
    print("2. Razorpay")

    gateway_choice = input("Enter your choice: ").strip()

    if gateway_choice == "1":
        gateway_name = "stripe"

    elif gateway_choice == "2":
        gateway_name = "razorpay"

    else:
        print("Invalid gateway choice.")
        return

    # Select payment method
    print("\nSelect Payment Method:")
    print("1. Card")
    print("2. UPI")

    method_choice = input("Enter your choice: ").strip()

    if method_choice == "1":
        method_type = "card"

    elif method_choice == "2":
        method_type = "upi"

    else:
        print("Invalid payment method choice.")
        return

    # Get payment details
    if method_type == "card":

        card_number = input("Enter card number: ").strip()

        if not card_number:
            print("Card number cannot be empty.")
            return

        payment_details = {
            "card_number": card_number
        }

    else:

        upi_id = input("Enter UPI ID: ").strip()

        if not upi_id:
            print("UPI ID cannot be empty.")
            return

        payment_details = {
            "upi_id": upi_id
        }

    # Get amount
    amount_input = input("Enter payment amount: ").strip()

    try:
        amount = float(amount_input)

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number for the amount.")
        return

    # Create the required aggregator using AggregatorFactory
    try:
        aggregator = AggregatorFactory.get_aggregator_object(
            gateway_name
        )

    except ValueError as error:
        print(error)
        return

    # Process payment
    try:
        result = aggregator.call_get_payment_object(
            method_type,
            amount,
            **payment_details
        )

        if result:
            print("\n================================")
            print("Transaction completed successfully.")
            print("================================")

        else:
            print("\nTransaction failed.")

    except ValueError as error:
        print("\nError:", error)
if __name__ == "__main__":
    main()