from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseNotAllowed


def register(request):
    """新しいユーザーを登録する"""
    if request.method != 'POST':
        # 空のユーザー登録フォームを表示する
        form = UserCreationForm()
    else:
        # 入力済みのフォームを処理する
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # ユーザーをログインさせてホームページにリダイレクトする
            login(request, new_user)
            return redirect('learning_logs:index')

    # 空または無効なフォームを表示する
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def logout_view(request):
    """ユーザーをログアウトする"""
    if request.method == 'POST':
        logout(request)
        return redirect('learning_logs:logged_out')
    else:
        # 許可されていないメソッドへの応答
        return HttpResponseNotAllowed(['POST']) 