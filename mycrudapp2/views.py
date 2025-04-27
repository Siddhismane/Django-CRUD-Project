from sys import intern
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Intern
from .forms import InternForm

def intern_list(request):
    interns = Intern.objects.all()  # Fetch all intern records from the database
    return render(request, "interns.html", {"interns": interns})


def create_intern(request):
    if request.method == "POST":
        form = InternForm(request.POST)
        if form.is_valid():
            intern = form.save()
            return JsonResponse({'id': intern.id, 'name': intern.name, 'email': intern.email, 'phone': intern.phone})
    return JsonResponse({'error': 'Invalid data'}, status=400)


def update_intern(request, intern_id):
    intern = get_object_or_404(Intern, id=intern_id)
    if request.method == "POST":
        form = InternForm(request.POST, instance=intern)
        if form.is_valid():
            intern = form.save()
            return JsonResponse({'id': intern.id, 'name': intern.name, 'email': intern.email, 'phone': intern.phone})
    return JsonResponse({'error': 'Invalid data'}, status=400)


def delete_intern(request, intern_id):
    intern = get_object_or_404(Intern, id=intern_id)
    intern.delete()
    return JsonResponse({'message': 'Intern deleted successfully'})
