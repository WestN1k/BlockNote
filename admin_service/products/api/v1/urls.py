from rest_framework.routers import DefaultRouter

from products.api.v1.views import ProductViewSet


router = DefaultRouter()

router.register('', ProductViewSet, 'product')

urlpatterns = router.urls
