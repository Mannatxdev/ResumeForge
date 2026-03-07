from rest_framework import viewsets
from .models import Resume, Skill, Project, Training, Certificate, Education
from .serializers import (
    ResumeSerializer,
    SkillSerializer,
    ProjectSerializer,
    TrainingSerializer,
    CertificateSerializer,
    EducationSerializer
)


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer



from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Resume, Skill, Project, Education


def download_resume(request, id):

    resume = Resume.objects.get(id=id)
    skills = Skill.objects.filter(resume=resume)
    projects = Project.objects.filter(resume=resume)
    education = Education.objects.filter(resume=resume)

    template = get_template("resume.html")

    html = template.render({
        "resume": resume,
        "skills": skills,
        "projects": projects,
        "education": education
    })

    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    pisa.CreatePDF(html, dest=response)

    return response