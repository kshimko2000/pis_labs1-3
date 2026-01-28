from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Включаем URL-ы приложения articles
    path('', include('articles.urls')),
]