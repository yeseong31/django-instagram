import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from config.settings.base import JWT_SECRET_KEY


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """Generate Tokens"""

    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + six.text_type(timestamp)) + six.text_type(user.is_active)


account_activation_token = AccountActivationTokenGenerator()


def get_jwt_token():
    """JWT SECRET KEY 조회 및 확인"""
    jwt_key = JWT_SECRET_KEY
    if jwt_key is None:
        from config.settings.local import JWT_SECRET_KEY as JWT_SECRET_KEY_LOCAL
        jwt_key = JWT_SECRET_KEY_LOCAL
    return jwt_key
