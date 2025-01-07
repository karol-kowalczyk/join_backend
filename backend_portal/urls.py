from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication_app.api.urls')),
    path('services/', include('service_management_db.api.urls')),
    path('auth', include('rest_framework.urls'))
]
