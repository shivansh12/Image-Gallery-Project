from django import forms
from .models import Category,Image


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name',)


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=('category','img_tag','img_title','img_des','image')


        widgets={

        'category':forms.Select(
         attrs={
         'class':'form-control',
         }
         ),
         'img_title':forms.TextInput(
         attrs={
         'class':'form-control',
         }
         ),
         'img_tag':forms.TextInput(
         attrs={
         'class':'form-control',
         }
         ),
         'img_des':forms.Textarea(
         attrs={
         'class':'form-control',
         }
         ),


           }
