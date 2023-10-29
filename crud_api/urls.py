from django.urls import include,path
from rest_framework.routers import DefaultRouter

from crud_api.views import Categoryviewset,Brandviewset,Itemsviewset

router=DefaultRouter()
router.register(r'category',Categoryviewset)
router.register(r'brand',Brandviewset)
router.register(r'items',Itemsviewset)


urlpatterns =router.urls