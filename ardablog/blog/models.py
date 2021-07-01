from django.db import models

# Create your models here.
class Yazılar(models.Model):
    pub_date=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=50 ,default='SOME STRING')
    article=models.TextField(default='SOME STRING')
    def __str__(self):
        return self.title
    
class Resimler(models.Model):
    ctgry=models.CharField(verbose_name="Category", max_length=50,default='SOME STRING')
    src = models.TextField(verbose_name="Src",default='SOME STRING')
    detail=models.TextField(default='SOME STRING')