from django.shortcuts import render

def main_view(request):
    context = {
        'title': 'Головна',
        'heading': 'Ласкаво просимо на головну сторінку!',
        'text': 'Це контент головної сторінки, згенерований через контекст.',
        'is_main': True  # Прапорець, що це головна сторінка
    }
    return render(request, 'page.html', context)

def about_view(request):
    context = {
        'title': 'Про нас',
        'heading': 'Про наш проєкт',
        'text': 'Тут знаходиться інформація про автора або опис лабораторної роботи.',
        'is_main': False
    }
    return render(request, 'page.html', context)

def contacts_view(request):
    context = {
        'title': 'Контакти',
        'heading': 'Наші контакти',
        'text': 'Зв'язатися з нами можна через робочий email або Telegram.',
        'is_main': False
    }
    return render(request, 'page.html', context)