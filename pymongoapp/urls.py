from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todoPymongo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('User/',views.UserApi),
    path('User/', views.Creation_Class.as_view()),
    #path('User/MC', views.Manipulation_Class.as_view()),
    path('User/<int:id>', views.Manipulation_Class.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)