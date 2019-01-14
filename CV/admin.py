from django.contrib import admin
from CV.models import Skill, WorkExperience, Education, Info, Refrences, Portfilio, social_network

# Register your models here.

admin.site.register(Skill)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Info)
admin.site.register(Refrences)
admin.site.register(Portfilio)
admin.site.register(social_network)
