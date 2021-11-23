from apps.users.models import User
from apps.users.forms import UserCreateForm
from django.views import generic
from django.urls import reverse_lazy

class UserCreateView(generic.CreateView):
    
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


