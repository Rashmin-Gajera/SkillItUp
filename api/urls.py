
from django.urls import path
from . import views

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'domains', views.DomainViewSet, basename='domains')
router.register(r'subdomains', views.SubDomainViewSet, basename='subdomains')
router.register(r'topics', views.TopicViewSet, basename='topics')
router.register(r'professions', views.ProfessionViewSet, basename='proffesions')
router.register(r'courses', views.CourseViewSet, basename='courses')
router.register(r'trendingtechs', views.TrendingTechViewSet, basename='trendingtechs')
router.register(r'trendingtools', views.TrendingToolViewSet, basename='trendingtechtools')
router.register(r'recommendationtest', views.RecommendationTestViewSet, basename='recommendationtest')
router.register(r'experts', views.ExpertViewSet, basename='expert')
router.register(r'searchexperts', views.SearchExpertViewSet, basename='searchexperts')
router.register(r'login', views.LoginViewSet, basename='login')
router.register(r'signup', views.SignUpViewSet, basename='signup')
urlpatterns = router.urls
