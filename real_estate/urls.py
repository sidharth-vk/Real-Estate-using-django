
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView ,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from listings.views import (LandingPageView,
                            LeadListView ,
                            LeadListDetail,
                            LeadDeleteDetail,
                            LeadCreateDetail,
                            LeadUpdateDetail,
                            SignUpView)







urlpatterns = [
    path('', LandingPageView.as_view(), name="landing_page" ),
    path('login/',LoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('signup/',SignUpView.as_view(), name="signup"),
    path('admin/', admin.site.urls),
    path('listing', LeadListView.as_view(),name="listing"),
    path('listing/<pk>', LeadListDetail.as_view() ),
    path('add-listing/', LeadCreateDetail.as_view()),
    path('listing/<pk>/edit', LeadUpdateDetail.as_view()),
    path('listing/<pk>/delete', LeadDeleteDetail.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
