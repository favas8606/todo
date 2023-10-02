from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . models import  Task
from . forms import TodoForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cdetail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
  
    model = Task
    template_name = ('delete.html')
    context_object_name = 'tasks'

    fields=('name','priority','date')

    success_url = reverse_lazy('todoapp:index')




def index(request):

    task1 = Task.objects.all().order_by('priority').values()
    
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name = name, priority = priority, date = date)
        task.save()

    return render(request, 'home.html', {'task1' : task1})

# def details(request):

#     task = Task.objects.all()

#     return render(request, 'details.html', {'task':task})


def done(request, id):
    tasks = Task.objects.get(id = id)
    if request.method == 'POST':
        tasks.delete()
        return redirect('/')
    return render(request, 'delete.html', {'tasks': tasks})

def update(request, id):
    task = Task.objects.get(id = id)
    form = TodoForms(request.POST or None , instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'task':task, 'form':form})

