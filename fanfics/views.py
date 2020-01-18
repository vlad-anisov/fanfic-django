from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from fanfiction.models import User
from .forms import UserForm, FanficForm
from django.http import Http404
from .models import Fanfic


def index(request):
    fanfics = Fanfic.objects.all()
    return render(request, 'fanfics/index.html', {"fanfics": fanfics})


def user_profile(request, name):
    user = get_object_or_404(User, username=name)
    fanfics = Fanfic.objects.filter(author=user)
    return render(request, 'fanfics/user_profile.html', {"user_profile": user, "fanfics": fanfics})


def user_edit(request, name):
    if request.user.username == name or request.user.is_superuser:
        user = get_object_or_404(User, username=name)
        if request.method == "POST":
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('user_edit', name=user.username)
        else:
            form = UserForm(instance=user)
        return render(request, 'fanfics/user_edit.html', {"form": form, "username": name})
    else:
        raise Http404("Poll does not exist")


def fanfic(request, pk):
    fanfic = get_object_or_404(Fanfic, pk=pk)
    return render(request, 'fanfics/fanfic.html', {"fanfic": fanfic})


def fanfic_new(request):
    if request.method == "POST":
        form = FanficForm(request.POST, request.FILES)
        if form.is_valid():
            fanfic = form.save(commit=False)
            fanfic.author = request.user
            fanfic.save()
            for tag in form.cleaned_data['tags']:
                fanfic.tags.add(tag)
            return redirect('index')
    else:
        form = FanficForm()
    return render(request, 'fanfics/fanfic_new.html', {"form": form})


def fanfic_edit(request, pk):
    fanfic = get_object_or_404(Fanfic, pk=pk)
    if request.user.username == fanfic.author.username or request.user.is_superuser:
        if request.method == "POST":
            form = FanficForm(request.POST, request.FILES, instance=fanfic)
            if form.is_valid():
                fanfic.save()
                for tag in form.cleaned_data['tags']:
                    fanfic.tags.add(tag)
                return redirect('fanfic_edit', pk=pk)
        else:
            form = FanficForm(instance=fanfic)
        return render(request, 'fanfics/fanfic_edit.html', {"form": form, "pk": pk})
    else:
        raise Http404("Poll does not exist")
