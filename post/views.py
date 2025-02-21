from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Thread, Post
from django.shortcuts import get_object_or_404

def home(request):
    return redirect('threads')

class ThreadListView(ListView):
    model = Thread
    template_name = 'post/thread_list.html'
    context_object_name = 'threads'

class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'post/thread_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(thread=self.object)
        return context

class ThreadCreateView(CreateView):
    model = Thread
    template_name = 'post/thread_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('threads')

class ThreadUpdateView(UpdateView):
    model = Thread
    template_name = 'post/thread_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('threads')

class ThreadDeleteView(DeleteView):
    model = Thread
    success_url = reverse_lazy('threads')
    template_name = 'post/thread_confirm_delete.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post/post_form.html'
    fields = ['title', 'picture', 'description', 'author']

    def form_valid(self, form):
        thread_id = self.kwargs.get('pk')
        form.instance.thread = get_object_or_404(Thread, pk=thread_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('thread-detail', kwargs={'pk': self.object.thread.pk})

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/post_form.html'
    fields = ['title', 'picture', 'description', 'author']

    def get_success_url(self):
        return reverse_lazy('thread-detail', kwargs={'pk': self.object.thread.pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('thread-detail', kwargs={'pk': self.object.thread.pk})
