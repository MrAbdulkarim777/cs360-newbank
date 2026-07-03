from django.test import TestCase
from django.urls import reverse

class CardDetailTests(TestCase):

    def test_valid_card_types_return_200(self):
        """Ruxsat berilgan karta turlari 200 OK qaytarishi kerak"""
        valid_cards = ['Visa', 'MasterCard', 'Humo', 'Uzcard']
        for card in valid_cards:
            # urls.py dagi name='card_detail' ga argument berib chaqiramiz
            url = reverse('home:card_detail', args=[card])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_invalid_card_type_returns_404(self):
        """Tizimda yo'q karta turi (masalan, Azizbek) kiritilsa 404 qaytarishi kerak"""
        url = reverse('home:card_detail', args=['Azizbek'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

class CurrencyViewTDDTests(TestCase):


    def test_currency_view_contains_uzs(self):
        response = self.client.get('/currency/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('UZS', response.context['currency_data'])