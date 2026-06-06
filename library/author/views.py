from .models import Author

def authors_list_view(request):
    authors = Author.objects.all()
    return render(request, 'author/authors_list.html', {'authors': authors})

def author_create_view(request):
    if not request.user.is_authenticated or request.user.role != 1:
        return redirect('login')

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')

        Author.objects.create(name=name, surname=surname, patronymic=patronymic)
        return redirect('authors_list')

    return render(request, 'author/author_form.html')

def author_delete_view(request, author_id):
    if not request.user.is_authenticated or request.user.role != 1:
        return redirect('login')

    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('authors_list')

    return render(request, 'author/author_confirm_delete.html', {'author': author})
