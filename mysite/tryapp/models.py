from django.db import models

class TemplateInfo(models.Model):
    template_title = models.CharField(max_length=264)
    file = models.FileField()

    def __str__(self):
        return self.template_title

        
