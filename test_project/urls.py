from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),

    path('calc/', views.calc, name='calc'),
    path('test1/', views.calc, name='test1'),
    path('webhook/paid/', views.paid_webhook, name='paid_webhook'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
