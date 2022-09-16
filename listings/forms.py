from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UsernameField
from .models import Listing
from django.contrib.auth import get_user_model

User = get_user_model()




class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "price",
            "discription",
            "num_bedrooms",
            "num_bathrooms",
            "square_footage",
            "address",
            "image",
            'image1',
            'image2',
            'agent'
        ]
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}