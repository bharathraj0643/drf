from django.urls import path , include
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('products' , views.ProductViewset)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', include(router.urls)),
]