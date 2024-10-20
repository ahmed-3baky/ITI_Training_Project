from django.db import models
from django.shortcuts import reverse

class Projects(models.Model):
    name = models.CharField()
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    technology = models.CharField()
    thumbnail = models.ImageField(upload_to="product/images/", null=True)
    @property
    
    def get_absolute_url(self) :
        if 'http' in  self.thumbnail.url : 
            return self.thumbnail
        else : 
            return self.thumbnail.url
        
    def get_project_url(self):
        return reverse('project', kwargs={"project_id": self.id})

class Contacts(models.Model): 
    project = models.ForeignKey(Projects , related_name='contacts' , on_delete=models.CASCADE)
    name = models.CharField()
    email  = models.TextField()
    phone = models.CharField()
