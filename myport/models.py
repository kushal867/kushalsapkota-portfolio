from django.db import models
from django.utils.text import slugify


#Profile /About
class Profile(models.Model):
    full_name = models.CharField(max_length=150)
    title = models.CharField(max_length=200, help_text="e.g. Full-Stack Developer | AI Enthusiast")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    resume = models.FileField(upload_to="resume/", blank=True, null=True)

    def __str__(self):
        return self.full_name


class SocialLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="social_links")
    platform = models.CharField(max_length=50)  # e.g. GitHub, LinkedIn
    url = models.URLField()

    def __str__(self):
        return f"{self.platform} ({self.profile.full_name})"


#Skills 
class SkillCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=70, help_text="Percentage skill level (0-100)")

    def __str__(self):
        return f"{self.name} ({self.level}%)"


# Projects
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="projects")
    description = models.TextField()
    short_description = models.CharField(max_length=250, blank=True)
    cover_image = models.ImageField(upload_to="projects/covers/")
    link_demo = models.URLField(blank=True, null=True)
    link_github = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="projects/gallery/")
    caption = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"


# Testimonials 
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)  # e.g. CEO at Company
    feedback = models.TextField()
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.role}"


#contacts
class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.email}"
