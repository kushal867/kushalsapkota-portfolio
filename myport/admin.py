from django.contrib import admin
from .models import Profile, SocialLink,SkillCategory, Skill,Category, Project, ProjectImage,Testimonial, ContactMessage

admin.site.register(Profile)
admin.site.register(SocialLink)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Testimonial)
admin.site.register(ContactMessage)