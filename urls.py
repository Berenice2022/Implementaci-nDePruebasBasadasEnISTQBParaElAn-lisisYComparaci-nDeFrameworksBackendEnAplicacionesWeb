from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from backend import views

from django.conf import settings
from django.contrib.staticfiles.urls import static 

router = routers.DefaultRouter()
#router.register('users', views.UserView, 'users')
router.register('register', views.UserView, 'register')
router.register('signin', views.UserView, 'signin')
router.register('users', views.UserView, 'users')
router.register('verify', views.UserView, 'verify')
router.register('users', views.UserView,'users')

router.register('posts', views.PostView, 'posts')
router.register('comments', views.CommentView, 'comments')
router.register('likes', views.LikeView, 'likes')
router.register('events', views.EventView, 'events')
router.register('interests', views.InterestView, 'interests')

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Backend API')),
    path('register/', views.register),
    path('signin/', views.signin),
    path('verify/', views.verify),
    path('users/', views.getUsers),
    path('users/', views.getUser),

    #path('snippets/', views.snippet_list),
    #path('snippets/<int:pk>/', views.snippet_detail),
    #path('register/',views.register, name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)