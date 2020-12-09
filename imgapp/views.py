from django.shortcuts import render,get_object_or_404
from .models import Category,Image
from .forms import ImageForm,CategoryForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.


def Image_List_View(request):
    result=None
    categories=Category.get_all_categories()
    category_id=request.GET.get('category')
    if category_id:
        result=Image.get_all_images__by_categoryid(category_id)
    else:
        result=Image.get_all_images()
    paginator=Paginator(result,8)
    page_number=request.GET.get('page')
    try:
        result=paginator.page(page_number)
    except PageNotAnInteger:
        result=paginator.page(1)
    except EmptyPage:
        result=paginator.page(paginator.num_pages)



    return render(request,'testapp/imglist.html',{'categories':categories,'result':result})

def Image_detailed_View(request,id):
    categories=Category.get_all_categories()
    image=Image.objects.get(pk=id)
    return render(request,'testapp/imgdetail.html',{'image':image,'categories':categories})






def add_post_view(request):
    form=ImageForm()
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            new_form=form.save(commit=False)
            print(new_form)
            print(request.FILES)
            new_form.image=request.FILES['image']
            new_form.save()
            print(new_form.image)
        return HttpResponseRedirect('/')
    else:
        form=ImageForm()
    return render(request,'testapp/addpost.html',{'form':form})


def add_category_view(request):
    form=CategoryForm
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')


    return render(request,'testapp/addcategory.html',{'form':form})
