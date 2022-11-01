from django.shortcuts import redirect, render
from .forms import SignupForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = SignupForm()
    return render(request, 'register/register.html', {"form":form})