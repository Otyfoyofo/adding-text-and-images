# this is a file created by us to use urls on homepage or to create a homepage.
from django.urls import path
from .views import HomepageView,postdetailview,Addpost

app_name='hello'

urlpatterns=[
    path('', HomepageView.as_view(), name='index'),
    path('detail/<int:pk>/',postdetailview.as_view(), name='detail'),
    path('post',Addpost.as_view(), name='post')
]
