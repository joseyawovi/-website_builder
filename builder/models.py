from django.db import models

class BusinessDetails(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length=100)
    preview_image = models.ImageField(upload_to='template_previews/')
    html_file = models.FileField(upload_to='template_html/')

    def __str__(self):
        return self.name

class UserWebsite(models.Model):
    business_details = models.ForeignKey(BusinessDetails, on_delete=models.CASCADE)
    selected_template = models.ForeignKey(Template, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Website for {self.business_details.name} using {self.selected_template.name}"
