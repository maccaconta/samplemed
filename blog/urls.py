
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import path, re_path
from django.conf.urls import include

urlpatterns = [
    path('', include('blog_app.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
