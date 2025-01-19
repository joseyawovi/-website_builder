from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('business-details/', views.business_details, name='business_details'),
    path('template-selection/', views.template_selection, name='template_selection'),
    path('website-preview/', views.website_preview, name='website_preview'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
