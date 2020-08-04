from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from django.views.generic import CreateView, FormView
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage

from .forms import signup_form, login_form
from django.views.generic import TemplateView

User=get_user_model()

def home(request):
    
    return render(request, 'django_app/home.html',{})


class signup_view(FormView):
    def post(self, request, *args, **kwargs):
        form = signup_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = User(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],

            )
            # file_obj=request.FILES['myfile']
            # fs=FileSystemStorage()
            # filename=fs.save(file_obj.name,file_obj)

            user.save()
            user.set_password(form.cleaned_data['password'])  
            user.save()

            username = form.cleaned_data['username']
            subject = f'Your Account is verified as {username}'
            message = f'Congratulations!! Your account is verified as {username} and now you can access our site as our User.Thank You!'
            from_email = 'prathamshrestha358@gmail.com'
            recipients = [request.user.email, ]
            send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipients)
            # print(f'verification sent to {email}')
            return redirect('login')
        return redirect('signup')

    def get(self, request, *args, **kwargs):
        form = signup_form()
        return render(request, 'django_app/signup.html', {'form': form})


class login_view(View):
    # form_class = AuthenticationForm
    #
    template_name = 'django_app/login.html'

    # success_url = 'profile'

    def post(self, request, *args, **kwargs):
        form = login_form(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                print('user found', user)
                login(request, user)
                return redirect('profile')
            else:
                print('user not found', user)
        return redirect('login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')

        form = login_form()
        return render(request, 'django_app/login.html', {'form': form})

# @login_required(login_url='login/')
class profile(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'django_app/profile.html')



class logout_view(View):
    def get(self, request):
        logout(request)
        return redirect('login')




# class crud_home(TemplateView):
#     template_name='django_app/home.html'
#     def post(self,request):
#         pass