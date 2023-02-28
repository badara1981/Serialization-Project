from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.urls import path, include

urlpatterns = [
    path('snippets/', views.SnippetsList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('usersList/', views.UsersList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('api-auth/', include('rest_framework.urls')),
]




urlpatterns = format_suffix_patterns(urlpatterns)