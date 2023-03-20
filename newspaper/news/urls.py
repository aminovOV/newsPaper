from django.urls import path
from .views import (
    NewsList, NewsDetail, SearchView, NewsCreate, NewsEdit, NewsDelete, ArticleCreate, ArticleEdit, ArticleDelete,
    CategoryListView, subscribe, unsubscribe, user_profile
)
from allauth.account.views import (
    LoginView, LogoutView
)


urlpatterns = [
    path('', NewsList.as_view(), name='news-list'),
    path('<int:pk>', NewsDetail.as_view(), name='news-detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('create/', NewsCreate.as_view(), name='news-create'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='news-edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news-delete'),
    path('article/create/', ArticleCreate.as_view(), name='article-create'),
    path('article/<int:pk>/edit/', ArticleEdit.as_view(), name='article-edit'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article-delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
    path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
    path('user-profile/', user_profile, name='user-profile'),
    path('accounts/login/', LoginView.as_view(), name='account-login'),
    path('accounts/logout/', LogoutView.as_view(), name='account-logout'),
]
