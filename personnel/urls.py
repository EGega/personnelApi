from .views import DepartmentView, PersonnelView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("departments", DepartmentView)
router.register("personnel", PersonnelView)

urlpatterns = [
 
]
urlpatterns += router.urls