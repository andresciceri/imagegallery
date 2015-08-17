from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from .models import ImageGallery, Contact

def index(request):
	image_list 	= ImageGallery.objects.order_by('-image_name')
	template 	= loader.get_template('index.html')
	context 	= RequestContext(
		request,{
			'image_list': image_list,
		})
	return HttpResponse(template.render(context))

def get_all_images(request):
	return HttpResponse("Response all images")

def get_all_images_by_user(request):
	return HttpResponse("Respons to images by user")

def upload_image_by_url(request):
	if request.POST:
		image 				= ImageGallery()
		image.image_name 	= request.POST['image_name']
		image.image_url		= request.POST['image_url']
		image.save()

		return HttpResponseRedirect(reverse('index'))	
	else:
		return render(request, 'create.html')

def about(request):

	return render(request, 'about.html')

def contact(request):
	if request.POST:
		contact			= Contact()
		contact.name 	= request.POST['name']
		contact.email	= request.POST['email']
		contact.phone	= request.POST['phone']
		contact.comment	= request.POST['comment']
		contact.save()

		return HttpResponseRedirect(reverse('index'))	
	else:
		return render(request, 'contact.html')

	