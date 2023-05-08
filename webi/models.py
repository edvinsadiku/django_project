from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('home')
    class Meta:
        verbose_name_plural = "Kategorite"

class Postimet(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    #author = models.ForeignKey(User,on_delete=models.CASCADE)
    body  = RichTextField(blank=True,null=True)
    pub_date = models.DateField(default=timezone.now)


    def save(self, *args, **kwargs):
        if not self.image:
            self.image = 'images/ambienti-cover.jpg'
        super(Postimet, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Postimet"

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Materiale per shkarkim"