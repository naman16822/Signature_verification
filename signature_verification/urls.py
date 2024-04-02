from django.contrib import admin
from django.urls import path, include
from verifier.views import upload_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('verifier.urls')),
    path('upload/', upload_view, name='upload'),  
]

