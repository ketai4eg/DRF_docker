from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from drf.views import UserViewSet, api_root, UserCreateViewSet, CategoriesViewSet, TransactionsViewSet, token_creation, docker_test
from rest_framework.authtoken.views import obtain_auth_token
from .yasg import urlpatterns as doc_urls

user_info = UserViewSet.as_view({
    'get': 'list',
    'put': 'update',
})

user_create = UserCreateViewSet.as_view({
    'post': 'create'
})

categories_list = CategoriesViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

category = CategoriesViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
})

transactions_list = TransactionsViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

transactions_details = TransactionsViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('user_info/', user_info, name='user-info'),
    path('user_create/', user_create, name='user-create'),
    path('categories/', categories_list, name='categories-list'),
    path('categories/<int:pk>/', category, name='category'),
    path('transactions/', transactions_list, name='transactions-list'),
    path('transactions/<int:pk>/', transactions_details, name='transactions-details'),
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('token_creation/', token_creation, name='token-creation'),
    path('docker_test/', docker_test, name='docker'),
])

urlpatterns += doc_urls