from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Portfolio
from .forms import PortfolioForm

# Create your views here.
def portfolio_home(request):
    return render(request, 'portfolio/portfolio_home.html')

# List all projects
@login_required
def portfolio_list(request):
    project = Portfolio.objects.order_by('-created_at')[:8] # Get the 8 most recent projects
    return render(request, 'portfolio/portfolio_list.html', {'projects': project})

# Show project details
@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Portfolio, id=project_id)
    return render(request, 'portfolio/project_detail.html', {'project': project})

# Create a new project
@login_required
@user_passes_test(lambda u: u.is_staff)
def portfolio_create(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioForm()
    return render(request, 'portfolio/portfolio_form.html', {'form': form})

# Update a project
@login_required
@user_passes_test(lambda u: u.is_staff)
def portfolio_update(request, project_id):
    project = get_object_or_404(Portfolio, id=project_id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project_id)
    else:
        form = PortfolioForm(instance=project)
    return render(request, 'portfolio/portfolio_form.html', {'form': form})

# Delete a project
@login_required
@user_passes_test(lambda u: u.is_staff)
def portfolio_delete(request, project_id):
    project = get_object_or_404(Portfolio, id=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio_list')
    return render(request, 'portfolio/portfolio_confirm_delete.html', {'project': project})

# Custom login view
def custom_logout(request):
    logout(request)
    return redirect('portfolio_home')