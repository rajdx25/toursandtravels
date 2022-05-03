
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [

 path('', views.home, name = "base"),
#  path('homes/',views.homes,name='homes'),
 path('login/',LoginView.as_view(),name='login'),
 path('logout/',LogoutView.as_view(),name='logout'),
 path("contactus/",views.contactus,name="contactus"),
 path('user',views.sign_up,name='login'),
 path('user',views.logout,name='logout'),
 path('feedbackform/',views.feedbackform,name='feedbackform'),
#  path('store/',views.store,name='store')
]