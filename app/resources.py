from flask_restful import Resource
from app.models import User, Vault
from flask import request, Response
import json, uuid
from app.repositories.cardRepository import CardRepo
from app import db


def get_user_from_token(token):
    return User.query.filter_by(token=token).first()


class HelloWorld(Resource):
    def get(self):
        user = User.query.all()
        print(user)
        return {'hello': 'world'}

class CardVault(Resource):
    def get(self):
        print(request.headers)
        return {"hi": "guys"}

    def post(self):
        data = request.get_json()
        
        # Fetch user token based on header
        if request.headers['X-Merchant-ID']:
            user = get_user_from_token(request.headers['X-Merchant-ID'])
        else:
            return Response({
                "status": "unauthenticated"
            }, status=400)
            
        card = {
            'card_number': data['card_number'],
            'cvv': data['cvv'],
            'expiry': data['expiry']
        }
        # JSONIFY card details
        card = json.dumps(card)
        card_repo = CardRepo()
        last_four = data['card_number'][:4]
        encrypted_card = card_repo.create_token(user, card)
        card_uuid = uuid.uuid4().hex
        vault = Vault(last_four=last_four, card_token=encrypted_card, user_id=user.id, uuid=card_uuid)
        db.session.add(vault)
        db.session.commit()
        
        return {
            "status": "success",
            "token": vault.uuid
        }

class Payment(Resource):
    def post(self):
        if request.headers['X-Merchant-ID']:
            user = get_user_from_token(request.headers['X-Merchant-ID'])
        else:
            return Response({
                "status": "unauthenticated"
            }, status=400)
        
        data = request.get_json()
        card_repo = CardRepo('stripe')
        response = card_repo.pay(data, user)
        return response
