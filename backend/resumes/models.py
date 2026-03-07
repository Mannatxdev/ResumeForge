from django.db import models


class Resume(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="skills")
    category = models.CharField(max_length=100)
    items = models.TextField()

    def __str__(self):
        return self.category


class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Training(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="trainings")
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Certificate(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="certificates")
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="education")
    institute = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    score = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.institute