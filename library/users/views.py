from django.shortcuts import render, redirect
from authentication.models import CustomUser

def users_list_view(request):
    if not request.user.is_authenticated or request.user.role != 1:
        return redirect('login')
    users = CustomUser.get_all()
    return render(request, 'users/users_list.html', {'users': users})

def user_detail_view(request, user_id):
    if not request.user.is_authenticated or request.user.role != 1:
        return redirect('login')
    target_user = CustomUser.get_by_id(user_id)
    if not target_user:
        return render(request, 'users/404.html', status=404)
    return render(request, 'users/user_detail.html', {'target_user': target_user})