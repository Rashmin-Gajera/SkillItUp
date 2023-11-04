from django.contrib import admin

# Register your models here.
from skillitupcore.models import *

admin.site.site_header = 'SkillItUp Administrator'

admin.site.register(Domain)
admin.site.register(SubDomain)
admin.site.register(Topic)
admin.site.register(Profession)
admin.site.register(EducationalInstitute)
admin.site.register(Event)
admin.site.register(TrendingTech)
admin.site.register(TrendingTool)
admin.site.register(Course)
admin.site.register(RecommendationTest)
admin.site.register(Expert)
