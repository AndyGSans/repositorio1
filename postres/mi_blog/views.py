from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Postre
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('lista_postres'))
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def lista_postres(request):
    postres = Postre.objects.all()
    return render(request, 'lista_postres.html', {'postres': postres})

@login_required
def detalle_postre(request, pk):
    postre = get_object_or_404(Postre, pk=pk)
    return render(request, 'detalle_postre.html', {'postre': postre})


