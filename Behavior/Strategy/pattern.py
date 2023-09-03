

class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} with Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} with PayPal")

class GooglePayPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} with Google Pay")


class ShoppingCart:
    def __init__(self, payment_strategy):
        self._payment_strategy = payment_strategy

    def checkout(self, total_amount):
        self._payment_strategy.pay(total_amount)

if __name__ == "__main__":
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    google_pay = GooglePayPayment()


    cart1 = ShoppingCart(credit_card)
    cart2 = ShoppingCart(paypal)
    cart3 = ShoppingCart(google_pay)


    cart1.checkout(100)
    cart2.checkout(200)
    cart3.checkout(150)
