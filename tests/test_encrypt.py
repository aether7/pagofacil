import unittest
from pagofacil import encrypt


class SerializationTestCase(unittest.TestCase):
    def test_message_generated(self):
        payload = encrypt.PagoPayload(
            account_id=123,
            amount=10000,
            currency='CLP',
            country='CL',
            reference='foo',
            session_id='foostore',
            customer_email='john.doe@mailinator.com',
            url_callback='http://foo.bar/callback',
            url_cancel='http://foo.bar/cancel',
            url_complete='http://foo.bar/complete'
        )
        actual_message=encrypt._serialize_payload(payload)
        expected= ''.join([
            'x_account_id123',
            'x_amount10000',
            'x_currencyCLP',
            'x_customer_emailjohn.doe@mailinator.com',
            'x_referencefoo',
            'x_session_idfoostore',
            'x_shop_countryCL',
            'x_url_callbackhttp://foo.bar/callback',
            'x_url_cancelhttp://foo.bar/cancel',
            'x_url_completehttp://foo.bar/complete'
        ])
        self.assertEqual(actual_message, expected)


class PagoFacilTestCase(unittest.TestCase):
    def test_encrypt_ok(self):
        payload = encrypt.PagoPayload(
            account_id=123,
            amount=10000,
            currency='CLP',
            country='CL',
            reference='foo',
            session_id='foostore',
            customer_email='john.doe@mailinator.com',
            url_callback='http://foo.bar/callback',
            url_cancel='http://foo.bar/cancel',
            url_complete='http://foo.bar/complete'
        )
        secret = '123'
        actual = encrypt.generate_encrypt(payload, secret)
        expected = 'fdb0246e9e63665b2f9b791fffa433b18adee00a911f8c2dd17278e49e34f87c'
        self.assertEqual(actual, expected)

    def test_encrypt_fail(self):
        payload = encrypt.PagoPayload(
            account_id='foostore',
            amount=5000,
            customer_email='john.doe@mailinator.com',
            reference='reference',
            session_id='321fafa',
            url_cancel='http://another.url/cancel',
            url_complete='http://another.url/complete',
            url_callback='http://another.url/callback'
        )
        secret = 'secretpassword'
        actual = encrypt.generate_encrypt(payload, secret)
        expected = 'b30db7a5abdd84a7dfb9559cdc81e90a70ae45a5029ccbb7cf378e26b4cb8dfb'
        self.assertNotEqual(actual, expected)
