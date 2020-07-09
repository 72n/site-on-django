from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Showcode, Image


def index(request):
    latest_showcodes_list = Showcode.objects.order_by('-Pub_date')
    return render(request, 'MyMapView/list.html', {'latest_showcodes_list': latest_showcodes_list})

def maine(request):
    try:
        a = Showcode.objects.get(id=1)
    except:
        raise Http404("Статья не найдена")
    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'base.html', {'showcode': a, 'latest_comments_list': latest_comments_list})

def contacts(request):
    return render(request, 'MyMapView/contacts.html')

def gallery(request):
    img_list = Image.objects.order_by('-id')
    return render(request, 'MyMapView/gallery.html', {'img_list': img_list})

def detail_img(request, image_id):
    try:
        a = Image.objects.get(id=image_id)
    except:
        raise Http404("Изображение не найдено")

    img_comments_list = a.imgcomment_set.order_by('-id')

    return render(request, 'MyMapView/detail_img.html', {'image': a, 'img_comments_list': img_comments_list})

def leave_imgcomment(request, image_id):
    try:
        a = Image.objects.get(id=image_id)
    except:
        raise Http404("Статья не найдена")

    a.imgcomment_set.create(author_name=request.POST['name'], pub_date=request.POST['pub_date'] , comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('MyMapView:detail_img', args=(a.id,)))

def detail(request, showcode_id):
    try:
        a = Showcode.objects.get(id=showcode_id)
    except:
        raise Http404("Статья не найдена")

    latest_comments_list = a.comment_set.order_by('-id')

    return render(request, 'MyMapView/detail.html', {'showcode': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, showcode_id):
    try:
        a = Showcode.objects.get(id=showcode_id)
    except:
        raise Http404("Статья не найдена")

    a.comment_set.create(author_name=request.POST['name'], pub_date=request.POST['pub_date'] , comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('MyMapView:detail', args=(a.id,)))