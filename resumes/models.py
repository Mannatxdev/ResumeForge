from django.db import models 
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)

class SkillCategory(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="skill_categories")
    category_name = models.CharField(max_length=100) 
    skills = models.TextField()  

class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    tech_stack = models.CharField(max_length=200)

class ProjectPoint(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="points")
    description = models.TextField()

class Training(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="trainings")
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

class Certificate(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="certificates")
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100)

class Achievement(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="achievements")
    description = models.TextField()

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="educations")
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    score = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=150)