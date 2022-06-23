from django.urls import reverse_lazy
from django.views.generic.edit import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from jay208.blog.models import post

# Create your views here.

class PostListView(ListView):
    model = post

    class PostCreateView(CreateView):
        model = post
        fields = "__all__"
        success_url = reverse_lazy("blog:all")

        class PostDetailView(DetailView):
            model = post

            class PostUpdateView(UpdateView):
                model = post

                class PostDeleteView(DeleteView):
                    model = post
                    fields = "__all__" 
                    success_url = reverse_lazy("blog:all")
        
