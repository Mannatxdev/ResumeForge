from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import download_resume

from .views import (
    ResumeViewSet,
    SkillViewSet,
    ProjectViewSet,
    TrainingViewSet,
    CertificateViewSet,
    EducationViewSet
)

router = DefaultRouter()

router.register(r'resumes', ResumeViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'training', TrainingViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'education', EducationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('resume/<int:id>/download/', download_resume),
]