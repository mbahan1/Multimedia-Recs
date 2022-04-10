from dataclasses import fields
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views import View # View class to handle requests
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect # This is our responses
from django.urls import reverse
from .models import Show, Review
from django.contrib.auth.models import User
# Auth imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Show_List(TemplateView):
    template_name = 'show_idx.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #this gets the title query parameter to access it 
        title = self.request.GET.get("title")
        #if the query exists we will filter by title
        if title != None:
            # .filter is the sql WHERE statement and title__icontains is doing a search for any title that contains the query param
            context["shows"] = Show.objects.filter(title__icontains=title)
            context["header"] = f"Searching for {title}"
        else: 
            context['shows'] = Show.objects.all() # this is where we add the key into our context object for the view to use
            context['header'] = "Our Shows"
        return context

@method_decorator(login_required, name='dispatch')
class Show_Create(CreateView):
    model = Show
    fields = ['title', 'first_aired', 'last_aired', 'genre', 'stream_service', 'img', 'description']
    template_name = "show_create.html"
    # def get_success_url(self):
    #     return reverse('show_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/shows')

class Show_Detail(DetailView):
    model = Show
    template_name="show_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Show_Detail, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Show, id=self.kwargs['pk'])
        total_thumbs = stuff.total_thumbs()
        # recced_by = stuff.recced_by()
        # context["recced_by"] = recced_by
        context["total_thumbs"] = total_thumbs
        return context 

@method_decorator(login_required, name='dispatch')
class Show_Update(UpdateView):
    model = Show
    fields = ['title', 'first_aired', 'last_aired', 'genre', 'stream_service', 'img', 'description']
    template_name = "show_update.html"
    def get_success_url(self):
        return reverse('show_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class Show_Delete(DeleteView):
    model = Show
    template_name = "show_delete_confirmation.html"
    success_url = "/shows/"

#user profile
@login_required #because it isn't a class, just a function
def profile(request, username):
    user = User.objects.get(username=username)
    shows = Show.objects.filter(user=user)
    reviews = Review.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'shows': shows, 'reviews': reviews})

#Show Reviews
def reviews_index(request):
    reviews  = Review.objects.all()
    return render(request, 'review_index.html', {'reviews': reviews})

def reviews_show(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'review_show.html', {'review': review})

@method_decorator(login_required, name='dispatch')
class ReviewCreate(CreateView):
    model = Review
    fields = ['body']
    template_name = "review_form.html"
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.show_id = self.kwargs['pk']
        self.object.save()
        return HttpResponseRedirect('/shows')

@method_decorator(login_required, name='dispatch')
class ReviewUpdate(UpdateView):
    model = Review
    fields = ['body']
    template_name = "review_update.html"
    success_url = '/reviews'

@method_decorator(login_required, name='dispatch')
class ReviewDelete(DeleteView):
    model = Review
    template_name = "review_confirm_delete.html"
    success_url = '/reviews'

# Login, Logout and Signup
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/shows')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'signup.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def thumb_view(request, pk):
    show = get_object_or_404(Show, id=request.POST.get('show_id'))
    show.thumbs.add(request.user)
    return HttpResponseRedirect(reverse('show_detail', args=[str(pk)]))

#Show Users
def users_index(request):
    users  = User.objects.all()
    return render(request, 'user_index.html', {'users': users})

def get_queryset(self):
    return User.objects.all()