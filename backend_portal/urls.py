from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication_app.api.urls')),
    path('database/', include('service_management_db.api.urls')),
    path('auth', include('rest_framework.urls'))
] + staticfiles_urlpatterns()
