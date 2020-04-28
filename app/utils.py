# Parse response from payment gateway to match a standard output
def standardize_response(gateway, payload):
    if gateway == 'briantree':
        # do briantree things here
        pass

    elif gateway == 'stripe':
        if payload and payload.status == 'requires_action' and payload.next_action.type == 'use_stripe_sdk':
            return payload
        elif payload.status == 'succeeded':
            return True
        else:
            return False


def further_processing(gateway, data):
    # Process data according to gateway
    pass