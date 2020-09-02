from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfilePictureUpdateForm


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "User does not exist or password is wrong ! ")
            return redirect("login")
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                return redirect("login")

        else:
            messages.info(request, 'Password mismatch')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def profile(request):
    return render(request, 'profile.html')


def edit_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        profile_pic = ProfilePictureUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid and profile_pic.is_valid():
            form.save()
            profile_pic.save()
            messages.success(request, f'Your account is updated')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
        profile_pic = ProfilePictureUpdateForm(instance=request.user.profile)
        args = {
            'form': form,
            'p_pic': profile_pic
        }
        return render(request, 'edit_profile.html', args)
