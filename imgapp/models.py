from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        ordering=('-name',)

        #
    @staticmethod
    def get_all_categories():
        return Category.objects.all()






    def __str__(self):
        return self.name








class Image(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    img_title=models.CharField(max_length=100)
    img_tag=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    img_des=models.CharField(max_length=500)


    class Meta:
        ordering=('-img_title',)

    def __str__(self):
        return self.img_title


    @staticmethod
    def get_all_images():
        return Image.objects.all()

    @staticmethod
    def get_all_images__by_categoryid(category_id):
        if category_id:
            return Image.objects.filter(category=category_id)
        else:
            return Image.objects.all()


    def get_absolute_url(self):
        return reverse('detail',kwargs={'id':self.id})
