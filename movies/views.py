
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from .models import *
from .forms import *
from .service import send
from .tasks import send_spam_email


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movies.objects.filter(draft=True).values("year")

    def get_category(self):
        return Category.objects.all()

    def get_age(self):
        return Movies.objects.filter(draft=True).values("age")

    def get_name(self):
        return Movies.objects.filter(draft=True).values('name')


class HomeView(GenreYear, ListView):
    model = Movies
    template_name = 'movies/index.html'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = Movies.objects.all()
        context['logo'] = Logo.objects.last()
        context['users'] = User.objects.all()
        return context


class MovieView(GenreYear,FormMixin, DetailView):
    model = Movies
    template_name = 'movies/Movie.html'
    context_object_name = 'movie'
    form_class = CommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.all()

        return context

    #def get_queryset(self, **kwargs):
    #    return Movies.objects.filter(slug=self.kwargs['slug'])

    def get_success_url(self, **kwargs):
        return reverse_lazy('movie', kwargs={'slug': self.get_object().slug})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return redirect('login')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


def update_comment_status(request, pk, type):
    item = Comments.objects.get(pk=pk)
    if request.user.is_superuser or request.user == item.author:
        if type == 'delete':
            item.delete()


def admin_panel(request):
    context = {
        'list_articles': Movies.objects.all().order_by('-id')
    }
    return render(request, 'movies/admin_panel.html', context)


def update_movie_redact(request, pk, type):
    item = Movies.objects.get(pk=pk)
    if type == 'delete':
        item.delete()


def post_edit(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    if request.method == "POST":
        form = AddViewForm(request.POST, instance=movie)
        if form.is_valid():
            movie.save()
            return redirect('admin_panel')

    else:
        form = AddViewForm(instance=movie)
    return render(request, 'movies/addmovie.html', {'form': form})


class AddView(LoginRequiredMixin,CreateView):
    form_class = AddViewForm
    template_name = 'movies/addmovie.html'
    success_url = reverse_lazy('admin_panel')
    raise_exception = True


class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'movies/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'movies/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def Logout(request):
    logout(request)
    return redirect('login')


class FilterMoviesView(GenreYear, ListView):
    template_name = 'movies/index.html'

    def get_queryset(self):
        queryset = Movies.objects.all()
        if "genre" in self.request.GET:
            queryset = queryset.filter(genres__in=self.request.GET.getlist("genre")).distinct()
        if "year" in self.request.GET:
            queryset = queryset.filter(year__in=self.request.GET.getlist("year")).distinct()
        if 'category' in self.request.GET:
            queryset = queryset.filter(category__in=self.request.GET.getlist('category')).distinct()
        if 'age' in self.request.GET:
            queryset = queryset.filter(age__in=self.request.GET.getlist('age')).distinct()
        if 'name' in self.request.GET:
            queryset = queryset.filter(Q(name__in=self.request.GET.getlist('name')) | (Q(name__iregex=self.request.GET.get('name'))))
        return queryset


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    template_name = 'movies/contact.html'

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)

