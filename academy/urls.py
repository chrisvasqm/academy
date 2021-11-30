from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('subjects', views.SubjectViewSet)
router.register('students', views.StudentViewSet)

urlpatterns = router.urls