import stripe

class Briantree:
    name = 'briantree'
    def pay(self, data):
        # Standardize response
        print("Payment from briantree", data)

class Stripe:
    name = 'stripe'
    charge = False
    def pay(self, data):
        # Standardize response
        stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
        parsed_card = {
                    "number": data['card']['card_number'],
                    "exp_month": int(data['card']['expiry'][:2]),
                    "exp_year": int(data['card']['expiry'][3:]),
                    "cvc": data['card']['cvv']
                }
        try:
            stripe_response = stripe.PaymentMethod.create(
                type="card",
                card=parsed_card
            )
        except stripe.error.InvalidRequestError as aa:
            print(aa)
            return False
        
        try:
            charge = stripe.PaymentIntent.create(
                payment_method = stripe_response.id,
                amount = data['amount'],
                currency = data['currency'],
                confirmation_method = 'manual',
                confirm = True,
            )
        except stripe.error.InvalidRequestError as aa:
            return False
        
        if charge and charge.status == 'requires_action' and charge.next_action.type == 'use_stripe_sdk':
            return charge
        elif charge.status == 'succeeded':
            return True
        else:
            return False