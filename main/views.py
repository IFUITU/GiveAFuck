from django.shortcuts import render,redirect, reverse
from .models import Game, Platform, Post_Img
from django.core.paginator import Paginator
from django.views.generic import ListView, View #methods of base classes 
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.conf import settings
from main.decorators import login_required
from datetime import datetime, timedelta

# from django.views.decorators.csrf import csrf_exempt
import os 
import string
import random
# Create your views here.



def index(request):
    games = Game.objects.select_related('platform').filter(bonus=False).order_by("-pub_date").all()
    paginator = Paginator(games, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(request.method)

    return render(request, 'pages/home.html', {"games":page_obj})

class Like(View,LoginRequiredMixin):
    def get(self, request, pk, type):#why get?
        try:
            Games = Game.objects.get(id=pk)
        except:
            return Http404()
        if type == 'u':
            Games.likes += 1
            Games.count_dwnd += 1
            Games.save()
            return HttpResponse("{}".format(Games.likes))
        elif type == 'd':
            Games.count_dwnd += 2
            Games.likes += 1
            if Games.file.name != "":
                hash = str(random.choice(string.ascii_letters)) + str(random.choice(string.digits))
                ext = Games.file.name.split('.')[-1]
                file_path = str(Games.file.path)
                
                child_path = Games.file.name.split('/')[:-1]
                old_filename = Games.file.name.split('/')[-1]
                
                new_filename = '{}.{}'.format( hash + Games.title, ext)
                new_path = file_path.replace(old_filename, new_filename)
                Games.file.name = ''.join(child_path) + '/' + new_filename
                # print(Games.file.path,'/////////////////////', new_path, '+++++++++++++++++++++++++++++++++++++++++',new_filename)
                
                os.rename(r'{}'.format(file_path), r'{}'.format(new_path))
            
                Games.save()
            
                return HttpResponseRedirect(settings.MEDIA_URL + str(Games.file)) #HttpResponse('{}'.format(Games.count_dwnd))
            return HttpResponseRedirect(reverse( 'main:bonus', args=(pk,)))

    def post(self, request, pk, type):
        try:
            Games = Game.objects.get(id=pk)
            vote = request.POST.get('rating2')
        except:
            raise Http404('Page Not Fount')
        
        if vote != None:
            if type == "v":
                Games.count_dwnd += 2
                Games.likes += 1
                Games.rated_user += 1
                Games.oponion += int(vote)
                Games.stars = (Games.oponion/Games.rated_user) 
                Games.save()
        else:
            print('messages if vote is None')
        return HttpResponseRedirect(reverse('main:detail', args=(pk,)))

# @csrf_exempt
def detail(request, id):
    try:
        obj = Game.objects.get(id=id)
    except:
        raise Http404('Page Not Fount')
    photos = Post_Img.objects.filter(game_id=id)
    recommend_query = Game.objects
    recommend_query = recommend_query.filter(
        ((Q(platform_id=int(obj.platform.pk)) & Q(count_dwnd__gte=100)) 
        | (Q(platform_id=int(obj.platform.pk)) & Q(pub_date__gte=(datetime.now() - timedelta(15))))
        ) & ~Q(id=id)
    ).all()[0:3]

    # file_path = settings.MEDIA_URL + str(Games.file.path)
    # ext = obj.file.name.split('.')[-1]
    
    
    
    return render(request, "pages/detail.html", {'object':obj, 'photos':photos, 'recommend':recommend_query})

def by_category(request, id):
    # obj = Game.objects.filter(category__id=id)
    current_platform = Platform.objects.get(id=id)
    try:
        obj = Game.objects.select_related('platform').filter(platform_id=id).all().order_by('-count_dwnd')
    except:
        raise Http404('Page Not Fount')
    paginator = Paginator(obj, 10)
    page_number = request.GET.get('page')    
    page_obj = paginator.get_page(page_number)
    
    
    # current_category_query = Category.objects.get(id=id)
    # print(current_platform)
    return render(request, 'pages/category.html', {'games':page_obj, 'current_platform':current_platform})


def top_100(request):
    obj = Game.objects.select_related('platform').filter(count_dwnd__gt=10).all()
    paginator = Paginator(obj, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'pages/top-100.html', {'games':page_obj})

# @login_required
def bonuses(request):
    obj = Game.objects.select_related('platform').filter(bonus=True).order_by('-pub_date').all()
    paginator = Paginator(obj, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'pages/bonus.html', {"games":page_obj})

def search(request):
    keyword = request.GET.get('searchField','')
    query = Game.objects
    
    if keyword != '':
        query = query.filter(
            Q(title__icontains=keyword) | Q(platform__name_eng__icontains=keyword) 
        )
    # title__icontains = request.GET.get('q','') # search via get method q attribute='value'
    else:
        return redirect('main:index')
    
    paginator = Paginator(query, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/home.html',{'games':page_obj})


class Bonus_Detail(View,LoginRequiredMixin):
    def get(self, request, id):
        try:
            obj = Game.objects.get(id=id)
        except:
            raise Http404('Page Not Fount')

        query = Game.objects
        query = query.filter(
            (Q(platform_id=int(obj.platform.pk)) | ~Q(video='') | Q(count_dwnd__gte=20) | Q(pub_date__gte=(datetime.now()-timedelta(30)))) & ~Q(id=id) 
        ).all()[0:3]
        
        # game_recommend = Game.objects.filter(platform_id=int(obj.platform.pk)).filter(video!='').exclude(id=id).all()[0:3]
        

        return render(request, 'pages/bonus_detail.html', {'object':obj ,'recommend':query})
    def post(self,request):
        return redirect('main:index')