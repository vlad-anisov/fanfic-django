from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('user/<name>/', user_profile, name='user_profile'), 
    path('user/<name>/edit', user_edit, name='user_edit'),
    path('fanfic/new/', fanfic_new, name='fanfic_new'),
    path('fanfic/<int:pk>/', fanfic, name='fanfic'),
    path('fanfic/<int:pk>/edit', fanfic_edit, name='fanfic_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)