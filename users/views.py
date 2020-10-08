from django.shortcuts import render, redirect
from django.contrib import messages     # to send message about login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm    # all the forms imported.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for {username}!, now you can Login".format(username=username))
            return redirect('login')    # redirect to login page where user can login and redirect to Blog homepage

    else:   # don't save
        form = UserRegisterForm()
            
    return render(request, 'users/register.html', {'form': form})   # render same page for with context as form

# to update User or Profile
@login_required     # decorator to add functionality of login_required to access /profile
def profile(request):   
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, 
                                    instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated.")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
    