from django.views.generic import CreateView
from django.views.generic import ListView

from .forms import UserInfoModelForm
from .models import UserInfo

class Create(CreateView):
    form_class=UserInfoModelForm
    template_name='django_app/create.html'

class List(ListView):
    model=UserInfo
    template_name='django_app/list.html'
    context_object_name='data'