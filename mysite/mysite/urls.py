
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('subscribe/', include('subscribe.urls')),
    path('registration/', include('registration.urls')),
    path('upload/', include('profile_maker.urls')),
    path('', include('home.urls')),
    path('', include('home.urls')),
   # path('design/', include('design.urls')),
    path('ajax/', include('post.urls'))
]
