from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy
from .models import Project, ContactMessage, Profile, SkillCategory, Testimonial, Category
from .forms import ContactForm

class HomeView(ListView):
    model = Project
    template_name = "portfolio/home.html"
    context_object_name = "projects"
    queryset = Project.objects.order_by("-featured", "-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        context["skill_categories"] = SkillCategory.objects.prefetch_related("skills").all()
        context["testimonials"] = Testimonial.objects.order_by("-created_at")[:6]
        context["categories"] = Category.objects.all()
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"
    context_object_name = "project"

class ContactView(FormView):
    template_name = "portfolio/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("portfolio:contact")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
