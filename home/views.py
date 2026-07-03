from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse

# 1. Ensure the index view is completely restored
def index(request):
    user = request.user
    return render(request, 'home/index.html', {'user': user})

# 2. Keep the original cards view
def cards(request):
    return render(request, 'home/index.html')

def card_detail(request, card_name):
    # Ruxsat etilgan kartalar ro'yxati
    VALID_CARD_TYPES = ['Visa', 'MasterCard', 'Humo', 'Uzcard']
    
    # Kiritilgan qiymatni ro'yxatdagilar bilan solishtirish (registrni hisobga olmaslik ham mumkin, masalan .title() bilan)
    # Biz aniq moslikni tekshiramiz:
    if card_name not in VALID_CARD_TYPES:
        raise Http404("Bunday turdagi karta mavjud emas!")

    context = {
        'card_name': card_name,
    }
    return render(request, 'home/card_detail.html', context)


def currency_view(request):
    # Valyuta ma'lumotlarini olish (bu yerda faqat misol uchun)
    currency_data = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.75,
        'JPY': 110.0,
        'UZS': 12600.0,
    }
    return render(request, 'home/currency.html', {'currency_data': currency_data})
