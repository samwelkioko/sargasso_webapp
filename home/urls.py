from django.urls import path,include
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static


app_name = "home" 

urlpatterns = [
    path('',views.index,name="index"),
    path('About-Us',views.about,name="profile"),
    path('Product-Impact',views.Product_impact,name="impact"),
    path('Plastics-Recycling',views.Recycle,name="recycle"),
    path('3D-Printing',views.Print,name="print"),
    path('Our-Team',views.Team,name="team"),
    path('Careers&Opportunities',views.Job,name="jobs"),
    path('SupportUs/Donate',views.Donate,name="donate"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)