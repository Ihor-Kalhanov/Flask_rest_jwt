# from datetime import datetime
#
# from flask_jwt_extended import decode_token
# from sqlalchemy.orm.exc import NoResultFound
#
#
#
#
# def add_token_to_database(encoded_token, identity_claim):
#     """
#     Adds a new token to the database. It is not revoked when it is added.
#     :param identity_claim: configured key to get user identity
#     """
#     decoded_token = decode_token(encoded_token)
#     jti = decoded_token["jti"]
#     token_type = decoded_token["type"]
#     user_identity = decoded_token[identity_claim]
#     expires = datetime.fromtimestamp(decoded_token["exp"])
#     revoked = False
#
#     db_token = TokenBlocklist(
#         jti=jti,
#         token_type=token_type,
#         user_id=user_identity,
#         expires=expires,
#         revoked=revoked,
#     )
#     db.session.add(db_token)
#     db.session.commit()
#
#
#
#
