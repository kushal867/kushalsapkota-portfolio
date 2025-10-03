from django import forms
from .models import ContactMessage, Profile, Skill, Project, Testimonial


# -------- Contact Form (Public) --------
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your Email"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Subject"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Your Message"}),
        }


# -------- Profile Form (optional, for admin panel or frontend CMS) --------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["full_name", "title", "bio", "profile_image", "resume"]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }


# -------- Skill Form --------
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["category", "name", "level"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "level": forms.NumberInput(attrs={"class": "form-range", "min": "0", "max": "100"}),
        }


# -------- Project Form --------
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "category", "description", "short_description", "cover_image", "link_demo", "link_github", "featured"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "short_description": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "link_demo": forms.URLInput(attrs={"class": "form-control"}),
            "link_github": forms.URLInput(attrs={"class": "form-control"}),
        }


# -------- Testimonial Form --------
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ["name", "role", "feedback", "photo"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "role": forms.TextInput(attrs={"class": "form-control"}),
            "feedback": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
