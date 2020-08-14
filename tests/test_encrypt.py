import unittest
from pagofacil import encrypt


class PagoFacilTestCase(unittest.TestCase):
    @unittest.skip
    def test_encrypt_ok(self):
        payload = encrypt.PagoPayload()
        payload.account_id = 123
        payload.amount = 10000
        payload.currency = '$'
        payload.country = 'cl'
        payload.reference = 'foo'
        payload.url_callback = 'http://foo.bar/callback'
        payload.url_cancel = 'http://foo.bar/cancel'
        payload.url_complete = 'http://foo.bar/complete'
        secret = '123'

        actual = encrypt.generate_encrypt(payload, secret)
        expected = 'b30db7a5abdd84a7dfb9559cdc81e90a70ae45a5029ccbb7cf378e26b4cb8dfb'
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
