from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import UserAPIKey, AdzunaJob, Database, Platform, TopTech, WebFramework, GithubRepo, JobOffer, RemoteokJob
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.http import HttpResponseForbidden
from rest_framework import viewsets

# Décorateur de vérification de clé API
def require_api_key(view_func):
    def _wrapped_view(request, *args, **kwargs):
        api_key = request.headers.get('X-API-KEY')
        if not api_key or not UserAPIKey.objects.filter(key=api_key).exists():
            return HttpResponseForbidden('Clé API invalide ou manquante.')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


@login_required
def get_api_key(request):
    api_key, created = UserAPIKey.objects.get_or_create(user=request.user)
    return JsonResponse({'api_key': api_key.key})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    api_key, _ = UserAPIKey.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'user': request.user, 'api_key': api_key.key})


def home(request):
    return render(request, 'home.html')


@require_GET
@require_api_key
def adzuna_job_list(request):
    page_number = request.GET.get('page', 1)
    jobs = AdzunaJob.objects.all().order_by('id')
    paginator = Paginator(jobs, 20)
    page = paginator.get_page(page_number)
    data = [
        {
            'id': job.id,
            'company': job.company,
            'description': job.description,
            'industry': job.industry,
            'job_title': job.job_title,
            'location': job.location,
            'skills': job.skills,
        }
        for job in page
    ]
    return JsonResponse({'count': paginator.count, 'num_pages': paginator.num_pages, 'results': data})


@require_GET
@require_api_key
def database_list(request):
    page_number = request.GET.get('page', 1)
    items = Database.objects.all().order_by('id')
    paginator = Paginator(items, 20)
    page = paginator.get_page(page_number)
    data = [
        {'id': obj.id, 'database': obj.database, 'usage_count': obj.usage_count}
        for obj in page
    ]
    return JsonResponse({'count': paginator.count, 'num_pages': paginator.num_pages, 'results': data})


@require_GET
@require_api_key
def platform_list(request):
    page_number = request.GET.get('page', 1)
    items = Platform.objects.all().order_by('id')
    paginator = Paginator(items, 20)
    page = paginator.get_page(page_number)
    data = [
        {
            'id': obj.id,
            'platform': obj.platform,
            'usage_count': obj.usage_count
        }
        for obj in page
    ]
    return JsonResponse({'count': paginator.count, 'num_pages': paginator.num_pages, 'results': data})

@require_GET
@require_api_key
def top_tech_list(request):
    page_number = request.GET.get('page', 1)
    items = TopTech.objects.all().order_by('id')
    paginator = Paginator(items, 20)
    page = paginator.get_page(page_number)
    data = [
        {'id': obj.id, 'offer_count': obj.offer_count, 'technology': obj.technology}
        for obj in page
    ]
    return JsonResponse({'count': paginator.count, 'num_pages': paginator.num_pages, 'results': data})


@require_GET
@require_api_key
def web_framework_list(request):
    page_number = request.GET.get('page', 1)
    items = WebFramework.objects.all().order_by('id')
    paginator = Paginator(items, 20)
    page = paginator.get_page(page_number)
    data = [
        {'id': obj.id, 'web_framework': obj.web_framework, 'usage_count': obj.usage_count}
        for obj in page
    ]
    return JsonResponse({'count': paginator.count, 'num_pages': paginator.num_pages, 'results': data})

@require_GET
@require_api_key
def github_repo_list(request):
    page_number = request.GET.get('page', 1)
    repos = GithubRepo.objects.all().order_by('id')
    paginator = Paginator(repos, 20)
    page = paginator.get_page(page_number)
    data = [
        {
            'id': repo.id,
            'name': repo.name,
            'owner': repo.owner,
            'language': repo.language,
            'stargazers_count': repo.stargazers_count,
            'forks_count': repo.forks_count,
            'html_url': repo.html_url,
            'open_issues_count': repo.open_issues_count,
            'watchers_count': repo.watchers_count,
        }
        for repo in page
    ]
    return JsonResponse({'count': paginator.count, 'num_pages': paginator.num_pages, 'results': data})

@require_GET
@require_api_key
def job_offer_list(request):
    page_number = request.GET.get('page', 1)
    offers = JobOffer.objects.all().order_by('id')
    paginator = Paginator(offers, 20)
    page = paginator.get_page(page_number)
    data = [
        {
            'id': offer.id,
            'job_title': offer.job_title,
            'company': offer.company,
            'salary': offer.salary,
            'contract': offer.contract,
            'remote': offer.remote,
            'city': offer.city,
        }
        for offer in page
    ]
    return JsonResponse({'count': paginator.count, 'num_pages': paginator.num_pages, 'results': data})


def remoteok_job_list(request):
    page_number = request.GET.get('page', 1)
    jobs = RemoteokJob.objects.all().order_by('id')
    paginator = Paginator(jobs, 20)
    page = paginator.get_page(page_number)
    
    data = [
        {
            'id': job.id,
            'job_title': job.job_title,
            'company': job.company,
            'source': job.source,
            'country': job.country,
            'job_link': job.job_link,
        }
        for job in page
    ]
    
    return JsonResponse({'count': paginator.count,'num_pages': paginator.num_pages,'results': data})



