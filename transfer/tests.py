from django.test import TestCase
from accounts.models import Account
from decimal import Decimal


class TransferAmountValidationTest(TestCase):

    def setUp(self):
        self.sender = Account.objects.create_user(
            username='sender', password='pass123', email='sender@test.com', balance=Decimal('200.00')
        )
        self.recipient = Account.objects.create_user(
            username='recipient', password='pass123', email='recipient@test.com', balance=Decimal('100.00')
        )
        self.client.login(username='sender', password='pass123')

class IfAuthorizedTest(TestCase):
    def transfer_requires_authorizateion(self):
        response = self.client.get(reverse('transfers:transfer'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:login'))


