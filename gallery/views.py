from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
# Create your views here.

from .models import ImageGallery

def index(request):
	image_list 	= ImageGallery.objects.order_by('-image_name')
	template 	= loader.get_template('gallery/index.html')
	context 	= RequestContext(
		request,{
			'image_list': image_list,
		})
	return HttpResponse(template.render(context))

def create(request):
	if request.POST:
		image 				= ImageGallery()
		image.image_name 	= request.POST['image_name']
		image.image_url		= request.POST['image_url']
		image.save()

		return HttpResponseRedirect(reverse('index'))	
	else:
		return render(request, 'gallery/create.html')