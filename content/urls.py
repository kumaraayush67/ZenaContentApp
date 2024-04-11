from rest_framework import routers

from content import views

router = routers.SimpleRouter()
router.register(r'guidelines', views.GuidelineView)
router.register(r'content', views.ContentView)
router.register(r'guideline-check', views.GuidelineCheckView)


urlpatterns = router.urls
