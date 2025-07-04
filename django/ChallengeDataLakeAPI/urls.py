from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()


urlpatterns = [
    path('api/github_repo/', views.github_repo_list, name='github_repo_list'),
    path('api/job_offer/', views.job_offer_list, name='job_offer_list'),
    path('api/remoteok_job/', views.remoteok_job_list, name='remoteok_job_list'),
    path('api/adzuna_job/', views.adzuna_job_list, name='adzuna_job_list'),
    path('api/database/', views.database_list, name='database_list'),
    path('api/platform/', views.platform_list, name='platform_list'),
    path('api/top_tech/', views.top_tech_list, name='top_tech_list'),
    path('api/web_framework/', views.web_framework_list, name='web_framework_list'),
    path('api/', include(router.urls)),
]