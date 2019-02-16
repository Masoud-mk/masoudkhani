from django.shortcuts import render, redirect
from .models import Skill, WorkExperience, Education, Info, Refrences, Portfilio, social_network, ContactUS
from .forms import ContactUs
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
            contact = ContactUS(name=request.POST['name'], subject=request.POST['subject'], email=request.POST['email'],
                                message=request.POST['message'])
            messages.success(request, 'Tanks for Sending me An email I response as soon as possible')
            contact.save()
            return redirect('index')
        else:
            form = ContactUs()

    Skills = Skill.objects.all()
    WorkExperiences = WorkExperience.objects.order_by('-diuration')
    Educations = Education.objects.order_by('-diuration')
    info = Info.objects.all()
    refrences = Refrences.objects.all()
    portfolio = Portfilio.objects.all()
    social_networks = social_network.objects.all()
    contactUs = ContactUs()

    context = {'Skills': Skills, 'WorkExperience': WorkExperiences, 'Education': Educations, 'Info': info,
               'Refrences': refrences, 'Portfilio': portfolio, 'social_network': social_networks,
               'contactUs': contactUs}
    return render(request, 'CV/index.html', context)
