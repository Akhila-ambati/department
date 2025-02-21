# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('departments/', include('departments.urls')),
# ]

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('departments/', include('departments.urls')),  # Departments app URLs
    path('', RedirectView.as_view(url='departments/')),  # Redirect root to departments
]

