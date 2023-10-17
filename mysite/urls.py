from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import os

if 'ADMIN_PANEL_URL' in os.environ:
    admin_panel_url = os.environ['ADMIN_PANEL_URL']
else:
    admin_panel_url = 'admin/'

urlpatterns = [
    path(admin_panel_url, admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
    path('courses/', include('courses.urls')),
    path('user/', include('users.urls')),
    path('blog/', include('blog.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
