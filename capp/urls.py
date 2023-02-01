from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index),
    path('login/', login),
    path('register/', register),
    path('about/', about),
    path('contact/', contact),
    path('job/', job),
    # path('nav/', nav),
    # path('footer/', footer),
    path('profile/', profile),
    path('vacancy/<int:id>', vacancy),
    path('about/', about),
    path('contact/', contact),
    path('blog/', blog),
    path('team/', team),
    path('terms/', terms),
    path('testimonials/', testimonials),
    path('vacancydisp/', vacancydis),
    path('vacancyedit/<int:id>', vacancyedit),
    path('vacancydel/<int:id>', vacancydel),
    path('userreg/', uregister),
    path('userlogin/', ulogin),
    path('vacancyapply/', vacancyapply),
    path('viewusers/', viewusers),
    path('useredit/<int:id>', useredit),
    path('userdel/<int:id>', userdel),
    path('userdetails/<int:id>', userdetails),
    path('userdisplay/<int:id>', userdisplay),
    path('userdetailsedit/<int:id>', edituserdetails),
    path('userdetailsdelete/<int:id>', deleteuserdetails),
    path('jobapply/<int:id>', jobapply),
    path('wishlist/<int:id>', wishlist),
    path('wishlistdisplay/', wishdisplay),
    path('wishlistdelete/<int:id>', wishdelete),
    path('viewappliedusers/<int:id>', displayappliedusers),
    path('sendmail/<int:id>', email),
    path('removeapplication/<int:id>', deleteapuser),


    ]