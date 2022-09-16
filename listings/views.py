from django.shortcuts import render,redirect, reverse
from .models import Listing 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView  , ListView , DetailView , CreateView , UpdateView, DeleteView
from .forms import ListingForm, CustomUserCreationForm
# Create your views here.

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("login")    

class LandingPageView(TemplateView):
    template_name = "home_page.html"   

class LeadListView(LoginRequiredMixin,ListView):
    template_name = "listings.html"
    queryset = Listing.objects.all().order_by('?')[:100]

class LeadListDetail(LoginRequiredMixin,DetailView):
    template_name = "listing.html"
    queryset = Listing.objects.all()

class LeadCreateDetail(LoginRequiredMixin,CreateView):
    template_name = "listing_create.html"
    form_class = ListingForm
    
    def get_success_url(self):
        return "/listing"
    
class LeadUpdateDetail(LoginRequiredMixin,UpdateView):
    template_name = "listing_update.html"
    queryset = Listing.objects.all()
    form_class = ListingForm
    
    def get_success_url(self):
        return "/listing"

class LeadDeleteDetail(LoginRequiredMixin,DeleteView):
    template_name = "listing_delete.html"
    queryset = Listing.objects.all()
    
    def get_success_url(self):
        return "/listing"
    

def listing_delete(request,pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/listing')