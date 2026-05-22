from django.shortcuts import render
from .models import Category, Product


def main_view(request):
    # Дістаємо всі категорії та всі продукти з бази даних
    categories = Category.objects.all()
    products = Product.objects.all()

    # Перевіряємо, чи користувач обрав якусь конкретну категорію через меню
    category_id = request.GET.get('category')
    selected_category = None

    if category_id:
        products = products.filter(category_id=category_id)
        selected_category = Category.objects.filter(id=category_id).first()

    context = {
        'title': 'Sweet Symphony | Головна',
        'heading': selected_category.name if selected_category else 'Наше меню солодощів',
        'text': 'Оберіть категорію в меню вище, щоб відфільтрувати товари.',
        'categories': categories,
        'products': products,
        'is_main': True
    }
    return render(request, 'page.html', context)


def about_view(request):
    # Передаємо категорії навіть на інші сторінки, щоб хедер всюди працював однаково
    categories = Category.objects.all()
    context = {
        'title': 'Про нас',
        'heading': 'Про наш проєкт',
        'text': 'Тут знаходиться інформація про автора або опис лабораторної роботи.',
        'categories': categories,
        'is_main': False
    }
    return render(request, 'page.html', context)


def contacts_view(request):
    categories = Category.objects.all()
    context = {
        'title': 'Контакти',
        'heading': 'Наші контакти',
        'text': 'Зв\'язатися з нами можна через робочий email або Telegram.',
        'categories': categories,
        'is_main': False
    }
    return render(request, 'page.html', context)