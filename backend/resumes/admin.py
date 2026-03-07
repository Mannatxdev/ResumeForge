from django.contrib import admin
from .models import Resume, Skill, Project, Training, Certificate, Education

admin.site.register(Resume)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Training)
admin.site.register(Certificate)
admin.site.register(Education)
