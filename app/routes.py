from app import api
from app.resources import HelloWorld, CardVault, Payment


api.add_resource(HelloWorld, '/')
api.add_resource(CardVault, '/tokenize/')
api.add_resource(Payment, '/sale/')
