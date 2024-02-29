from django.contrib import admin
from django.urls import path, include

admin.site.site_header='Microservice1-Admin'
admin.site.site_header = "Microservice1-Admin'"
admin.site.site_title = "MS1-Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]
