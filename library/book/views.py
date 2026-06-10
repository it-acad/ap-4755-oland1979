from django.shortcuts import render
from django.db.models import Q

from .models import Book
from order.models import Order


def books_list(request):
    books = Book.objects.all()

    title = request.GET.get("title")
    author = request.GET.get("author")

    if title:
        books = books.filter(
            name__icontains=title
        )

    if author:

        words = author.split()
        author_filter = Q()


        for word in words:
            author_filter &= (Q(authors__name__icontains=word) | Q(authors__surname__icontains=word))


        books = books.filter(author_filter).distinct()



    return render(
        request,
        "book/list.html",
        {"books": books}
    )


def book_detail(request, id):
    book = Book.get_by_id(id)

    return render(
        request,
        "book/detail.html",
        {"book": book}
    )


def user_books(request, user_id):
    orders = Order.objects.filter(
        user_id=user_id,
        end_at=None
    )

    books = [order.book for order in orders]

    return render(
        request,
        "book/user_books.html",
        {"books": books}
    )