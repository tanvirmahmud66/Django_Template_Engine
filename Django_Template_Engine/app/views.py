from django.shortcuts import render
from .models import Publisher
from .forms import PublisherForm, AuthorForm, BookForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.views import View
from django.urls import reverse_lazy, reverse

# Create your views here.


# class base view with TemplatesView
class Home(TemplateView):
    template_name = 'home.html'




class PublisherListView(ListView):
    model = Publisher #------------------------------------------ model name that retrieve data from 
    template_name = 'publishersList.html' #---------------------- tamplate name
    context_object_name = 'Publishers' #------------------------- dataset name for template
    # queryset = Publisher.objects.all() #------------------------- queryset for custom data retrieve
    # paginate_by = 10 #------------------------------------------- Specifies the number of objects to display per page
    ordering = ['-id'] #--------------------------- Allows you to specify the default ordering for the queryset
    extra_context = {
        'value1': 1,
        'value2': 2
    } #---------------------------------------------------------- Provides additional context data to be included in the template
    # http_method_names = ['get'] #-------------------------------- Restricts the allowed HTTP methods for the view
    # def get_queryset(self):
    #     category_id = self.kwargs['category_id']  #-------------- gives you parameter value through url
    #     return YourModel.objects.filter(category_id=category_id)





class SinglePublisherView(DetailView):
    model = Publisher #--------------------------------------------------------- Specifies the model from which the object is retrieved
    # queryset = YourModel.objects.filter(some_condition=True) #---------------- Allows you to provide a custom queryset instead of using the default
    template_name = 'singlepublisher.html' #------------------------------------ Specifies the template used to render the view
    context_object_name = 'publisher' #----------------------------------------- Sets the variable name used in the template to access the object
    # slug_field = 'modelname_slug' #----------------------------------------------------- Used when you want to perform a lookup using a slug field instead of the primary key
    # slug_url_kwarg = 'slug' #------------------------------------------------- Used when you want to perform a lookup using a slug field instead of the primary key
    pk_url_kwarg = 'publisher_id' #---------------------------------------------- Used to specify the name of the URL keyword argument containing the primary key
    # query_pk_and_slug = True #------------------------------------------------ If set to True, the view will consider both pk and slug when retrieving the object
    # extra_context = {'additional_info': 'Some extra information'} #----------- Provides additional context data to be included in the template
    # http_method_names = ['get'] #--------------------------------------------- Restricts the allowed HTTP methods for the view.





class CreatePublisherView(CreateView):
    model = Publisher #--------------------------------------------------------- Specifies the model that the view will create an instance of.
    form_class = PublisherForm #------------------------------------------------ Specifies the form class that the view will use
    context_object_name = 'newly_created_object_forTemplates' #----------------- Sets the variable name used in the template to access the created object.
    template_name = 'createpublisher.html' #------------------------------------ Specifies the template used to render the view
    # initial = {'field1': 'initial_value'} #------------------------------------- Allows you to specify initial data for the form
    # extra_context = {'additional_info': 'Some extra information'} #----------- Provides additional context data to be included in the template    


    def get_success_url(self):
        return reverse('all-publisher') #--------------------------------------- Specifies the URL to redirect to after the object is successfully created




class EditPublisherView(UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'editpublisher.html'
    
    def get_success_url(self):
        return reverse('single-publisher', args=(self.object.id,))
    
    # def form_valid(self, form):
    #     # Update only the 'id' and 'name' fields without touching other fields
    #     self.object.field_name = form.cleaned_data['field_name']
    #     self.object.field_name = form.cleaned_data['field_name']
    #     self.object.save()
    #     return super().form_valid(form)



class DeletePublisherView(DeleteView):
    model = Publisher
    template_name = 'deletepublisher.html'
    context_object_name = 'object'
    success_url = reverse_lazy('all-publisher')


