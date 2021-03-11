from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
  
# Create your views here. 
def image_view(request): 
  
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('display_images') 
    else: 
        form = ImageForm() 
    return render(request, 'image.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded')

def display_images(request): 
    if request.method == 'GET': 
        # getting all the objects of image
        image = Image.objects.all()
        return render(request, 'display_images.html', {'images' : image})