from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST
from .models import Page
from .forms import PageForm

def home(request):
    query = request.GET.get('q')
    if query:
        pages = Page.objects.filter(title__icontains=query)
    else:
        pages = Page.objects.all()
    return render(request, 'pages/home.html', {'pages': pages, 'query': query})

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'pages/page_detail.html', {'page': page})

@login_required
def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user  # asigna autor automáticamente
            page.save()
            return redirect('home')
    else:
        form = PageForm()
    return render(request, 'pages/page_form.html', {'form': form})

@login_required
def page_edit(request, slug):
    page = get_object_or_404(Page, slug=slug)
    if page.author != request.user:
        return HttpResponseForbidden("No tienes permiso para editar esta página.")

    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect('page_detail', slug=page.slug)
    else:
        form = PageForm(instance=page)
    return render(request, 'pages/page_form.html', {'form': form, 'page': page})

@login_required
@require_POST
def page_delete(request, slug):
    page = get_object_or_404(Page, slug=slug)
    if page.author != request.user:
        return HttpResponseForbidden("No tienes permiso para borrar esta página.")
    page.delete()
    return redirect('home')

def about(request):
    return render(request, 'pages/about.html')