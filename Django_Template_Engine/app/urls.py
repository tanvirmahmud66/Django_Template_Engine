from django.urls import path
from django.views.generic import TemplateView
from .views import Home, PublisherListView, SinglePublisherView, CreatePublisherView, EditPublisherView, DeletePublisherView

urlpatterns = [

    path('', TemplateView.as_view(template_name='about.html'), name='home'),
    path('', Home.as_view(), name="home"),
    path('all-publisher/', PublisherListView.as_view(), name='all-publisher'),
    path('single-publisher/<int:publisher_id>/', SinglePublisherView.as_view(), name='single-publisher'),
    path('create-publisher/', CreatePublisherView.as_view(), name='create-publisher'),
    path('edit-publisher/<int:publisher_id>/', EditPublisherView.as_view(), name='edit-publisher'),
    path('delete-publisher/<int:pk>/', DeletePublisherView.as_view(), name='delete-publisher'),
]