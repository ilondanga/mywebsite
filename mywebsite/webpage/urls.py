from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('posts/<str:pk>',views.posts, name='posts'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('posts',views.posts, name='posts'),
    path('Contact_view',views.Contact_view,name='Contact_view')
]
