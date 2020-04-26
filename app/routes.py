from app import api
from app.resources import HelloWorld, CardVault, Payment


api.add_resource(HelloWorld, '/')
api.add_resource(CardVault, '/card/')
api.add_resource(Payment, '/pay/')
