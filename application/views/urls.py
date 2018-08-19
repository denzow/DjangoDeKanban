from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.views.generic import TemplateView

from .accounts import signup as signup_view

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup_view.SignUpView.as_view(), name='signup'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# app routing to vue-router
urlpatterns += [re_path('.*', TemplateView.as_view(template_name='index.html'))]
