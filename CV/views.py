from django.shortcuts import render
from .models import Skill, WorkExperience, Education, Info


# Create your views here.
def index(request):
    Skills = Skill.objects.all()
    WorkExperiences = WorkExperience.objects.order_by('-diuration')
    Educations = Education.objects.order_by('-diuration')
    info = Info.objects.all()

    context = {'Skills': Skills, 'WorkExperience': WorkExperiences, 'Education': Educations, 'Info': info}

    return render(request, 'CV/index.html', context)
