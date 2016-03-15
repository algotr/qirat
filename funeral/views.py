from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from haystack.query import SearchQuerySet

from utils import contstants

from .models import Funeral

from .forms import FuneralForm


def index(request):
    funeral_list = Funeral.objects.select_related()
    paginator = Paginator(funeral_list, contstants.POSTS_PER_PAGE)
    page = request.GET.get('page')

    try:
        funerals = paginator.page(page)
    except PageNotAnInteger:
        funerals = paginator.page(1)
    except EmptyPage:
        funerals = paginator.page(paginator.num_pages)
    return render(request, 'funeral/index.html', {'funerals': funerals})


@login_required()
def add_funeral(request):
    form = FuneralForm(request.POST or None, auto_id=False)
    funeral_list = Funeral.objects.select_related().filter(author=request.user)
    paginator = Paginator(funeral_list, contstants.POSTS_PER_PAGE)
    page = request.GET.get('page')

    try:
        funerals = paginator.page(page)
    except PageNotAnInteger:
        funerals = paginator.page(1)
    except EmptyPage:
        funerals = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        if form.is_valid():
            funeral = form.save(commit=False)
            funeral.author = request.user
            # save the form data
            funeral.save()
            # save the form tags
            form.save_m2m()

            return redirect('funeral:add')
    return render(request, 'funeral/add_funeral.html',
                  {'form': form, 'funerals': funerals, 'current_url': 'funeral:add'})


@login_required()
def delete_funeral(request):
    if request.method == 'POST':
        funeral_id = request.POST.get('id')
        funeral = get_object_or_404(Funeral, pk=funeral_id)

        funeral.delete()
        success = 'success'

        if request.is_ajax():
            return HttpResponse(success)
        else:
            return redirect('funeral:add')


@login_required()
def update_funeral(request, funeral_id):
    funeral = get_object_or_404(Funeral, pk=funeral_id)
    form = FuneralForm(instance=funeral)
    funeral_list = Funeral.objects.select_related().filter(author=request.user)
    paginator = Paginator(funeral_list, contstants.POSTS_PER_PAGE)
    page = request.GET.get('page')

    try:
        funerals = paginator.page(page)
    except PageNotAnInteger:
        funerals = paginator.page(1)
    except EmptyPage:
        funerals = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = FuneralForm(request.POST, instance=funeral)
        if form.is_valid():
            funeral.place_tags.clear()
            form.save()
            return redirect('funeral:add')

    return render(request, 'funeral/add_funeral.html',
                  {'form': form, 'funerals': funerals, 'current_url': 'funeral:update', 'funeral_id': funeral_id})


def tag_funerals(request, tag_name):
    funeral_list = Funeral.objects.select_related().filter(place_tags__name__in=[tag_name])
    paginator = Paginator(funeral_list, contstants.POSTS_PER_PAGE)
    page = request.GET.get('page')

    try:
        funerals = paginator.page(page)
    except PageNotAnInteger:
        funerals = paginator.page(1)
    except EmptyPage:
        funerals = paginator.page(paginator.num_pages)

    return render(request, 'funeral/tag_funerals.html', {'tag_name': tag_name, 'funerals': funerals})

