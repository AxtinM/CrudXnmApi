from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import StockView
router = DefaultRouter()
router.register('stock', StockView)
urlpatterns = [
    url(r'^', include(router.urls))
]