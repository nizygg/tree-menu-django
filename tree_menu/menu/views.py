from django.shortcuts import render
from .models import MenuItem  # Импортируем вашу модель меню


def menu_view(request):
    menu_name = "main_menu"

    menu_items = MenuItem.objects.filter(name=menu_name).first()

    context = {
        "menu_items": menu_items,
    }

    return render(request, "index.html", context)
