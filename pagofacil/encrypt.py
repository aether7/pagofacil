import hmac
import hashlib
import codecs
from dataclasses import dataclass

@dataclass
class PagoPayload:
    account_id: str
    customer_email: str
    reference: str
    session_id: str
    url_cancel: str
    url_complete: str
    url_callback: str
    amount: float = 0
    country: str = 'CL'
    currency: str = 'CLP'


def generate_encrypt(payload: PagoPayload, secret: str) -> str:
    signature_str = _serialize_payload(payload)

    signature = hmac.new(
        codecs.encode(secret),
        msg=codecs.encode(signature_str),
        digestmod=hashlib.sha256
    )

    return signature.hexdigest()


def _serialize_payload(payload: PagoPayload):
    transaction_payload = {
        'x_account_id': payload.account_id,
        'x_amount': payload.amount,
        'x_currency': payload.currency,
        'x_customer_email': payload.customer_email,
        'x_reference': payload.reference,
        'x_session_id': payload.session_id,
        'x_shop_country': payload.country,
        'x_url_cancel': payload.url_cancel,
        'x_url_complete': payload.url_complete,
        'x_url_callback': payload.url_callback
    }
    message = ''

    for key in sorted(transaction_payload.keys()):
        message += '{}{}'.format(key, transaction_payload[key])

    return message
