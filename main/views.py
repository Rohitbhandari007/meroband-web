from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Post
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostUpdateForm
from django.contrib.auth.models import User, auth
from django.urls import reverse


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'home1.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'home1.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title',
        'content',
        'videos'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        'content',
        'videos'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required()
def updatepost(request):
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=request.user.post.videos)

        if form.is_valid:
            form.save()

            return redirect('profile')

    else:
        form = PostUpdateForm(instance=request.user)
        args = {
            'form': form,
        }
        return render(request, 'post_form.html')
