from django.contrib import admin
from .models import Listing, Agent,UserProfile,User
# Register your models here.


admin.site.register(Listing)
admin.site.register(UserProfile)
admin.site.register(Agent)
admin.site.register(User)