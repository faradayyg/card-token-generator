from Crypto.Cipher import AES
import base64, hashlib, json
from app.services import payment
from app.models import Vault

class CardRepo:
    gateway = 'briantree'
    available_gateways = ['stripe', 'briantree']

    def __init__(self, gateway = None):
        if gateway is not None and gateway in self.available_gateways:
            self.gateway = gateway

    def create_token(self, user, card_number):
        md5Key = hashlib.md5(user.encryption_key.encode("utf-8")).digest()
        md5Key = md5Key+md5Key[0:16]

        blockSize = 16
        padDiff = blockSize - len(card_number) % blockSize
        padding = chr(padDiff)*padDiff
        card_number += padding
        cipher = AES.new(md5Key, AES.MODE_CBC, user.iv_string)
        ciphertext = base64.b64encode(cipher.encrypt(card_number)).decode('utf-8')
        return ciphertext

    def decode_token(self, user, token):
        md5Key = hashlib.md5(user.encryption_key.encode("utf-8")).digest()
        md5Key = md5Key+md5Key[0:16]

        cipher = AES.new(md5Key, AES.MODE_CBC, user.iv_string)

        decrypted = cipher.decrypt(base64.b64decode(token)).decode("utf-8")
        return decrypted[:decrypted.rfind('}')+1]

    def pay(self, data, user):
        methods = {
            'briantree': payment.Briantree(),
            'stripe': payment.Stripe()
        }
        vault = Vault.query.filter_by(user_id=user.id).filter_by(uuid=data['token']).first()
        data['card'] = json.loads(self.decode_token(user, vault.card_token))
        status = methods[self.gateway].pay(data)

        if status == True:
            return {"status": "success", "message": "charge successful"}
        elif status == False:
            return {"status": "error", "message": "charge failure"}, 500
