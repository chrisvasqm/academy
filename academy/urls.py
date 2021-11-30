from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('subjects', views.SubjectViewSet)

urlpatterns = router.urls