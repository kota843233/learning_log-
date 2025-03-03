"""users用URLパターンの定義"""
from django.urls import path, include

from .import views

app_name = "users"
urlpatterns = [
    # デフォルトの認証URL
    path('', include('django.contrib.auth.urls')),
    # ユーザー登録ページ
    path('register', views.register, name='register'),
    # ログアウトページ
    path('logout/', views.logout, name='logout'),   
]