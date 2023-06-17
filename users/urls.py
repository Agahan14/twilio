from django.urls import path
from .views import SendSMSView, BannerViewSet
from rest_framework.routers import DefaultRouter

users_router = DefaultRouter()

users_router.register(r'banner', BannerViewSet)


urlpatterns = [
    path('send-sms/', SendSMSView.as_view(), name='send_sms'),
]
