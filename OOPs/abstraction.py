from abc import ABC, abstractmethod


# The purpose of an abstract base class is to provide a common interface that other classes must implement.


class PaymentMethod(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def generate_receipt(self):
        pass


class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number, card_holder, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv

    def authenticate(self):
        print("Hello, authenticating your card.. please wait")
        if len(self.card_number) == 16 and len(self.cvv) == 3:
            print("Authentication Completed")
            print()
            return True
        else:
            print("Authentication Failed")
            return False

    def process_payment(self, amount):
        if self.authenticate():
            print("Processing Your Payment")
            print(f"Payment of {amount} made using credit card")
            return True
        print("Payment Failed")
        return False

    def generate_receipt(self):
        print("Generating receipt for credit card payment")
        print()
        return f"Receipt: Payment made using credit card ending with {self.card_number[-4:]}"


class UPI(PaymentMethod):
    def __init__(self, upi_id, pin):
        self.upi_id = upi_id
        self.pin = pin

    def authenticate(self):
        if 'bank' in self.upi_id:
            print("Its valid")
            return True
        print("Try Another")
        return False

    def process_payment(self, amount):
        if self.authenticate():
            print("Payment done")
            return True
        print("try again")
        return False

    def generate_receipt(self):
        print("here is your receipt")


# This class is designed to handle the processing of payments, regardless of the payment method used.
# This is where the design pattern of separating the payment logic from the payment processing logic comes into play
class PaymentProcessor:
    def processor(self, payment_method: PaymentMethod, amount):
        print("Initiating Payment Process...")
        print()
        if payment_method.process_payment(amount):
            receipt = payment_method.generate_receipt()
            print("Payment Processed Successfully")
            print(receipt)
        else:
            print("Payment Failed")


credit_card_payment = CreditCardPayment("1234567890123456", "Divu", "143")
payment_processor = PaymentProcessor()
payment_processor.processor(credit_card_payment, 150.0)

upi_id = UPI("abd@bank", 1234)
payment_processor.processor(upi_id, 160)
