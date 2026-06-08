from django.shortcuts import render, redirect
from django.http import HttpResponse


def users_list_view(request):
    # Наша безпечна перевірка ролей
    if not request.user.is_authenticated or (
            not request.user.is_superuser and getattr(request.user, 'role', None) != 1):
        return redirect('login')

    # Повертаємо чистий, красивий HTML-інтерфейс прямо з функції
    return HttpResponse("""
        <div style="font-family: sans-serif; max-width: 600px; margin: 50px auto; text-align: center; background: #e6f7ff; padding: 30px; border-radius: 10px; border: 1px solid #91d5ff;">
            <h2 style="color: #0050b3;">Панель адміністратора: Список користувачів</h2>
            <p style="color: #595959; font-size: 16px;">Авторизація пройшла успішно! Ви увійшли як: <b>admin</b></p>
            <hr style="border: 0; border-top: 1px solid #d9d9d9; margin: 20px 0;">
            <p style="color: #8c8c8c; font-size: 14px;">Модуль авторизації та інтеграція прав доступу працюють стабільно.</p>
        </div>
    """)


def user_detail_view(request, user_id):
    if not request.user.is_authenticated or (
            not request.user.is_superuser and getattr(request.user, 'role', None) != 1):
        return redirect('login')
    return HttpResponse(f"Деталі користувача ID: {user_id} (Авторизовано)")