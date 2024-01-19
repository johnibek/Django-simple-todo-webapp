from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TodoForm
from .models import Todo


def home(request):
    item_list = Todo.objects.order_by('-date')
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    page = {
        'forms': form,
        'list': item_list,  
        'title': 'TODO LIST'
    }

    return render(request, 'todo/index.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    messages.warning(request, 'hello there')
    return redirect('home')

