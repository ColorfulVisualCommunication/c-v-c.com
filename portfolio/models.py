from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=250)
    short_description = models.TextField(max_length=250, help_text='A brief summary of the project (max 250 characters)')
    description = models.TextField()
    technologies = models.CharField(max_length=250, help_text='Comma separated list of technologies used in the project(e.g. HTML, CSS, JavaScript)')
    image = models.ImageField(upload_to='portfolio_images/', null=True, blank=True)
    testemonial = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title