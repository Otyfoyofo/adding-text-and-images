#we created this to use default classes not functions
from django.contrib import messages
from django.views.generic import TemplateView, DetailView,FormView
from .models import Post
from .form import Postforms

class HomepageView(TemplateView):
    template_name="home.html"

    def get_context_data( self, **kwargs):
        context=super().get_context_data(**kwargs)
        #context['my_things']= "hello world :P This is my page"
        context['posts']= Post.objects.all().order_by('-id')
        return context
    
class postdetailview(DetailView):
    template_name="detail.html"
    model=Post


class Addpost(FormView):
    template_name="new_post.html"
    form_class= Postforms
    success_url="/"

    def dispatch(self, request, *args, **kwargs):
        self.request= request
        return super().dispatch(request,*args, **kwargs)

    def form_valid(self,form):
      # we are going to create a form 
        new_object= Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image'],
           
        )
        messages.add_message(self.request,messages.SUCCESS, "your post is successful")
        return super().form_valid(form)


