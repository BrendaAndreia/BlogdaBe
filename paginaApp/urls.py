from django.urls import path
from .views import home, contatos, sobre, posts, post_detail, post_list_by_tag

urlpatterns = [
    path('', home, name='home'),
    path('contatos', contatos, name='contatos'),
    path('sobre', sobre, name='sobre'),
    path('posts', posts, name='posts'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('posts/tag/<str:tag>/', post_list_by_tag, name='post_list_by_tag'),
]
