from django.urls import path
from.import views
app_name='mybooks'


urlpatterns=[
    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('masterpage/',views.masterpage,name='masterpage'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('seeallbooks/',views.seeallbooks,name='seeallbooks'),
    path('addbooks/',views.addbooks,name='addbooks'),
    path('reviews/<int:bid>',views.reviews,name='reviews'),
    path('like/',views.like,name='like'),
    path('add_to_liked/<int:bid>',views.add_to_liked,name='add_to_liked'),
    path('remove/<int:bid>',views.remove,name='remove')
    
    
]
