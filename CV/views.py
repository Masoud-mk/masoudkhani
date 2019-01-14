from django.shortcuts import render
from .models import Skill, WorkExperience, Education, Info, Refrences, Portfilio, social_network


# Create your views here.
def index(request):
    Skills = Skill.objects.all()
    WorkExperiences = WorkExperience.objects.order_by('-diuration')
    Educations = Education.objects.order_by('-diuration')
    info = Info.objects.all()
    refrences = Refrences.objects.all()
    portfolio = Portfilio.objects.all()
    social_networks = social_network.objects.all()
    context = {'Skills': Skills, 'WorkExperience': WorkExperiences, 'Education': Educations, 'Info': info,
               'Refrences': refrences, 'Portfilio': portfolio, 'social_network': social_network}

    return render(request, 'CV/index.html', context)
