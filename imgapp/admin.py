from django.contrib import admin
from .models import Image,Category

class ImageAdmin(admin.ModelAdmin):
    list_display=['category','img_tag','img_title','image','img_des']

# Register your models here.
admin.site.register(Image,ImageAdmin)
admin.site.register(Category)
