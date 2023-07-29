from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
    title = 'TITLE ENVIADO DESDE EL BACKEND!!! '
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    return render(request, 'about.html')


def hello(request,username):
    return HttpResponse('Hello %s' %username)


def projects(request):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        'projects': projects
    })


def tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse('tasks: %s' % task.title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })