from datetime import timedelta

from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Order
from book.models import Book


def orders_list(request):

    orders = Order.objects.all()

    return render(
        request,
        "order/list.html",
        {"orders": orders}
    )


def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    )

    return render(
        request,
        "order/my_orders.html",
        {"orders": orders}
    )


def create_order(request, book_id):

    if request.method == "POST":

        book = Book.get_by_id(book_id)

        planned_date = (
            timezone.now() +
            timedelta(days=14)
        )

        Order.create(
            user=request.user,
            book=book,
            plated_end_at=planned_date
        )

        return redirect("my_orders")

    return redirect("books_list")


def close_order(request, id):

    order = Order.get_by_id(id)

    if order:

        order.update(
            end_at=timezone.now()
        )

        order.book.count += 1
        order.book.save()

    return redirect("orders_list")
